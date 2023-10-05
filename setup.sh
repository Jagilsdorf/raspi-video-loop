#!/bin/bash

# Update and install required packages
sudo apt-get update
sudo apt-get install -y git vlc xterm unclutter python3-pil.imagetk

#Auto-Hide mouse
#echo "unclutter -idle 0.1 -root &" >> ~/.bashrc

# Clone the repository into the user's home directory
if [ -d "~/raspi-video-loop" ]; then
    sudo rm -rf ~/raspi-video-loop
fi
git clone https://github.com/jagilsdorf/raspi-video-loop.git ~/raspi-video-loop

# Set permissions to execute the python scripts
chmod +x ~/raspi-video-loop/*.py

# Check if autostart directory exists, if not create it
if [ ! -d "~/.config/autostart" ]; then
    mkdir -p ~/.config/autostart
fi

# Create autostart entry for the main script
echo "[Desktop Entry]
Type=Application
Exec=/usr/bin/python3 $HOME/raspi-video-loop/main.py
Hidden=false
X-GNOME-Autostart-enabled=true
Name=Custom Script" > $HOME/.config/autostart/custom_script.desktop

# Auto-hide the LXPanel (taskbar)
sed -i 's/autohide=0/autohide=1/' ~/.config/lxpanel/LXDE-pi/panels/panel

# Hide Wastebasket and External Disks icons from the desktop
sed -i 's/show_trash=1/show_trash=0/' ~/.config/pcmanfm/LXDE-pi/desktop-items-0.conf
sed -i 's/show_mounts=1/show_mounts=0/' ~/.config/pcmanfm/LXDE-pi/desktop-items-0.conf

#Security: Block Wi-Fi and Bluetooth modules
echo "blacklist brcmfmac" | sudo tee -a /etc/modprobe.d/raspi-blacklist.conf
echo "blacklist brcmutil" | sudo tee -a /etc/modprobe.d/raspi-blacklist.conf
echo "blacklist btbcm" | sudo tee -a /etc/modprobe.d/raspi-blacklist.conf
echo "blacklist hci_uart" | sudo tee -a /etc/modprobe.d/raspi-blacklist.conf

# Reboot the Raspberry Pi
reboot