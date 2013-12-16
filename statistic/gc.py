import sys

def computeGC(read):
    gc=read.count('c')+read.count('g')+read.count('C')+read.count('G')
    gc/=1.0*len(read)
    return gc

def getGCs(absPath):
    gcs=[]
    read=[]
    with open(absPath,'r') as f:
        for line in f:
            line = line.strip()
            if '>' in line:
                if len(read)>0: gcs.append(computeGC(''.join(read)))
                read=[]
            else:
                read.append(line)
    if len(read)>0: gcs.append(computeGC(''.join(read)))
            
    return sorted(gcs,reverse=True)

if __name__=="__main__":
    print getGCs(sys.argv[1])
