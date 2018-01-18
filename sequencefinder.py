#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

from Bio import SeqIO

for i in range(len(sys.argv)):

    #this is a Boolean statement that says if the argument you've reached
    #in the for loop is -i, then the next argument should be assigned
    #to the Python variable Argument_1
    if sys.argv[i] == "-i": 
        Unique_Scaffolds = sys.argv[i+1]
    
    #This elif statement is another Boolean that says if the argument 
    #you've reached in the for loop is -o, then the next argument
    #should be assigned to the Python variable Argument_2.
    elif sys.argv[i] == "-s":
        Cymbo_Genome = sys.argv[i+1]

    elif sys.argv[i] == "-o":
        Results_File = sys.argv[i+1]



#Create a variable to read in the file of sequence ids, unique_scaffolds.txt



#Create a variable to read in the Cymbomonas genome file



#Create a variable to write to a new results file, results_file.fasta


#create a variable representing the information in your unique scaffolds file
#which contains an empty set
Wanted_Scaffolds = set()

#Open your file containing unique scaffold ids using a with statement that assigns
#the file to the variable f
with open(Unique_Scaffolds) as f:
    #write a for loop to strip white space from the file, skip empty lines, and
    #add sequence ids to the empty set, Wanted_Scaffolds, defined above
    for x in f:
    	x = x.strip()
    	if x != "":
    		Wanted_Scaffolds.add (x)





            
#Use SeqIO to open and parse the Cymbomonas genome file as a fasta file and assign
#those sequences to a variable
from Bio import SeqIO
sequences = SeqIO.parse(Cymbo_Genome, "fasta")


#Open your results file in order to write to it using a with statement that
#assigns the file to a variable f
with open(Results_File, "w") as f:
    #write a for loop to loop through the sequences in the sequence variable created above
   for line in sequences:
        #if the sequence id matching the sequence is in the set of sequence ids created above...
        if line.id in Wanted_Scaffolds:
            #Use SeqIO.write() to write those sequences to a fasta file
            SeqIO.write([line], f, "fasta")

