#!/bin/bash


#PBS -l walltime=96:00:00
#PBS -l nodes=1:ppn=16
#PBS -N trimmer_fastqc
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

for srr in $(cat SRR_List.txt);do
	java -jar /projects/software_archive/Trimmomatic-0.38/trimmomatic-0.38.jar PE -threads 16 -phred33 "$srr"_1.fastq.bz2 "$srr"_2.fastq.bz2 "$srr"_paired_1.fastq "$srr"_unpaired_1.fastq "$srr"_paired_2.fastq "$srr"_unpaired_2.fastq ILLUMINACLIP:TruSeq2-PE.fa:2:30:10 MINLEN:50
	/projects/software_archive/FastQC/fastqc "$srr"_paired_1.fastq
	/projects/software_archive/FastQC/fastqc "$srr"_paired_2.fastq
done