#!/usr/bin/python

from coreapi import Client
from Bio import SeqIO
import sys
import os
from collections import OrderedDict
from requests.exceptions import ConnectionError

try:
    inputfile= open (sys.argv[1], 'r')
    # to get the last argument on command line
    filename = sys.argv[-1]
    #outputfile name to store the results
    outputfilename=os.path.splitext(filename)[0] + '.txt'
    outputfilename1=os.path.splitext(filename)[0]+ 'finaltable' + '.txt'
    try:
        #Connecting to JASPAR
        client=Client()
        document=client.get('http://jaspar.genereg.net/api/v1/docs/')
    except ConnectionError as e:
        print e
        print "Database is not responding. Try again later. "
    print "Profile Inference Search Started....."
    for record in SeqIO.parse(inputfile, "fasta"):
        
        recordseq=record.seq
        
        action=["infer","read"]
        params={"sequence": '%s'%recordseq,}
        result=client.action(document, action, params=params)
        data1= record.id + "#" + str(result)
        with open(outputfilename, 'a') as the_file:
            the_file.write(str(data1)+'\n')
except:
    print "Provide sequence file"
    
finally:
    the_file.close()
    print "Profile Inference Search Finished"

       
resultfinle=open(outputfilename, 'r')   

print "Generating File....."

with open(outputfilename1, 'a') as the_file:
    the_file.write( "GeneID"+'\t'+ "Profile_Name"+'\t'+ "url"+'\t'+"Evalue" +'\t'+ "Matrix_id" +'\t'+ "dbd" +'\t'+ "sequence_logo" +'\n')
    for line in resultfinle:
        line2=line.split('#')
        a = eval(line2[1], {'OrderedDict': OrderedDict})
        dictfilt = lambda x, y: dict([ (i,x[i]) for i in x if i in set(y) ])
    
        wanted_keys = ("count","results")
    
        result1 = dictfilt(a, wanted_keys)
        data1=result1.get('results')
        for elements in data1:
            the_file.write(line2[0]+'\t')
            for key1, value2 in elements.items():
                the_file.write(str(value2)+'\t')
                if key1 == 'sequence_logo':
                    the_file.write('\n')
the_file.close()  

os.remove(outputfilename)   
        

    
    

