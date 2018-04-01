# Nestor
Dashboard with Rasberry Pi and ePaper display

# Hardware
- [Raspberry Pi 3 Model B](https://www.amazon.de/gp/product/B01CD5VC92/ref=oh_aui_detailpage_o06_s00?ie=UTF8&psc=1)
- SD Card with 8GB
- [Waveshare 7.5 Inch E-Paper Display - Amazon](https://www.amazon.de/gp/product/B075R4QY3L/ref=oh_aui_detailpage_o05_s00?ie=UTF8&psc=1)
- [Waveshare Wiki](https://www.waveshare.com/wiki/7.5inch_e-Paper_HAT?Amazon)

## e-Paper Driver HAT Settings
If you using the Driver HAT, like i do. Make sure the switches on the Hat are set correctly.

*Display Config* has to be set accordingly to the display you are using. In case of the 7.5 inch it would be *B*.

The *Interface Config* must be set to *0*.

Waveshare has a [Video](https://www.youtube.com/watch?v=f4yoYbSWctI) explaining the different settings. 

# Setup
## Install OS
Download [Raspbian Stretch Lite](https://www.raspberrypi.org/downloads/raspbian/).

Use [Etcher](https://etcher.io/) to write the image to your SD card.

## Enable SSH
Because of security issues in the recent past, SSH is not enabled by default.

You can hook up a display and keyboard/mouse to enable ssh via the grapical userinterface, but the developers also added a nice little "headless" option. 

If you create a file named `ssh` on the boot partition, ssh will be enabled.

## Find your raspberry's IP
Plug in your Raspberry. If you have a screen connected, the ip address will be prompted. 

Should you have trouble find it or you do not have a screen attached, you can use `nmap` to scan your local network.

```bash
sudo apt install -y nmap
sudo nmap -sP 192.168.178.1/24
```

## Connect to your raspberry
After you got your ip, its time to connect to your raspberry.

```bash
ssh pi@192.168.178.5
```

After the initial connectivity is assured, change the default password with `sudo passwd pi` on your pi.

After than use `ssh-copy-id` to make your raspberry accessible via ssh-key.

```bash
ssh-copy-id -i ~/.ssh/id_rsa pi@192.168.178.5
```

This way you do not have to type your password with every access, once your key is unlocked.

## [optional] Remove graphical user interface
If you do not need a desktop environment, you can remove it.

```bash
sudo apt-get remove cups*
sudo apt-get remove gnome*
sudo apt-get remove x11-common*
sudo apt-get autoremove
```

## Install python
Install python 3 on your raspberry via:
```bash
sudo apt install -y python3
sudo apt install -y python3-dev
sudo apt install -y python3-pip
# PILLOW DEPENDENCIES
sudo apt install -y libopenjp2-7-dev
sudo apt install -y libtiff4
sudo apt install -y libtiff5
```

## Third party libraries
On the Waveshare Wiki there is a section about libraries you need to install.
I obtained them with the [Example Code](https://www.waveshare.com/wiki/File:7.5inch-e-paper-hat-code.7z), but ended up not needing them. 

If the project does not work for you, you may want to look at Waveshares [Guide to install libraries](https://www.waveshare.com/wiki/Pioneer600#Libraries_Installation_for_RPi).

## Enable SPI
To allow your adapter to communicate with your display, you have to enable SPI. 
```bash
sudo raspi-config
```
Go to *Interface Options*, then *SPI*, then *enable*

# Setup Google Calender
## Register Application and activate API
Go and look at Googles [Quickstart Tutorial](https://developers.google.com/calendar/quickstart/python)

Make sure to register your application and download *client_id.json* and put it under *config/* directory of this project.

## Get Credentials
To get credentials from google, run the provided script. Make sure you have a browser open with the google account you want to access.
```bash
./get_google_credentials.sh
```
The credentials file will be saved under *config/google_credentials.json*

