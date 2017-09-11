#!/usr/bin/python
#Ghana S. Challa (challa.ghanashyam@gmail.com)

#script to identify AT tracts in a given DNA sequence.
# used in the wheat chromosome rearrangement paper

import sys
import re
from Bio import SeqIO

if len(sys.argv) !=2:
    
    print "Usage: AT_tract.py inputseq.fasta >output.txt"
else:
    inseq = open(sys.argv[1], "ru")
     
    for seq1 in SeqIO.parse(inseq, "fasta"):
        seq = str(seq1.seq)
#    runs = re.findall(r"[AT]{6,100}", seq)
#   print len(seq)
#   print(runs)
        runs = re.finditer(r"[AT]{6,100}", seq)
        print ("AT_tract_Seq\tStart\tEnd\tLength")
        for match in runs:
            run_start =match.start()
            run_end =match.end()
            AT_tract = match.group()
            match_len = len(AT_tract)
            print("%s\t%d\t%d\t%d") % (AT_tract,run_start,run_end,match_len)
            