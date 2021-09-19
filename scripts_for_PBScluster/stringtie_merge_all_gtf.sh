#!/bin/bash


#PBS -l walltime=10:00:00
#PBS -l nodes=1:ppn=12
#PBS -N stringtie_merge_all_gtf
#PBS -q sib
#PBS -j oe
###PBS -o stringtie_merge_all_gtf.out                                                            
###PBS -e stringtie_merge_all_gtf.err
###PBS -m be  
#
#####################################

# Change to the directory from which the batch job was submitted
cd $PBS_O_WORKDIR

module load java
/projects/stringtie-1.3.5.Linux_x86_64/stringtie --merge stringtie_all_gtf.txt -G /projects/common_data_dump/tair10/Araport11_GFF3_genes_transposons.201606.gff -o stringtie_merge_all_gtf.gtf
