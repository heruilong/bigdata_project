#!/usr/bin/env python
import sys

def getReads(absPath):
    fastq=[]
    with open(absPath,'r') as f:
        for line in f:
            line = line.strip()
            fastq.append(line.upper())

    return fastq

if __name__=="__main__":
    fastq = getReads(sys.argv[1])
    print ''.join(fastq)
