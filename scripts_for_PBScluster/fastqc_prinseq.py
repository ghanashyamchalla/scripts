import subprocess

srrlist_file = open("SRR_List.txt", "r")
srrlist = srrlist_file.read().split("\n")
for srr in srrlist:
	output = open(srr+'_fastqc_prinseq.py', 'w')
	print >> output, '#!/bin/bash'
	print >> output, '#PBS -l walltime=04:00:00'
	print >> output, '#PBS -l nodes=1:ppn=12'
	print >> output, '#PBS -N '+srr+'_fastqc_prinseq.py'
	print >> output, '#PBS -q secondary'
	print >> output, '#PBS -j oe'
	print >> output, '#PBS -o '+srr+'_fastqc_prinseq.out'                                                           
	print >> output, '#PBS -e '+srr+'_fastqc_prinseq.err'
	print >> output, '#PBS -m be' 
	print >> output, '#'
	print >> output, '#####################################'

	print >> output, 'cd $PBS_O_WORKDIR'

	print >> output, 'module load java'

	print >> output, '/projects/software_archive/FastQC/fastqc ' +srr+'_paired_1_prinseq_good.fastq'
	'/projects/software_archive/FastQC/fastqc ' +srr+'_paired_2_prinseq_good.fastq'
	output.close()
	subprocess.call('chmod a+x '+srr+'_fastqc_prinseq.py', shell = "true")
	subprocess.call('qsub '+srr+'_fastqc_prinseq.py', shell = "true")
