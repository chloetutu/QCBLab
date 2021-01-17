#%% ------ FINAL PROJECT ------
#  For the final activity: Use what we have learned during last three days to read
#a file (say, SARS-N.seq, but any other FASTA formatted DNA sequence file would be
#fine; passing the file name as a command line argument would be nice ;o) with
#a DNA sequence corresponding to a fragment of SARS virus genome (NOTE: SARS genome
#is encodeded by RNA but the file contains corresponding DNA sequence) and find out
#what are the sequences of proteins it might encode. You will need to add some code
# to remove  spaces and new line ('\n') characters that appear in the file. You will
# also have to skip the first line (header) of the file. Once the DNA sequence is
# ready to process you will have to iterate over 3 letter substrings (codons) and use
# translation table (after reading it from codon-table.txt file) to infer which aminoacid
# or stop codon each substring correspond to. Note, that translation might start in 3
# different 'reading frames'  each shifted by one position. It is also possible that the
# complementary DNA strand might be translated (in case of SARS virus it does not happen
# but is possible for any organism with DNA-based genome) How will you handle these cases ?

# NOTE: This is, in principle, the core functionality provided by

# https://web.expasy.org/translate/

# Web page. You can use it to verify the output of your program.

#%%----------------------------
# Chloe Tu
# W9 INTRO TO PYTHON FINAL PROJECT
           
def reading_frame(seq, rf):                         # prints AA sequence given the reading frame
    while (seq):
        seq = seq[rf:]
        codon = seq[:3]
        seq = seq[3-rf:]
        if codon in codon_table:
            print(codon_table[codon], end = " ")

def for_rev_translation(seq,codon_table):           # sets reading frame and calls funct. reading_frame for template and complementary strand 
    for rf in range(0,3):
        print("5'-3' Reading Frame", rf + 1)
        reading_frame(seq, rf)
        print("\n")
    seq = seq.replace("A", "t")                     # obtaining complementary sequence from template sequence
    seq = seq.replace("T", "a")
    seq = seq.replace("C", "g")
    seq = seq.replace("G", "c")
    seq = seq.upper()
    seq = seq[::-1]
    for rf in range(0,3):
        print("3'-5' Reading Frame", rf + 1)
        reading_frame(seq, rf)
        print("\n")
        
seq = ""
codon_table = {}   

with open("SARS-N.seq") as seqfile:
    for line in seqfile:
        if not line.startswith(">"):
            seq = seq + line.strip()
            seq = seq.replace(" ", "")
            seq = seq.upper()

with open("codon-table.txt", "r") as codonfile:
    for line in codonfile:                    
        line = line.strip()            
        cols = line.split()           
        if len(cols) == 3:              
            codon_table[cols[0]] = cols[1]
            
for_rev_translation(seq, codon_table)

       
        
       
        
       
        
       