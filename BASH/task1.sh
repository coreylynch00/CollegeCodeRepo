#### TASK 1 ####
# Corey Lynch - SD2-A

#!/bin/bash

#Move the user to the home directory
cd ~

#Print a blank line for spacing - making program more readable
echo ""
echo "*NOTE* This script searches from the home directory. No need to include home dir in argument."
echo "Example Execute: ./task1.sh MyFolder/Example1/* example"
echo "This will search for the string 'example' from all files within the folder Example1"
echo ""

#Check if user passed 2 arguemnts
if [ $# -eq 2 ]
then
	#Ask the user for 2 arguemnts, path and string pattern
	echo "Entered path to a folder: $1"
	echo "Entered string pattern to look for: $2"
	#Print a blank line for spacing
	echo ""
	#List all contents of the directory
	echo "This folder contains the following files:"
	ls $1
	echo ""
else
	#User did not pass 2 arguments, print error and terminate
	echo "You must pass 2 arguments, path and string pattern"
	exit 1 
fi

#Search for string pattern in files
echo "The file(s) which contain(s) the string '$2' are:"
grep $2 $1

###I ATTEMPTED TO INCLUDE THE FILE SIZE IN THE OUTPUT BUT COULD NOT GET IT WORKING. I COMMENTED MY ATTEMPT BELOW###

#Create a variable that utilises the grep command on the arguments
#search=$(grep $2 $1)
#If statement to echo the search results along with the file sizes
#if [ "$search" ]
#then 
#	echo "$search"
#	file_size=$(stat -c%s $search)
#	echo $file_size
#fi
