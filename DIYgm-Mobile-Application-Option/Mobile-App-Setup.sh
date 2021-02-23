# Set up script for the mobile application V2.0 - Andrew Kent
#install bluetooth-dev
sudo apt-get install libbluetooth-dev

#add --compat to /etc/systemd/system/dbus-org.bluez.service
sudo sed -i 's_ExecStart=/usr/lib/bluetooth/bluetoothd_ExecStart=/usr/lib/bluetooth/bluetoothd --compat_g' /etc/systemd/system/dbus-org.bluez.service

#restart all bluetooth fucntionality
sudo systemctl daemon-reload
sudo systemctl restart bluetooth
sudo chmod 755 /var/run/sdp

#move all necessary files to root
sudo cp -R /home/pi/DIYgm/DIYgm-Mobile-Application-Option/* /


#setup arm bluetooth node extension
sudo tar -xf /node-v4.3.1-linux-armv6l.tar.gz
sudo service bluetooth stop
sudo cp -R /node-v4.3.1-linux-armv6l/* /usr/local
sudo service bluetooth start

#mark all executables as executable
sudo chmod +x /startup.sh
sudo chmod +x /discoverable.sh
sudo chmod +x auto-launch.sh

#set up crontab V2.0
sudo crontab -l | { cat; echo "@reboot /./auto-launch.sh"; } | sudo crontab -

#set up crontab V1.0
#write out current crontab
#sudo crontab -l > /tempcron
#echo new cron into cron file
#echo "@reboot /./auto-launch.sh" >> /tempcron
#install new cron file
#sudo crontab /tempcron
#sudo rm /tempcron