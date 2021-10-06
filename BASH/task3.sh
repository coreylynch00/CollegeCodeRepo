#### TASK 3 ####
# Corey Lynch - SD2-A 

#!/bin/bash

#Check if script is ran with root privilages

if [ $EUID -ne 0 ]
then
	echo "This script requires root privileges to execute"
	echo "User: sudo $0 ...."
	exit 1
fi

#Check if username is successfully passed as an argument
if [ $# -ne 1 ]
then 
	echo "Please provide the required arguments"
	echo "User: sudo $0 username"
	exit 2
fi

#Successfully passes required checks
echo "Successfully passed checks!"

#Create new user
useradd -m $1

#Output user details
cat /etc/passwd

#Wait 10 seconds
sleep 10

#Delete account
echo "Deleting account"
userdel -rf $1

#Output user details
cat /etc/passwd


