import Bio
from Bio import SeqIO
import csv
import sys
import math


def main(input_file,output_file_name):
    #the DNA sequence file
    dna_sequence = Bio.SeqIO.parse(input_file, 'fasta')


    #variables
    c_counter = 0
    g_counter = 0
    n_counter = 0
    a_counter = 0
    t_counter = 0
    final = 0
    total2 = 0
    seq = 0

    #create a csv file called gcdata.csv to append our data
    with open(output_file_name, 'w') as f:
        writer = csv.writer(f)

        #for loop that loops through the different sequence in the data file
        for seq_record in dna_sequence:
            seq = (seq_record.seq)
            #loops through every nucleotide in each sequence and incriments the specific
            #counter by 1 everytime it loops through the corresponding nucleotide
            for base in seq:
                if base == 'C':
                    c_counter += 1
                elif base == 'G':
                    g_counter += 1
                elif base == 'N':
                    n_counter += 1
                elif base == 'A':
                    a_counter += 1
                elif base == 'T':
                    t_counter += 1
            #prints the sequence id
            print seq_record.id
            #the total of all the Bases to find the mean
            total = c_counter + g_counter + n_counter + a_counter + t_counter
            #find the percentage of C and G and then adding them together
            cpercentage = float(c_counter)/ float(total) * 100
            gpercentage = float(g_counter)/ float(total) * 100
            gcpercentage = cpercentage + gpercentage
            #add all the GC percentages of the different DNA sequences to find the mean
            final += gcpercentage
            #append the items in my list to the csv file created above
            mylist =[seq_record.id, c_counter, g_counter, gcpercentage]
            writer.writerow(mylist)
            #print the number of G and C and the Percentage for each DNA sequence
            print 'NUMBER OF G: ', g_counter
            print 'NUMBER OF N: ', n_counter
            print 'PERCENTAGE: ', gcpercentage,'%'
            print '--------------------------------------------------'
            c_counter = 0
            g_counter = 0
            n_counter = 0
            a_counter = 0
            t_counter = 0
        #calculate the mean

        scaffolds = []
        #n = SeqIO.parse(input_file, 'fasta')
        #for seq_record in n:
            #scaffolds.append(seq_record.id)
        for seq_record in dna_sequence:
            seq = (seq_record.seq)
            scaffolds.append(seq_record.id)
            print seq_record.id

        m = len(scaffolds)

        mean = final/ m
        first = gcpercentage - mean
        second = math.pow(first, 2)
        total2 += second
        mean2 = total2 / m
        fianldeviation = math.sqrt(total2)

        print 'MEAN: ', mean, '%'
        print 'STANDARD DEVIATION: ', fianldeviation
        print '--------------------------------------------------'

        #append the mean to the csv file
        writer.writerow(['MEAN', mean])
        writer.writerow(['STANDARD DEVIATION', fianldeviation])

    #close csv file
    f.close()

for i in range(len(sys.argv)):

    #this is a Boolean statement that says if the argument you've reached
    #in the for loop is -i, then the next argument should be assigned
    #to the Python variable Argument_1
    if sys.argv[i] == "-i":
        input_file = sys.argv[i+1]

    #This elif statement is another Boolean that says if the argument
    #you've reached in the for loop is -o, then the next argument
    #should be assigned to the Python variable Argument_2.
    elif sys.argv[i] == "-o":
        output_file_name = sys.argv[i+1]

main(input_file,output_file_name)
