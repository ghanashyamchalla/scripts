#!/bin/bash


#PBS -l walltime=125:00:00
#PBS -l nodes=1:ppn=1
#PBS -N Prinseq
#PBS -q sib
#PBS -j oe
###PBS -o serial.out                                                            
###PBS -e serial.err
###PBS -m be  
#
#####################################

# Change to the directory from which the batch job was submitted
cd $PBS_O_WORKDIR

module load java

# Run the serial code
for srr in $(cat SRR_List.txt);do
  perl /projects/prinseq-lite-0.20.4/prinseq-lite.pl -verbose -fastq "$srr"_paired_1.fastq -fastq2 "$srr"_paired_2.fastq -ns_max_n 0 -min_len 50 -min_qual_mean 30 -trim_qual_type mean -trim_qual_left 30 -trim_qual_right 30 -trim_qual_window 3 -trim_qual_step 1 
done
