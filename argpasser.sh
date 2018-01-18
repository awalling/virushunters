#!/bin/bash


#$1, $2, $3, $4 all stand for arguments

#This code prints out "Not enough arguments", if there are 
#less than 4 arguments in the command line
if [ $# -lt 4 ]; then
	echo "$0: Not enough arguments"
	echo "Usage: $0 "

	exit
#This code prints out "Too many arguments", if there are 
#more than 4 arguments in the command line
elif [ $# -gt 4 ]; then
	echo "$0: Too many arguments"
	echo "Usage: $0 "

	exit
#Then this code calls the python scripts and passes the
#arguments needed for each of the files
fi 
python sequencefinder.py -i $1 -s $2 -o $3
python cg_calculator.py -i $3 -o $4


exit