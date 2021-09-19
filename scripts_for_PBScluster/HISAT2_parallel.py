import subprocess

srrlist_file = open("SRR_List.txt", "r")
srrlist = srrlist_file.read().split("\n")
for srr in srrlist:
	output = open(srr+'_HISAT2_parallel.py', 'w')
	print >> output, '#!/bin/bash'
	print >> output, '#PBS -l walltime=04:00:00'
	print >> output, '#PBS -l nodes=1:ppn=12'
	print >> output, '#PBS -N '+srr+'_HISAT2_parallel.py'
	print >> output, '#PBS -q secondary'
	print >> output, '#PBS -j oe'
	print >> output, '#PBS -o '+srr+'_HISAT2_parallel.out'                                                           
	print >> output, '#PBS -e '+srr+'_HISAT2_parallel.err'
	print >> output, '#PBS -m be' 
	print >> output, '#'
	print >> output, '#####################################'

	print >> output, 'cd $PBS_O_WORKDIR'

	print >> output, 'module load java'

	print >> output, '/projects/software_archive/hisat2-2.1.0/hisat2 -p 12 -x /projects/common_data_dump/TAIR10_hisat2 -1 ' +srr+'_paired_1_prinseq_good.fastq -2 ' +srr+'_paired_2_prinseq_good.fastq -S ' +srr+'_paired_prinseq_good_hisat2.sam'
	output.close()
	subprocess.call('chmod a+x '+srr+'_HISAT2_parallel.py', shell = "true")
	subprocess.call('qsub '+srr+'_HISAT2_parallel.py', shell = "true")


