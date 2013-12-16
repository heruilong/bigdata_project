import sys
import fastq2reads
import layout
import overlap
import dc
import hamm

def getPartAssembly(fastq,links,pos):
    if len(links)==0 : return []
    assert pos< len(links)
    links_part = links[pos]
    occurence = []
    segments = []
    offset = 0
    for i in xrange(len(links_part)):        
        read_id = links_part[i][0][0]
        for j in xrange(len(fastq[read_id*4+1])):
            if len(occurence) <= offset+j :
                occurence.append([fastq[read_id*4+1][j],1])
            else :
                occurence[offset+j][1]+=1
        offset += links_part[i][0][1]
        segments.append(fastq[4*read_id:4*read_id+4])
    return occurence,segments
'''
def getHamm(fastq,links,count):
    dist=[]
    for k in xrange(len(links)):
        for i in xrange(len(links[k])):
            if count==0 : return dist

            read_id1 = links[k][i][0][0]
            read_id2 = links[k][i][1][0]
            dis.append(hamm.distance(fastq[read_id1*4+1],fastq[read_id2*4+1]))
            count-=1
    return dist
'''            

def getAssembly(absPath,count=2000000):
    fastq=fastq2reads.getReads(absPath)
    if count<=1 :count=1000
    reads = [ read+'0' for read in fastq[1::4][:count]]
    SA = dc.getSA(''.join(reads))
    links = overlap.getOverlap(SA,reads)
    links = layout.getLayout(links)
    return getPartAssembly(fastq,links,0)
    #return getHamm(fastq,links,1000)

if __name__=="__main__":
    print getAssembly(sys.argv[1],int(sys.argv[2]))
