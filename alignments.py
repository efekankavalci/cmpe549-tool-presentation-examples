#GLOBAL ALIGNMENT
#Align module contains many different functions and methods to perform both local and global alignments.
from Bio import Align

#Create an object from the Align module. Set the match score. For every match, the score will increment.
#We can put that object into a variable.

aligner = Align.PairwiseAligner(match_score = 2.0)

seq1 = "GAACT"
seq2 = "GAT"

#Get score using score method
score = aligner.score(seq1, seq2)
print(f" The score of the alignment is {score}")

#This is default by global aligment so it will give you all the optimal global possibilities.
alignments = aligner.align(seq1, seq2)
for alignment in alignments:
    print(alignment)



#LOCAL ALIGNMENT
aligner.mode = "local"

seq3 = "ATTAATG"
seq4 = "TAAT"

localscore = aligner.score(seq3,seq4)

print(f"The local alignment score is {localscore}")

alignment_local = aligner.align(seq3, seq4)

for alignment in alignment_local:
    print(alignment)
