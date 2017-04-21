Taller de Raspberry
=================


## Tabla de contenidos

1. [Introducción al Raspberry Pi](Introduction)
2. [Manejo de los GPIO's](GPIO)
3. [Web I](server)
4. [Web II](client)
5. [Bluetooth](bluetooth)



Introducción al Raspberry Pi
===========================

![](img/intro/anio.jpg)

##	¿Qué es un Raspberry pi?

1. Es un ordenador de placa reducida de bajo coste.
2. Nació para estimular la enseñanza de ciencias de la computación en las escuelas del Reino Unido( plataforma educativa).
3. Actualmente es una plataforma de desarrollo.

![](img/intro/proyectos.jpg)

#### Recursos

- SoC: Broadcom BCM2835 (CPU + GPU + DSP + SDRAM + puerto USB)
- CPU: ARM 1176JZF-S a 700 MHz (familia ARM11)
- Juego de instrucciones: RISC de 32 bits
- GPU: Broadcom VideoCore IV, OpenGL ES 2.0, MPEG-2 y VC-1 (con licencia), 1080p30 H.264/MPEG-4 AVC
- Memoria (SDRAM): 512 MiB (compartidos con la GPU)
- Puertos USB 2.0: 4
- Entradas de video: Conector MIPI CSI que permite instalar un
- módulo de cámara desarrollado por la RPF
- Salidas de video: Conector RCA (PAL y NTSC), HDMI (rev1.3 y 1.4), Interfaz DSI para panel LCD
- Salidas de audio: Conector de 3.5 mm, HDMI
- Almacenamiento integrado: MicroSD
- Conectividad de red: 10/100 Ethernet (RJ-45) via hub USB
- Periféricos de bajo nivel: GPIO, SPI, I2C, UART
- Consumo energético: 600 mA, (3.0 W)
- Fuente de alimentación: 5V v´ıa Micro USB o GPIO header
- Dimensiones: 85.60mm × 53.98mm
- Sistemas operativos soportados:GNU/Linux: Debian (Raspbian), Fedora (Pidora), Arch Linux (Arch Linux ARM), Slackware Linux. RISC OS

#### Modelos

##### RPI 1 Modelo A
<img  src="img/intro/ModelA.png" width="500" alt=""/>

##### RPI 1 Modelo A+
<img  src="img/intro/ModelA+.png" width="500" alt=""/>

##### RPI 1 Modelo B
<img  src="img/intro/ModelB.png" width="500" alt=""/>

##### RPI 1 Modelo B+
<img  src="img/intro/ModelB+.jpg" width="500" alt=""/>

##### RPI 2 Modelo B
<img  src="img/intro/Model2B.jpeg" width="500" alt=""/>

##### RPI ZERO
<img  src="img/intro/modelzero.jpg" width="500">

##### RPI 3 Modelo B
<img  src="img/intro/model3.jpg" width="500" alt=""/>


|               |RPI 1 Model A		|RPI 1 Model A+	 	|RPI 1 Model B		|RPI 1 Model B+	|RPI Model 2 Model B| RPI Zero| RPI 3 Model B|
|---------------|:-------------:|:-------------:|:-------------:|:-----------:|:-------------:|:--------------:|:-------:|
|SoC|	Broadcom BCM2835| Broadcom BCM2835|Broadcom BCM2835|Broadcom BCM2835|Broadcom BCM2836| Broadcom BCM2835|BCM287 |
|CPU| ARMv6 700 MHz| ARM11 ARMv6 700 MHz| ARM11 ARMv6 700 MHz| ARM11 ARMv6 700 MHz| ARM11 ARMv7 ARM Cortex-A7 4 núcleos @ 900 MHz| ARM11 ARMv6 Dual Core 1 GHz| ARM cortex A53 1.2GHz 64bit 4 núcleos|
|GPU|Broadcom VideoCore IV 250 MHz. OpenGL ES 2.0 |Broadcom VideoCore IV 250 MHz. OpenGL ES 2.0| Broadcom VideoCore IV 250 MHz. OpenGL ES 2.0| Broadcom VideoCore IV 250 MHz. OpenGL ES 2.0	| Broadcom VideoCore IV 250 MHz. OpenGL ES 2.0| Broadcom VideoCore IV 250 MHz. OpenGL ES 2.0|Broadcom VideoCore IV 250 MHz. OpenGL ES 2.0 |
|RAM| 256 MB LPDDR SDRAM 400 MHz| 256 MB LPDDR SDRAM 400 MHz| 512 MB LPDDR SDRAM 400 MHz| 512 MB LPDDR SDRAM 400 MHz| 1 GB LPDDR2 SDRAM 450 MHz| 512 MB LPDDR SDRAM 400 MHz| 1 GB LPDDR2 SDRAM 450 MHz|
|USB| 1 USB 2.0|1 USB 2.0|2 USB 2.0|4 USB 2.0|4 USB 2.0| 1 microUSB 2.0| 4 USB 2.0|
|Salidas de vídeo|HDMI 1.4 @ 1920x1200 píxeles|HDMI 1.4 @ 1920x1200 píxeles|HDMI 1.4 @ 1920x1200 píxeles|HDMI 1.4 @ 1920x1200 píxeles|HDMI 1.4 @ 1920x1200 píxeles|mini-HDMI 1.4 @ 1920x1200 píxeles | HDMI 1.4 @ 1920x1200 píxeles |
|Almacenamiento|SD/MMC|microSD|SD/MMC|microSD|microSD|microSD| microSD|
|Ethernet|No|No|Sí, 10/100 Mbps|Sí, 10/100 Mbps|Sí, 10/100 Mbps| No | 10/100 Mbit/s Ethernet 802.11n wireless Bluetooth 4.1 |
|Tamaño	|85,60mmx56,5 mm|65mmx56,5 mm|85,60mmx56,5 mm|85,60mmx56,5 mm|85,60mmx56,5 mm|65mmx30mm|85,60mmx56,5 mm|
|Peso   |45 g.|23 g.|45 g.|45 g.|45 g.|9 g| 45g|
|Precio	|25 dólares|20 dólares|35 dólares|35 dólares|35 dólares|5 dólares| 35 dólares|


## Relación con otros ordenadores

## Herramientas

### Windows

- Win32DiskImager [(Descargar)](http://sourceforge.net/projects/win32diskimager/files/latest/download
)
- Putty [(Descargar)](https://the.earth.li/~sgtatham/putty/latest/x86/putty-0.67-installer.msi)
- WinSCP [(Descargar)](https://winscp.net/eng/download.php#download2)
- Advanced IP Scanner [(Descargar)](http://www.filehippo.com/download_advanced_ip_scanner/?utm_source=FT&utm_medium=Redirect&utm_campaign=AIS)
- SDFormater [(Descargar)](https://www.sdcard.org/downloads/formatter_4/eula_windows/SDFormatterv4.zip)

### Linux

```console
$ sudo dd bs=4M if=/path/of/raspbian-image.img of=/dev/mmcblk0
$ sudo apt-get -y install nmap
$ sudo nmap -sn ip.of.red.0/24
$ ssh pi@your.rpi.ip.address
$ scp your_archivo pi@your.rpi.ip.address:"/home/pi"
```

## Materiales

- MicroSD
- Cable ethernet
- Fuente de 5V 2amp
- Raspberry pi
- PC
- Software Putty
- Cable HDMI(opcional)
- Teclado(opcional)
- Mouse(opcional)
- Usb Wifi(opcional)

### Instalacion de SO

1. SO Raspbian, descargarlo de la página oficial de Raspberry Pi desde [aquí](https://www.raspberrypi.org/downloads/raspbian/)
2. una memoría microSD de al menos 4Gb (recomiendo que sea de clase 10)
3. software para grabar el SO en la memoria microSD, en este caso optaremos por Win32DiskImager

El usuario por defecto es **pi** y la contraseña **raspberry**

### Primera conexión:

Formaremos una red local entre el Rpi y la PC para poder acceder a esta sin necesidad de una pantalla y teclado ni demás conectores.Los materiales que se necesitaremos son:

Despues de grabar la memoría microSD con Raspbian, lo insertamos en la pc y vamos a editar el archivo cmdline.txt:

```
 pi@raspberrypi:~ $ nano boot/cmdline.txt
 dwc_otg.lpm_enable=0 console=ttyAMA0,115200 <...> rootwait ip=your.rpi.ip.address
```

Luego insertamos la memoria en el raspberry pi, y alimentamos la raspberry pi, en paralelo cambiamos la configuración de ethernet en nuestra PC con la siguiente configuración:

```
ip address: your.rpi.ip.another_address
netmask: 255.255.255.0
gateway: your.rpi.ip.address
```

Y conectamos la Rpi con la PC mediante el cable ethernet, y abrimos el programa Putty y colocaremos la ip del raspberry pi, aceptamos la llave SSH y colocamos el usuario:pi y la contraseña:raspberry cuando nos pidan. Luego de esto configuramos una mejor conexión ya sea cableada o inalámbrica.

Desde [https://www.raspberrypi.org/documentation/remote-access/ssh/](https://www.raspberrypi.org/documentation/remote-access/ssh/) :

> As of the November 2016 release, Raspbian has the SSH server disabled by default.
>  You will have to enable it manually. This is done using raspi-config: 
> Enter sudo raspi-config in the terminal, first select Interfacing options, then navigate to  ssh, press
> Enter and select Enable or disable ssh server.
> For headless setup, SSH can be enabled by placing a file named 'ssh', without any extension, onto the boot partition of the SD card.

##### RASPBIAN JESSIE LITE

Segun un aviso de la actualización, se removio el acceso ssh por defecto por lo que no se podrá seguir el manual para versiones posteriores a Noviembre del 2016.

En los foros nos muestra una solución para la version Lite de raspbian. Primero debemos ingresar al archivo cmdline.txt añadir lo siguiente:
```
ip=192.168.1.200::192.168.1.1:255.255.255.0:rpi:eth0:off
```
Esta estructuta tiene la forma: 
```
ip=<client-ip>:<server-ip>:<gw-ip>:<netmask>:<hostname>:<device>:<autoconf>
```

Despues de esto para habilitar la conexión ssh solo es necesario crear un archivo vacio  llamado ***ssh***.

En el caso de nuestra computadora debemos configurarlo como:

```
$ ip address: 192.168.1.xxx
$ netmask: 255.255.255.0
$ gateway: 192.168.1.1
```

**Nota**: La creación del archivo ***ssh*** o ***ssh.txt*** habilta el protócolo ssh en 
***RASPBIAN JESSIE WITH PIXEL*** pero la configuración de ip estática genera que el boot no se complete.

#### Cableada(IP Dinámica)

No editamos nada pero necesitaremos un software que escanee la red como Advanced IP Scanner donde buscaremos la red que tenga como fabricante a Raspberry Pi Foundation.

#### Cableada(IP Estática)

Editamos el archivo interfaces:

```
pi@raspberrypi:~ $ sudo nano /etc/networks/interfaces
```

y cambiamos a:

```
 auto eth0
 #iface eth0 inet dhcp
 iface eth0 inet static
 address 192.168.1.11
 netmask 255.255.255.0
 gateway 192.168.1.1 #dirección ip del router
```

#### Inalámbrica

 Editamos el archivo wpa_supplicant.conf:&nbsp:

```
pi@raspberrypi:~ $ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```
y cambiamos a:

```
network={
    ssid="Your ssid"
    psk="your wifi password"
}
```

En ambos casos reiniciar la Rpi y conectarse ahora por el nuevo IP a través del cliente SSH, en nuestro caso Putty(en el caso de una red inalámbrica averigue su IP con Advanced IP Scanner )

Si la Raspberry Pi tiene acceso a internet comprobamos si esta bien configurado con el siguiente comando:
```
pi@raspberrypi:~ $ ping -c 3 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=45 time=173 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=45 time=180 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=45 time=172 ms
--- 8.8.8.8 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2002ms
rtt min/avg/max/mdev = 172.677/175.469/180.461/3.554 ms
```

Y sino tendremos que configurar el DNS, para ello editamos el archivo /etc/resolv.conf

```
pi@raspberrypi:~ $ sudo nano /etc/resolv.conf
nameserver 8.8.8.8
nameserver 8.8.4.4
```

###	Comandos en GNU-Linux

Algunos de los miles de comandos de linux!!!

| Comando 	|Función 			| Uso 								|
|-----------|-------------------|-----------------------------------
|man 		|manual  			| ``$ man man``						|
|ls 		|listing 			| ``$ ls /home/pi``					|
|cd 		|change directory	| ``$ cd ..``						|
|mv 		|move 				|``$ mv carpeta1 carpeta2``			|
|rm 		|remove 			|``$ rm archivo.txt``				|
|rmdir 		|remove directory 	|``$ rmdir carpeta``				|
|mkdir 		|make directory 	|``$ mkdir carpeta``				|
|cp 		|copy 				|``$ cp archivo1.txt archivo2.txt``	|
|find 		|find 				|``$ find archivo.txt``				|
|locate 	|locate 			|``$ locate archivo.txt``			|

##	Uso del editor Nano
```sh
$ nano name_of_file
```

## raspi-config

La herramienta Raspi-config le ayuda a configurar su Raspberry Pi; varios ajustes se pueden cambiar con esta herramienta sin tener que conocer los comandos correctos para su uso.

```console
$ sudo raspi-config
```

<img  src="img/raspi-config.png" width="400"/>

## Escritorio Remoto: VNC

```console
$ sudo apt-get install tightvncserver
$ vncserver :1 -geometry 1280x800 -depth 16 -pixelformat rgb565
```

Para windows descargar desde [aquí](https://www.realvnc.com/download/binary/1795/)

Para linux instalar:
```console
pi@raspberrypi:~ $ sudo apt-get -y install 
```

ingresar con **your.rpi.ip.address:1**


## Editor remoto: Sublime

Usar la terminal para editar no es amigable, por ello recurrimos a esta gran utilidad.

### Instalar sublime

1. Instalar sublime desde [aquí](https://download.sublimetext.com/Sublime%20Text%202.0.2a%20x64%20Setup.exe)
2. Instalar Package Control
	Ejecutar View/Console y pegar
```perl
import urllib2,os,hashlib; h = '2915d1851351e5ee549c20394736b442' + '8bc59f460fa1548d1514676163dafc88'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); os.makedirs( ipp ) if not os.path.exists(ipp) else None; urllib2.install_opener( urllib2.build_opener( urllib2.ProxyHandler()) ); by = urllib2.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); open( os.path.join( ipp, pf), 'wb' ).write(by) if dh == h else None; print('Error validating download (got %s instead of %s), please try manual install' % (dh, h) if dh != h else 'Please restart Sublime Text to finish installation')
```
3. Ejecutar ctrl-shift-p, escribir install y seleccionar rsub

### Instalar rmate

```bash
pi@raspberrypi:~ $ sudo wget -O /usr/local/bin/rsub https://raw.github.com/aurora/rmate/master/rmate
pi@raspberrypi:~ $ sudo chmod +x /usr/local/bin/rsub
```

### Configurar Putty

1. Ejecutar como administrador putty
2. Seleccionar Connection/SSH/tunnels
3. Colocar en **Source port**: 52698, en **Destination**:127.0.0.1:52698 y seleccionar **Remote**

### USO

```bash
pi@raspberrypi:~ $ rsub your_file
```

### Resumen

	pi@raspberrypi:~ $ sudo apt-get update
	pi@raspberrypi:~ $ sudo apt-get upgrade
	pi@raspberrypi:~ $ sudo apt-get install -y tree
	pi@raspberrypi:~ $ sudo apt-get install -y mlocate
	pi@raspberrypi:~ $ sudo updatedb