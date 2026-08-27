#!/bin/bash
sed '/>/d' FASTA.txt
sed 's/T/U/g' FASTA.txt
sed 's/seq1/human_gene/' FASTA.txt

