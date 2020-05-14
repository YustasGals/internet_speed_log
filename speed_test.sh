#!/bin/bash 
# ~/Speed/speed.sh

sleep 30s

while [ 1 = 1 ]
do

date | tee -a ~/Speed/logfile.txt
#~/Speed/speedtest-cli-master/speedtest.py --simple | tee -a ~/Speed/logfile.txt
ping ya.ru -c 3 | tee -a ~/Speed/logfile.txt
ping rtc.ru -c 3 | tee -a ~/Speed/logfile.txt
ping gmail.com -c 3 | tee -a ~/Speed/logfile.txt
speedtest --csv >> st.csv
speedtest --csv --server 2753 >> st2.csv
sleep 5m #4h

done
