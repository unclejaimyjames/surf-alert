# INITIATE BOOT: https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/
sudo nano /etc/rc.local
add sudo python /home/pi/surf-alert/surf.py &


#clone surf-alert git
git clone git://github.com/unclejaimyjames/surf-alert.git

#update git
git pull git://github.com/unclejaimyjames/surf-alert.git

#navigate in to the directory
cd surf-alert

#run code
python surf.py


