#!/bin/python
# script for generating the pbs job submission scripts for a large number of fastq files
#This takes a list of SRR ids and generates the shell scripts to submit a job for each fastq file to the cluster

import subprocess

srrlist_file = open("SRR_List.txt", "r")
srrlist = srrlist_file.read().split("\n")
#srrlist_file.close()
for srr in srrlist:
	output = open(srr+'_trimmomatic.sh', 'w')
	print >> output, '#!/bin/bash'
	print >> output, '#PBS -l walltime=04:00:00'
	print >> output, '#PBS -l nodes=1:ppn=16'
	print >> output, '#PBS -N '+srr+'_trimmomatic.sh'
	print >> output, '#PBS -q secondary'
	print >> output, '#PBS -j oe'
	print >> output, '#PBS -o '+srr+'_trimmomatic.out'                                                           
	print >> output, '#PBS -e '+srr+'_trimmomatic.err'
	print >> output, '#PBS -m be' 
	print >> output, '#'
	print >> output, '#####################################'

	print >> output, 'cd $PBS_O_WORKDIR'

	print >> output, 'module load java'

	print >> output, 'java -jar /projects/software_archive/Trimmomatic-0.38/trimmomatic-0.38.jar PE \
						-threads 16 -phred33 ' +srr+'_1.fastq.bz2 '+srr+'_2.fastq.bz2 ' +srr+'_paired_1.fastq ' \
						+srr+'_unpaired_1.fastq '+srr+'_paired_2.fastq '+srr+'_unpaired_2.fastq ' \
						'ILLUMINACLIP:TruSeq2-PE.fa:2:30:10 MINLEN:50'
	output.close()
	subprocess.call('chmod a+x '+srr+'_trimmomatic.sh', shell = "true")
	subprocess.call('qsub '+srr+'_trimmomatic.sh', shell = "true")
