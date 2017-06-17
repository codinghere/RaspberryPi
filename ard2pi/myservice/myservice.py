import sys
from struct import unpack

import logging
import logging.handlers
import argparse


from PyQt5.QtCore import QObject, qCritical, qDebug, QTimer, QByteArray, QCoreApplication
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtSql import QSqlDatabase, QSqlQuery



# Deafults
LOG_FILENAME = "/tmp/myservice.log"
LOG_LEVEL = logging.INFO  # Could be e.g. "DEBUG" or "WARNING"

# Define and parse command line arguments
parser = argparse.ArgumentParser(description="My simple Python service")
parser.add_argument("-l", "--log", help="file to write log to (default '" + LOG_FILENAME + "')")

# If the log file is specified on the command line then override the default
args = parser.parse_args()
if args.log:
    LOG_FILENAME = args.log

# Configure logging to log to a file, making a new file at midnight and keeping the last 3 day's data
# Give the logger a unique name (good practice)
logger = logging.getLogger(__name__)
# Set the log level to LOG_LEVEL
logger.setLevel(LOG_LEVEL)
# Make a handler that writes to a file, making a new file at midnight and keeping 3 backups
handler = logging.handlers.TimedRotatingFileHandler(LOG_FILENAME, when="midnight", backupCount=3)
# Format each log message like this
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
# Attach the formatter to the handler
handler.setFormatter(formatter)
# Attach the handler to the logger
logger.addHandler(handler)


# Make a class we can use to capture stdout and sterr in the log
class MyLogger(object):
    def __init__(self, logger, level):
        """Needs a logger and a logger level."""
        self.logger = logger
        self.level = level

    def write(self, message):
        # Only log if there is a message (not just a new line)
        if message.rstrip() != "":
            self.logger.log(self.level, message.rstrip())


class DataBaseManager(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)
        self.createConnection()

    def createConnection(self):
        db = QSqlDatabase.addDatabase('QMYSQL')
        db.setHostName("localhost")
        db.setDatabaseName('ard2pi')
        db.setUserName("root")
        db.setPassword("raspberry")
        if not db.open():
            qCritical("Not open")
        self.createTable()

    def createTable(self):
        query = QSqlQuery()
        query.exec_("CREATE TABLE if not EXISTS Monitoreo (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, "
                    "created_at timestamp default current_timestamp,"
                    "Temperatura FLOAT, Humedad FLOAT)")

        if query.lastError().isValid():
            qCritical("Error: " + query.lastError().text())

    def saveData(self, value):
        val1, val2 = value
        query = QSqlQuery()
        query.exec_("insert into Monitoreo (Temperatura, Humedad) values('{}', '{}')".format(val1, val2))
        qDebug("{:.1f}, {:.1f}".format(val1, val2))
        if query.lastError().isValid():
            qCritical("Error: " + query.lastError().text())


class SerialPortManager(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)
        self.serial = QSerialPort(self)
        self.serial.error.connect(self.handleError)
        self.serial.readyRead.connect(self.readData)
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.writeData("@"))
        self.timer.start(1000)
        self.dbManager = DataBaseManager(self)

        self.data = QByteArray()

    def handleError(self, error):
        if error == QSerialPort.ResourceError:
            qCritical("Serial Port error:" + self.serial.errorString())
            self.closeSerialPort()

    def closeSerialPort(self):
        self.serial.close()
        qDebug("Disconnected")

    def readData(self):
        if self.serial.bytesAvailable() > 0:
            data = self.serial.readAll()
            self.data.append(data)
            if self.data.size() > 8:
                val = self.data[:8]
                self.dbManager.saveData(unpack("ff", val))
                self.data = self.data[8:]

    def writeData(self, data):
        self.serial.write(data)

    def openSerialPort(self):
        portToUse = None
        for info in QSerialPortInfo.availablePorts():
            s = "Port: {}\n".format(info.portName())
            s += "Location: {}\n".format(info.systemLocation())
            s += "Description: {}\n".format(info.description())
            s += "Manufacturer: {}\n".format(info.manufacturer())
            s += "Serial number: {}\n".format(info.serialNumber())
            s += "Vendor Identifier: {}\n".format(info.hasVendorIdentifier())
            s += "Product Identifier: {}\n".format(info.hasProductIdentifier())
            s += "Busy: {}\n".format("Yes" if info.isBusy() else "No")

            if not info.isBusy() and (
                            "Arduino" in info.description().encode() or "Arduino" in info.manufacturer().encode()):
                portToUse = info
            qDebug(s)

        if not portToUse or not portToUse.isValid():
            qDebug("port is not valid:" + portToUse.portName())
            return

        self.serial.setPortName(portToUse.portName())
        self.serial.setBaudRate(QSerialPort.Baud115200)
        self.serial.setDataBits(QSerialPort.Data8)
        self.serial.setParity(QSerialPort.NoParity)
        self.serial.setStopBits(QSerialPort.OneStop)
        self.serial.setFlowControl(QSerialPort.NoFlowControl)

        if self.serial.open(QSerialPort.ReadWrite):
            qDebug("Connected to " + portToUse.manufacturer() + " on " + portToUse.portName())
        else:
            qCritical("Serial Port error: " + self.serial.errorString())
            qDebug("Open error")


if __name__ == '__main__':
    # Replace stdout with logging to file at INFO level
    sys.stdout = MyLogger(logger, logging.INFO)
    # Replace stderr with logging to file at ERROR level
    sys.stderr = MyLogger(logger, logging.ERROR)
    app = QCoreApplication(sys.argv)
    o = SerialPortManager()
    o.openSerialPort()
    sys.exit(app.exec_())
