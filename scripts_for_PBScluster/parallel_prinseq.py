srrlist_file = open("Nitrogen_time_series_SRR_List.txt", "r")
srrlist = srrlist_file.read().split("\n")

for srr in srrlist:
	output = open(srr+'_parallel_prinseq.sh', 'w')
	print >> output, '#!/bin/bash'
	print >> output, '#PBS -l walltime=04:00:00'
	print >> output, '#PBS -l nodes=1:ppn=16'
	print >> output, '#PBS -N '+srr+'_parallel_prinseq.sh'
	print >> output, '#PBS -q secondary'
	print >> output, '#PBS -j oe'
	print >> output, '#PBS -o '+srr+'_parallel_prinseq.out'                                                           
	print >> output, '#PBS -e '+srr+'_parallel_prinseq.err'
	print >> output, '#PBS -m be' 
	print >> output, '#'
	print >> output, '#####################################'

	print >> output, 'cd $PBS_O_WORKDIR'

	print >> output, 'module load java'

	print >> output, 'perl /projects/prinseq-lite-0.20.4/prinseq-lite.pl -verbose -fastq \
						' +srr+'_paired_1.fastq -fastq2 ' +srr+'_paired_2.fastq -ns_max_n 0 -min_len \
						50 -min_qual_mean 30 -trim_qual_type mean -trim_qual_left 30 \
						-trim_qual_right 30 -trim_qual_window 3 -trim_qual_step 1' 
	output.close()
	subprocess.call('chmod a+x '+srr+'_parallel_prinseq.sh', shell = "true")
	subprocess.call('qsub '+srr+'_parallel_prinseq.sh', shell = "true")
