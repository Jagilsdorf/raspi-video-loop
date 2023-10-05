#!/bin/bash

# Update and install required packages
sudo apt-get update
sudo apt-get install -y git vlc xterm python3-pil.imagetk

# Clone the repository into the user's home directory
git clone https://github.com/jagilsdorf/raspi-video-loop.git ~/raspi-video-loop

# Set permissions to execute the python scripts
chmod +x ~/raspi-video-loop/main.py
chmod +x ~/raspi-video-loop/screensaver.py

# Check if autostart directory exists, if not create it
if [ ! -d "~/.config/autostart" ]; then
    mkdir -p ~/.config/autostart
fi

# Create autostart entry for the main script
echo "[Desktop Entry]
Type=Application
Exec=/usr/bin/python3 ~/raspi-video-loop/main.py
Hidden=false
X-GNOME-Autostart-enabled=true
Name=Custom Script" > ~/.config/autostart/custom_script.desktop

# Auto-hide the LXPanel (taskbar)
sed -i 's/autohide=0/autohide=1/' ~/.config/lxpanel/LXDE-pi/panels/panel

# Hide Wastebasket and External Disks icons from the desktop
sed -i 's/show_trash=1/show_trash=0/' ~/.config/pcmanfm/LXDE-pi/desktop-items-0.conf
sed -i 's/show_mounts=1/show_mounts=0/' ~/.config/pcmanfm/LXDE-pi/desktop-items-0.conf

# Reboot the Raspberry Pi
reboot
