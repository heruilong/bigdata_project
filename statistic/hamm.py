import sys
import fastq2reads

def distance(a,b):
    n = len(a)
    if n!=len(b): return "the length of two dna are not same!"
    dist = 0
    for i in range(0,n):
        if a[i]!=b[i]: dist=dist+1
    return dist

def getHamm(absPath,count=1000):
    hamm=[]
    fastq=fastq2reads.getReads(absPath)
    if count<=1 :count=1000
    reads = fastq[1::4][:count]
    for pos in (xrange(1,len(reads))):
        hamm.append(distance(reads[pos-1],reads[pos]))
    return sorted(hamm,reverse=True)

if __name__=="__main__":
    print getHamm(sys.argv[1],int(sys.argv[2]))
