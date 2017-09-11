#!/usr/local/bin/perl

#   Ghana S. Challa (challa.ghanashyam@gmail.com)
#   It may be freely distributed under GNU General Public License.
#   This perl scripts takes in the NCBI BLAST output in the alignment format (-outfmt 0) and reports the results in the tabular format.
#   This scripts reports only the first hit assuming it is the tophit. If you want to sort differently, do it while running BLAST using the inbuit sort option.
#   Can be changed to report all the hits in the output file.
#   The output of this script is a tab-delimited file with Query name, query length, Hit name, Hit length, E-value, Alignment length, Query coverage, Percent Identity of alignment, percent of matches per query, Number of matches, Bit score and HSP count.

#Usage : perl Blast_Output_to_Table.pl <BLAST_Output_file> <Parsed_Tabular_outfile_name>


use strict;
use warnings;
use Bio::SearchIO;
use Bio::Search::Tiling::MapTiling;


# Usage information
die "Usage: $0 <BLAST_Output_File> <Parsed_Output_File>\n", if (@ARGV != 2);

my $infile = $ARGV[0];
my $outfile =$ARGV[1];
print "Parsing the BLAST output from file $infile\n";

open (OUT,">$outfile") or die "Cannot open $outfile: $!";

print OUT "Query_Name\tQuery_Length\tHit_Name\tHit_Length\tE-Value\tAlignment_Length\tQuery_Coverage\tPercent_Identity\tIdentities_Covered_percent\tNumber_of_Matches\tBit_Score\tHSPs\n";

my $in = Bio::SearchIO->new(-format => 'blast', -file => $infile);
#my $result = $in->next_result;
while (my $result = $in->next_result) {

	my $qid = $result->query_name;
	my $qlen = $result->query_length;
	if ($result->num_hits==0) {
	print $qid."\t".$qlen."\t"."No hits found\n"; #writes to the STDOUT
	}
	else {
	
	my $hit = $result->next_hit; #Use this for reprting only the top hit (sorting depends on the blast run).
        #Instead of looping through the hits, here we only take the first result (assuming it as top hit reported by the BLAST program). 
	#while ($hit = $result->next_hit){ #use this to report all Hits from Blast Ouput
		my $tiling = Bio::Search::Tiling::MapTiling->new($hit);	
		my $subject_id = $hit->accession;
		my $subject_len = $hit->length;
		my $evalue = $hit->significance;
		my $bitScore = $hit->bits;
        my $hsp_count = $hit->num_hsps;
		
		my $align_length_query = $tiling->length('query'); # length of aquery sequence in tiled alignment
		my $query_coverage_unrounded = $align_length_query*100/$qlen;
		my $query_coverage = sprintf "%.2f",$query_coverage_unrounded;
		#my $sub_length_tiling = $tiling->length('subject'); # total length of aligned residues in subject sequence
		my $query_identity_unrounded = $tiling->frac_identical('query', 'aligned')*100; #percent ID of the aligned part of the query (identical residues/alignment length)
		my $query_identity = sprintf "%.2f",$query_identity_unrounded;
		my $residue_cov_q_unrounded = $tiling->percent_identity('query'); #percent of identitical base pairs compared to query seq length
		my $residue_cov_q = sprintf "%.2f",$residue_cov_q_unrounded;
		my $q_identities = $tiling->identities('query'); #number of identical residues of query sequence in tiled alignment
			
		printf OUT $qid."\t".$qlen."\t".$subject_id."\t".$subject_len."\t".$evalue."\t".$align_length_query."\t".$query_coverage."\t".$query_identity."\t".$residue_cov_q."\t".$q_identities."\t".$bitScore."\t".$hsp_count;
		print OUT "\n";
		}
}
close OUT;
print " DONE!!!\n";
