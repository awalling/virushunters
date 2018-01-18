#!/bin/bash


#$1, $2, $3, $4 all stand for arguments

#$0 means the first item in command line, which is the
#name of the script

#This code prints out "Not enough arguments", if there are 
#less than 4 arguments in the command line
if [ $# -lt 4 ]; then
	echo "$0: Not enough arguments. You need to input ./argpasser.sh followed by 4 file names."
	echo "The first file should be a scaffolds file"
	echo "The second file should be a fasta file"
	echo "The third file should be the name you want the output file name to be, from the first python script"
	echo "The fourth file should be the name you want the output file name to be, from the second python script"
	echo "Usage: $0 "

	exit
#This code prints out "Too many arguments", if there are 
#more than 4 arguments in the command line
elif [ $# -gt 4 ]; then
	echo "$0: Too many arguments. You need to input ./argpasser.sh followed by 4 file names." 
	echo "The first file should be a scaffolds file"
	echo "The second file should be a fasta file"
	echo "The third file should be the name you want the output file name to be, from the first python script"
	echo "The fourth file should be the name you want the output file name to be, from the second python script"
	echo "Usage: $0 "

	exit
#Then this code calls the python scripts and passes the
#arguments needed for each of the files
fi 
python sequencefinder.py -i $1 -s $2 -o $3
python gc_calculator.py -i $3 -o $4


exit