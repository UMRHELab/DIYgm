#!/bin/bash
echo "---------------- Update ----------------\n"

# Make sure the system is up to date
apt-get update

echo "---------------- Installing Dependencies ----------------\n"
# Install all dependencies
apt-get -y install python-bluez
pip3 install pybluez

# Set up script for the mobile application V2.0 - Andrew Kent
#install bluetooth-dev
apt-get -y install libbluetooth-dev

echo "---------------- Modifying bluetooth for compatibility ----------------\n"
#add --compat to /etc/systemd/system/dbus-org.bluez.service
sed -i 's_ExecStart=/usr/lib/bluetooth/bluetoothd_ExecStart=/usr/lib/bluetooth/bluetoothd --compat_g' /etc/systemd/system/dbus-org.bluez.service

echo "---------------- Restarting Bluetooth ----------------\n"
#restart all bluetooth fucntionality
systemctl daemon-reload
systemctl restart bluetooth
chmod 755 /var/run/sdp

echo "---------------- Copying Necessary Files to root ----------------\n"
#move all necessary files to root
cp -R /home/pi/DIYgm/mobile-app/* /

echo "---------------- Extracting Node.js ----------------\n"
#setup arm bluetooth node extension
tar -xf /node-v4.3.1-linux-armv6l.tar.gz
service bluetooth stop
cp -R /node-v4.3.1-linux-armv6l/* /usr/local
service bluetooth start

echo "---------------- Adding Executable Status to Program ----------------\n"
#mark all executables as executable
chmod +x /startup.sh
chmod +x /discoverable.sh
chmod +x /auto-launch.sh

echo "---------------- Adding Cronjob ----------------\n"
crontab -l | crontab -

#set up crontab V2.0
crontab -l | { cat; echo "@reboot /./auto-launch.sh"; } | crontab -

#set up crontab V1.0
#write out current crontab
#sudo crontab -l > /tempcron
#echo new cron into cron file
#echo "@reboot /./auto-launch.sh" >> /tempcron
#install new cron file
#sudo crontab /tempcron
#sudo rm /tempcron