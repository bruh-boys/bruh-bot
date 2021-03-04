#!/bin/bash
clear
python3 twitch.py &
#python3 spy.py &
node reddit.js &
while :
do
python3 main.py 
done
