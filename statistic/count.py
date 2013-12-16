import sys

# count the number of A C G T of each dna sequence
def dnaCount(dna):
        return (dna.count('A'),dna.count('C'),dna.count('G'),dna.count('T'))

# count all A C G T of one fasta file.
def fastaCount(fastaArr):
	countRes = [0,0,0,0]
	for dna in fastaArr[1::2]:
		eachCount = dnaCount(dna)
		for i in xrange(0,len(countRes)):
			countRes[i] += eachCount[i]
	return countRes

# test
def test():
	fastaStr = sys.stdin.read()
	print fastaCount(fastaStr)	
	
