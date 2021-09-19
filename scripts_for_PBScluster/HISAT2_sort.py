import subprocess

srrlist_file = open("SRR_List.txt", "r")
srrlist = srrlist_file.read().split("\n")
for srr in srrlist:
	output = open(srr+'_HISAT2_sort.sh', 'w')
	print >> output, '#!/bin/bash'
	print >> output, '#PBS -l walltime=04:00:00'
	print >> output, '#PBS -l nodes=1:ppn=12'
	print >> output, '#PBS -N '+srr+'_HISAT2_sort.sh'
	print >> output, '#PBS -q secondary'
	print >> output, '#PBS -j oe'
	print >> output, '#PBS -o '+srr+'_HISAT2_sort.out'                                                           
	print >> output, '#PBS -e '+srr+'_HISAT2_sort.err'
	print >> output, '#'
	print >> output, '#####################################'

	print >> output, 'cd $PBS_O_WORKDIR'

	print >> output, 'module load java'

	print >> output, 'samtools sort -o ' +srr+'_paired_prinseq_good_hisat2_sorted.bam ' +srr+'_paired_prinseq_good_hisat2.sam'
	output.close()
	subprocess.call('chmod a+x '+srr+'_HISAT2_sort.sh', shell = "true")
	subprocess.call('qsub '+srr+'_HISAT2_sort.sh', shell = "true")

#samtools view +srr+_paired_prinseq_good_hisat2.sam |samtools sort -o +srr+_paired_prinseq_good_hisat2_sorted.bam -
