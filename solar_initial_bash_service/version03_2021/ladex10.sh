#!/bin/bash

gpio -g mode 17 out
gpio -g write 17 1
gpio -g mode 18 out
gpio -g write 18 1
gpio -g mode 22 out
gpio -g write 22 1
gpio -g mode 23 out
gpio -g write 23 1
gpio -g mode 24 in

sleep 2

while true;
do
solarstrom=$(gpio -g read 24)
if (( $solarstrom == 1 ))
then 
sleep 2
 gpio -g write 22 1
 gpio -g write 23 1
sleep 2
 gpio -g write 17 0
 gpio -g write 18 0
else
sleep 2
 gpio -g write 17 1
 gpio -g write 18 1
sleep 2 
 gpio -g write 22 0
 gpio -g write 23 0
sleep 2
fi;
done
