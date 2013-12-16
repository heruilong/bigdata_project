import sys
import geneFormat
import revc

def findM(dna):
    pos = dna.find("ATG")
    return dna[pos::] if pos>=0 else ''

def trans(dna):
    rna = geneFormat.transcript(dna)
    prot = geneFormat.translate(rna)
    return prot

def getOrfs(prot,orfs):
    while(True):
        start = prot.find("M")
        if start <0 : break
        prot = prot[start::]
        end = prot.find(".")
        if end <=0 : break
        orf = prot[:end:]
        orfs.add(orf)
        prot = prot[1::]        
    return orfs

def run(dna):
    orfs = set()
    rev = revc.run(dna)
    for i in xrange(0,6):
        frame = dna[i/2::] if i%2==0 else rev[i/2::]
        prot = trans(frame)
        orfs = getOrfs(prot,orfs)        
    return orfs

def getOrfLen(absPath,count=5):
    orfs_len=[]
    read=[]
    if count<=0 :count=5
    with open(absPath,'r') as f:
        for line in f:
            if count<0:break
            line = line.strip()
            if '>' in line:
                if len(read)>0: orfs_len.append(len(run(''.join(read))))
                read=[]
                count-=1
            else:
                read.append(line)
    if len(read)>0: orfs_len.append(len(run(''.join(read))))     
    return orfs_len
    
if __name__=="__main__":
    print getOrfLen(sys.argv[1],int(sys.argv[2]))
    
   
