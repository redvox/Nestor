# Nestor
Dashboard with Rasberry Pi and ePaper display

# Hardware
[Waveshare 7.5 Inch E-Paper Display - Amazon](https://www.amazon.de/gp/product/B075R4QY3L/ref=oh_aui_detailpage_o05_s00?ie=UTF8&psc=1)
[Waveshare Wiki](https://www.waveshare.com/wiki/7.5inch_e-Paper_HAT?Amazon)

# Setup
## Find your Raspberry
Plug in your Raspberry. If you have trouble find the right ip adress, you can use `nmap` to scan your local network.

```bash
sudo apt-get install nmap
sudo nmap -sP 192.168.178.1/24
```
## Connect to your rasbperry
After you got your ip, its time to connect to your raspberry.

```bash
ssh pi@<ip-adress>
```

After the inital connectify is assured, use `ssh-copy-id` to make your raspberry accessible via ssh-key.

```bash
ssh-copy-id -i ~/.ssh/id_rsa pi@<ip-adress>
```

This way you do not have to type your password with every access, once your key is unlocked.

