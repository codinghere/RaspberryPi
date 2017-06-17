import sys

import xlwt
from PyQt5.QtCore import QSettings, QModelIndex, Qt
from PyQt5.QtSql import QSqlQueryModel, QSqlDatabase
from PyQt5.QtWidgets import QTableView, QApplication, QMainWindow, QMessageBox, qApp, QMenuBar, QMenu, QAction, \
    QFileDialog, QWidget, QVBoxLayout, QStatusBar


def createConnection():
    db = QSqlDatabase.addDatabase('QMYSQL')
    db.setHostName("localhost")
    db.setDatabaseName('ard2pi')
    db.setUserName("root")
    db.setPassword("raspberry")

    if not db.open():
        QMessageBox.critical(None, qApp.tr("Cannot open database"),
                             qApp.tr("Unable to establish a database connection.\n"
                                     "This example needs SQLite support. Please read "
                                     "the Qt SQL driver documentation for information "
                                     "how to build it.\n\n"
                                     "Click Cancel to exit."),
                             QMessageBox.Cancel)



class Widget(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)

        self.centralwidget = QWidget(self)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.tableView = QTableView(self.centralwidget)
        self.verticalLayout.addWidget(self.tableView)
        self.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(self)
        self.menuFile = QMenu(self.menubar)
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.actionExport = QAction(self)
        self.actionExport.setText("Exportar")
        self.actionExport.triggered.connect(self.export)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.setTitle("Archivo")
        self.menubar.addAction(self.menuFile.menuAction())

        self.model = QSqlQueryModel()
        self.tableView.setModel(self.model)
        self.model.setQuery("select * from Monitoreo")

    def readSettings(self):
        pass

    def saveSettings(self):
        settings = QSettings()
        settings.beginGroup("db")
        settings.setValue("hostname", "localhost")
        settings.setValue("databaseName", "ard2pi")
        settings.setValue("username", "root")
        settings.setValue("password", "qhipa")
        settings.endGroup()

    def export(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Guardar Datos", "", "xls (*.xls)")

        if fileName != "":
            workbook = xlwt.Workbook()
            sheet = workbook.add_sheet('test')

            for col in range(self.model.columnCount()):
                sheet.write(0, col, self.model.headerData(col, Qt.Horizontal))

            for row in range(self.model.rowCount()):
                for col in range(self.model.columnCount()):
                    index = self.model.index(row, col, QModelIndex())
                    sheet.write(row+1, col, self.model.data(index))

            workbook.save(fileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setOrganizationName("eyllanesc")
    app.setOrganizationDomain("https://github.com/eyllanesc")
    app.setApplicationName("ard2pi")
    createConnection()
    w = Widget()
    w.show()
    sys.exit(app.exec_())
