cyan='\e[5;36m'
purple='\e[5;35m'
brown='\e[0;33m'
lightgray='\e[0;37m'
darkgray='\e[1;30m'
lightblue='\e[1;34m'
lightgreen='\e[5;32m'
lightcyan='\e[5;36m'
lightred='\e[1;31m'
lightpurple='\e[1;35m'
yellow='\e[5;33m'

sleep 0.5

python2 banner.py

echo -e $cyan "1.Port (8080)"
echo -e $purple "2.Port (4444)"
echo -e $lightgreen "3.Port (8000)"
echo -e $lightcyan "4.Port (3333)"
echo -e $yellow "5.Port (5000)"

read -p "Pilihmana : " bro

if [ $bro = 1 ] || [ $bro = 1 ]
then
python2 1.py
fi

if [ $bro = 2 ] || [ $bro = 2 ]
then
python2 2.py
fi

if [ $bro = 3 ] || [ $bro = 3 ]
then
python2 3.py
fi

if [ $bro = 4 ] || [ $bro = 4 ]
then
python2 4.py
fi

if [ $bro = 5 ] || [ $bro = 5 ]
then
python2 5.py
fi
