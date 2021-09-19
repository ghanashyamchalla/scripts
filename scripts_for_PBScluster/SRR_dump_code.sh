#!/bin/bash


#PBS -l walltime=96:00:00
#PBS -l nodes=1:ppn=1
#PBS -N dataDump
#PBS -q sib
#PBS -j oe
###PBS -o serial.out                                                            
###PBS -e serial.err
###PBS -m be  
#
#####################################

# Change to the directory from which the batch job was submitted
cd $PBS_O_WORKDIR

for srr in $(cat SRR_List.txt);do
	wget ftp://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/${srr:0:3}"/"${srr:3:3}"/"$srr"/"$srr".sra
	/projects/software/sratoolkit.2.9.2-centos_linux64/bin/fastq-dump —-bzip2 split-files ./"$srr".sra
	/projects/software/FastQC/fastqc "$srr"_1.fastq "$srr"_2.fastq
done
