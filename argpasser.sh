#!/bin/bash


#$1 $2 all stand for arguments

if [ $# -lt 4 ]; then
	echo "$0: Not enough arguments"
	echo "Usage: $0 "

	exit
elif [ $# -gt 4 ]; then
	echo "$0: Too many arguments"
	echo "Usage: $0 "

	exit
fi 
python sequencefinder.py -i $1 -s $2 -o $3
python cg_calculator.py -i $3 -o $4


exit