# Do-It-Yourself Geiger-Muller Device
### The Basic Code For A DIYgm Raspberry Pi Device

This is the public access version of the University of Michigan Radiological Health Engineering Laboratory Do-It-Yourself Geiger-Muller Device code.
This code is built to run on a Raspberry Pi Zero W with bluetooth enabled using the UMRHE DIYgm Board and Raspian.


## Usage

This software requires [python-bluez](https://packages.debian.org/buster/python-bluez) for Buster and pip3 [pybluez](https://github.com/pybluez/pybluez).
You may install these on the Raspberry Pi using:  
`sudo apt-get install python-bluez`  
`sudo pip3 install pybluez`  

## Running on Raspberry PI  
#### If you plan to use this only on the Raspberry Pi, do this:  

The final step after setting up bluetooth is to type:  
`cp -R DIYgm-Raspberry-Pi-Only/* .`

#### **You should be all set at this point**

## Running With A Mobile Application
There exists an optional mobile application for use with the DIYgm software for IOS or Android that links through bluetooth.


Raspberry Pi Softwarefor Bluetooth connection to Mobile Applications

1. Plug in the ports on the Raspberry Pi to turn it on and connect it to a monitor, mouse, and keyboard.

2. Make sure you are connected to the Internet. Use the Wifi symbol on the top right of the screen to do this.
 Some Wifi may require you to open a browser to connect to it.

3. Open a Terminal by clicking the “>_” symbol on the top toolbar.

4. First we need to install pybluez, which will let the Pi connect to the Android app via Bluetooth. Type  
`sudo apt-get install libbluetooth-dev` into the Terminal and press Enter. 
When installation is finished, type  
`sudo python3 -m pip install pybluez` into the Terminal and press Enter. 
Press the Y key when prompted in order to install.

5. We now need to edit the newly installed software to make it compatible with the Pi. After installation,  
type `sudo nano /etc/systemd/system/dbus-org.bluez.service` and hit Enter. You should now be editing a text file.

6. Use the arrow keys to go to the line `ExecStart=/usr/lib/bluetooth/bluetoothd`. Go to the end of the line and add `--compat` to the end. 
It should now say `ExecStart=/usr/lib/bluetooth/bluetoothd --compat`. Then, press Ctrl+X, Y, and enter. This should end the editing.

7. We then need to reload some parts of the Pi:  
	a. Type `sudo systemctl daemon-reload`     and press Enter.  
	b. Type `sudo systemctl restart bluetooth` and press Enter.  
	c. Type `sudo chmod 755 /var/run/sdp`      and press Enter.  

8. To get the DIYgm-Mobile-Application files from inside the folder, type in:  
`cp -R DIYgm-Mobile-Application-Option/* .` (including the period)

9. We need to install node.js, which will let the Pi connect to the mobile apps via Bluetooth. To do this, right click on the 
`node-v4.3.1-linux-armv6l.tar.gz` file in the home folder and click “Extract Here.” 
After the extraction, open a Terminal byclicking the “>_” symbol on the top toolbar. 
Type `sudo service bluetooth stop` to turn off the Pi’s Bluetooth for now.

10. Node.js has already been downloaded as one of the DIYgm-iOS files, so we now just have to move it to a system folder. 
Type `cd node-v4.3.1-linux-armv6l` and press Enter (Tip: press Tab to autocomplete the filename). Type 
`sudo cp -R * /usr/local` and press Enter.

11. Restart the Pi’s Bluetooth by typing `sudo service bluetooth start` and pressing Enter


You may change the name of your Raspberry Pi so you can recognize it in the mobile app. 
Click on the folder icon in the top toolbar to open the File Manager. Double click on the name.txt file. 
This should open a text editor. Replace “TestName” with your preferred name for the Pi.

#### IOS:
For IOS you must install the test flight application **prior** to downloading the DIYgm app
You can do this by either searching for the _Test Flight_ application in the app store, or clicking the link below on your mobile device and choosing step one.
Once you have Test Flight downloaded, go to the [**DIYgm on IOS Download Page**](https://testflight.apple.com/join/hFALODXI).

#### Android:
