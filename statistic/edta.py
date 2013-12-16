import sys
import geneFormat
import fastq2reads
from numpy import zeros

def edDistDp(x, y):
    """ Calculate edit distance between sequences x and y using
        matrix dynamic programming.  Return distance. """
    D = zeros((len(x)+1, len(y)+1), dtype=int)
    D[0, 1:] = range(1, len(y)+1)
    D[1:, 0] = range(1, len(x)+1)
    for i in xrange(1, len(x)+1):
        for j in xrange(1, len(y)+1):
            delt = 1 if x[i-1] != y[j-1] else 0
            D[i, j] = min(D[i-1, j-1]+delt, D[i-1, j]+1, D[i, j-1]+1)
    return D[len(x)][len(y)]

def getDist(absPath,count=1000):
    fastq = fastq2reads.getReads(absPath)
    if count<=1 :count=1000
    reads = fastq[1::4][:count]    
    dist=[]
    for pos in xrange(1,len(reads)):
        dist.append(edDistDp(reads[pos-1],reads[pos]))
    return sorted(dist,reverse=True)

if __name__=="__main__":
    print getDist(sys.argv[1],int(sys.argv[2]))
