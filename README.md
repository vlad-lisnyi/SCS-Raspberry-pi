<p align="center">
  <h1 align="center"> SCS-Raspberry-pi Shield</h1>
  <h3 align="center">Without Gateway</h3>
  
  <div align="center">
    <a href="https://scsshield.altervista.org/">https://scsshield.altervista.org/</a>
  </div>
</p>

<br>

<p align="center">
  <img src="raspberry4.jpg" width="300" />
</p>

**Contacts**
* <code><a href="http://scsshields.altervista.org/contatti.html">Contatti</a></code>

**Characteristics**

* Raspberry completely isolated from the bus
* Simple configuration thanks to the web-app
* Possibility to carry out actuator tests thanks to the web-app
* Communication with the shield occurs simply via <code>MQTT</code>, with the user's ability to develop their own applications with any desired language by communicating via <code>MQTT Publish/Subscribe</code>


**Pins used**

* UART0 TX (8)
* UART0 RX (10)
* GPIO 12 (32)



**Prerequisites and installation preparation**


* I recommend this version of raspberry "2021-05-07-raspios-buster-armhf-full.zip"
scaricabile nel seguente <a href="https://drive.google.com/file/d/1n9x76HdiFXM_pIzgByjm45ASKpH6mBKp/view" target="_blank"> link </a>
* <code><a href="https://phoenixnap.com/kb/enable-ssh-raspberry-pi" target="_blank">Abilitare SSH</a></code>
* <code> <a href="https://spellfoundry.com/2016/05/29/configuring-gpio-serial-port-raspbian-jessie-including-pi-3-4/" target="_blank">Abilitare la Porta Seriale</a> <u><i>per chi usa la Raspberry pi 3 disabilitare il Bluetooth</i></u></code>
* <code> <a href="https://di-marco.net/blog/it/2020-04-18-tips-disabling_bluetooth_on_raspberry_pi/" target="_blank">Guida per disabilitare il Bluetooth</a></code>





**Installation**
* <code>sudo apt full-upgrade</code>
* <code>sudo apt-get update</code>
* Dal Terminale SSH, digitare <code>git clone https://github.com/salviador/SCS-Raspberry-pi.git</code>
* <code>cd SCS-Raspberry-pi/SCS/</code>
* <code>sudo chmod +x setup.sh</code>
* <code>sudo ./setup.sh</code>
* <code>sudo pip3 install gmqtt</code>
* <code>sudo pip3 install uvloop</code>
* <code>sudo reboot</code>
* <code>Dopo il riavvio http://raspberrypi.local</code>

**Configuration and Use**
* <code><a href="http://scsshields.altervista.org/">http://scsshields.altervista.org/</a></code>


