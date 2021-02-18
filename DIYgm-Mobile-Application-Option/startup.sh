if [ -f transfer.txt ]
then
	sudo rm -f transfer.txt
	sudo echo transfer.txt deleted
fi

sudo ./discoverable.sh &
sudo node main.js &
sudo python3 diygm.py &
