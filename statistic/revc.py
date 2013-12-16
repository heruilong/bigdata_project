import sys

def reverse(dna):
    return dna[::-1]

def complement(dna):
    dna = dna.replace('1','').replace('2','').replace('3','').replace('4','')
    temp = dna.replace('A','1').replace('T','2').replace('C','3').replace('G','4')
    compl = temp.replace('1','T').replace('2','A').replace('3','G').replace('4','C')
    return compl

def run(dna):    
    rev = reverse(dna)
    compl = complement(rev)
    return compl
