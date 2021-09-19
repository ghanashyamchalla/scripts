import subprocess

srrlist_file = open("SRR_List.txt", "r")
srrlist = srrlist_file.read().split("\n")
for srr in srrlist:
	output = open(srr+'_stringtie.sh', 'w')
	print >> output, '#!/bin/bash'
	print >> output, '#PBS -l walltime=04:00:00'
	print >> output, '#PBS -l nodes=1:ppn=12'
	print >> output, '#PBS -N '+srr+'_stringtie.sh'
	print >> output, '#PBS -q secondary'
	print >> output, '#PBS -j oe'
	print >> output, '#PBS -o '+srr+'_stringtie.out'                                                           
	print >> output, '#PBS -e '+srr+'_stringtie.err'
	print >> output, '#'
	print >> output, '#####################################'

	print >> output, 'cd $PBS_O_WORKDIR'

	print >> output, 'module load java'

	print >> output, '/projects/stringtie-1.3.5.Linux_x86_64/stringtie '+srr+'_paired_prinseq_good_hisat2_sorted.bam -p 12 -G /projects/common_data_dump/tair10/Araport11_GFF3_genes_transposons.201606.gff -A '+srr+'_gene_abundances.tab -o '+srr+'_stringtie.gtf'
	output.close()
	subprocess.call('chmod a+x '+srr+'_stringtie.sh', shell = "true")
	subprocess.call('qsub '+srr+'_stringtie.sh', shell = "true")


