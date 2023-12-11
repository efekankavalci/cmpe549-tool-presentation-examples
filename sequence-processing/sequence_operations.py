from Bio.Seq import Seq
gene  = Seq("GTGGCTGATCGTATC")
print(gene)
print(gene.complement())
print(gene.reverse_complement())
print(gene.transcribe())
print(gene.translate())



#gene or protein sequences can be stored in FASTA file format. It begins with a > and one line identifier. 
#FASTA  can contain more than 1 record.

from Bio import SeqIO
for sequence in SeqIO.parse("protein.fasta", "fasta"): 
    print(sequence.id)
    print(repr(sequence.seq))
    print(len(sequence))



#GC Content
from Bio.SeqUtils import gc_fraction
print(gc_fraction(gene))


#Six frame translations
from Bio.SeqUtils import six_frame_translations
print(six_frame_translations("ATGTAGTGATGGATGGCCCGTGAGTGAGGT"))


#Aminoacid - 1 letter code to 3 letter code
from Bio.SeqUtils import seq3
sequence = "MVCYGHWWMCVH"
print(seq3(sequence))







