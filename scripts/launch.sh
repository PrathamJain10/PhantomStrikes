#!/bin/bash

# https://github.com/your-github-username/PhantomStrikes

if [[ $(uname -o) == *'Android'* ]];then
	PHANTOMSTRIKES_ROOT="/data/data/com.termux/files/usr/opt/phantomstrikes"
else
	export PHANTOMSTRIKES_ROOT="/opt/phantomstrikes"
fi

if [[ $1 == '-h' || $1 == 'help' ]]; then
	echo "To run PhantomStrikes type \`phantomstrikes\` in your cmd"
	echo
	echo "Help:"
	echo " -h | help : Print this menu & Exit"
	echo " -c | auth : View Saved Credentials"
	echo " -i | ip   : View Saved Victim IP"
	echo
elif [[ $1 == '-c' || $1 == 'auth' ]]; then
	cat $PHANTOMSTRIKES_ROOT/data/auth/usernames.dat 2> /dev/null || { 
		echo "No Credentials Found !"
		exit 1
	}
elif [[ $1 == '-i' || $1 == 'ip' ]]; then
	cat $PHANTOMSTRIKES_ROOT/data/auth/ip.txt 2> /dev/null || {
		echo "No Saved IP Found !"
		exit 1
	}
else
	cd $PHANTOMSTRIKES_ROOT
	bash ./Phantom.sh
fi
