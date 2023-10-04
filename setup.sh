#!/bin/bash

# Update and install required packages
sudo apt-get update
sudo apt-get install -y git vlc xterm python3-pil.imagetk

# Clone the repository
git clone https://github.com/jagilsdorf/raspi-video-loop.git

mkdir /etc/raspi-video-loop/

# Move the assets to the user's new directory
mv raspi-video-loop/main.py /etc/raspi-video-loop/
mv raspi-video-loop/screensaver.py /etc/raspi-video-loop/
mv raspi-video-loop/logo.png /etc/raspi-video-loop/
mv raspi-video-loop/file.mp4 /etc/raspi-video-loop/

# Set permissions to execute the python scripts
chmod +x /etc/raspi-video-loop/main.py
chmod +x /etc/raspi-video-loop/screensaver.py

# Check if autostart directory exists, if not create it
if [ ! -d "~/.config/autostart" ]; then
    mkdir -p ~/.config/autostart
fi

# Create autostart entry for the main script
echo "[Desktop Entry]
Type=Application
Exec=/usr/bin/python3 /etc/raspi-video-loop/main.py
Hidden=false
X-GNOME-Autostart-enabled=true
Name=Custom Script" > ~/.config/autostart/custom_script.desktop
reboot
