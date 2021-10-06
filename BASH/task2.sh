#### TASK 2 ####
# Corey Lynch - SD2-A 

#!/bin/bash

#Function for writing to a file 
write_to_file() 
{
	#Initialise entry variable
	entry=0
	#Read in file name from user
	echo ""
	echo "Please enter the file name in which you would like to write to."
	read write_file_name
	#While the user does not input Exit, request the data the user would like to write 
	while [ "$entry" != "end" ]
		do
			echo ""
			echo "Please input what you would like to write to the file."
			echo "*NOTE* Type 'end' to exit back to the main menu. "
			echo ""
			read entry
			echo "$entry" >> "$write_file_name"
	done
}

#Function for reading from a file
read_from_file()
{
	#Ask user for the name of the file they would like to read from
	echo ""
	echo "Please enter the name of the file in which you would like to read from."
	read read_file_name
	if [ -w $read_file_name ]
	then
		#Print contents of file to terminal
		echo ""
		echo "Contents of $read_file_name: "
		less $read_file_name
	else
		#If file does not exist, print error
		echo ""
		echo "The file $read_file_name does not exist!"
	fi
}

#Function to rename a file
rename_file()
{	
	echo ""
	#Read in the file name in which user would like to rename
	echo "Please enter the name of the file in which you would like to rename."
	read rename_file_name
	if [ -w $rename_file_name ]
	then
		#If file exists, rename file
		echo ""
		echo "Please enter the new name for the specified file."
		read new_rename_file_name
		mv $rename_file_name $new_rename_file_name
	else
		#If file does not exist, print error
		echo ""
		echo "The file $rename_file_name does not exist!"
	fi
}

#Function to quit program
quit()
{
	exit 0
}

#Generate user menu and take the users input
echo ""
PS3="Please enter your menu choice (1-4). "
options=("Write To File" "Read From File" "Rename File" "Quit")
select user_option in "${options[@]}"
do
	echo ""
	case $user_option in
		"Write To File")
			echo "You selected '$user_option'."
			write_to_file
			;;
		"Read From File")
			echo "You selected '$user_option'."
			read_from_file
			;;
		"Rename File")
			echo "You selected '$user_option'."
			rename_file
			;;
		"Quit")
			echo "Thank You and Goodbye!"
			quit
			;;
		*) echo "Invalid option"
	esac
done



