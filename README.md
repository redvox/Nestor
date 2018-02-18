# Nestor
Dashboard with Rasberry Pi and ePaper display

# Hardware
- [Raspberry Pi 3 Model B](https://www.amazon.de/gp/product/B01CD5VC92/ref=oh_aui_detailpage_o06_s00?ie=UTF8&psc=1)
- SD Card with 8GB
- [Waveshare 7.5 Inch E-Paper Display - Amazon](https://www.amazon.de/gp/product/B075R4QY3L/ref=oh_aui_detailpage_o05_s00?ie=UTF8&psc=1)
- [Waveshare Wiki](https://www.waveshare.com/wiki/7.5inch_e-Paper_HAT?Amazon)

# Setup
## Setup OS
Download [Raspbian Stretch Lite](https://www.raspberrypi.org/downloads/raspbian/).

Use [Etcher](https://etcher.io/) to write the image to your SD card.

## Enable SSH
Because of security issues in the recent past, SSH is not enabled by default.

You can hook up a display and keyboard/mouse to enable ssh via the grapical userinterface, but the developers also added a nice little "headless" option. 

If you create a file named `ssh` on the boot partition, ssh will be enabled.

## Find your Raspberrys IP
Plug in your Raspberry. If you have a screen connected, tteh ip adress will be prompted. Should you have trouble find it, you can use `nmap` to scan your local network.

```bash
sudo apt-get install nmap
sudo nmap -sP 192.168.178.1/24
```

## Connect to your rasbperry
After you got your ip, its time to connect to your raspberry.

```bash
ssh pi@<ip-adress>
```

After the inital connectivity is assured, change the default password with `sudo passwd pi` on your pi.

After than use `ssh-copy-id` to make your raspberry accessible via ssh-key.

```bash
ssh-copy-id -i ~/.ssh/id_rsa pi@<ip-adress>
```

This way you do not have to type your password with every access, once your key is unlocked.

## [optional] remove graphical user interface
If you do not need a desktop environment, you can remove it.

```bash
sudo apt-get -y remove cups*
sudo apt-get -y remove gnome*
sudo apt-get -y remove x11-common*
sudo apt-get -y autoremove
```

## Install libraries
tbd