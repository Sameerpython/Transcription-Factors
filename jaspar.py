#!/usr/bin/python

from coreapi import Client
from Bio import SeqIO
import sys
import os

inputfile= open (sys.argv[1], 'r')

# to get the last argument on command line
filename = sys.argv[-1]

client=Client()

#outputfile name to store the results
outputfilename=os.path.splitext(filename)[0] + '.txt'


#Connecting to JASPAR
document=client.get('http://jaspar.genereg.net/api/v1/docs/')

#Provide sequence in fasta as input file
for record in SeqIO.parse(inputfile, "fasta"):
        
        recordseq=record.seq
        
        action=["infer","read"]
        params={"sequence": '%s'%recordseq,}
        result=client.action(document, action, params=params)
        data1= record.id + "#" + str(result)
        with open(outputfilename, 'a') as the_file:
            the_file.write(str(data1)+'\n')

the_file.close()
        
        
        

    
    

