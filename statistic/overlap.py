#!/usr/bin/env python
import sys
import fastq2reads
import dc
import bisect
from os import path 

# Return the longest prefix of all list elements.
def commonprefix(m):
    "Given a list of pathnames, returns the longest common leading component"
    if not m: return ''
    s1 = min(m)
    s2 = max(m)
    for i, c in enumerate(s1):
        if c != s2[i]:
            return s1[:i]
    return s1

def downSearch(SA,reads,links,pos,pre_nodes):
    read_id1 = SA[pos][0]; start1=SA[pos][1] #start1=0
    com_prefix = reads[read_id1]
    for j in xrange(pos+1,len(SA)):
        if len(pre_nodes)==len(reads)-1: break  
        read_id2 = SA[j][0]; start2=SA[j][1]
        if read_id1==read_id2 or read_id2 in pre_nodes : continue
        com_prefix = path.commonprefix([reads[read_id1],reads[read_id2][start2:]])
        if len(com_prefix)< len(reads[read_id1])-1 : break
        pre_nodes.add(read_id2)
        #print read_id2,read_id1,com_prefix
        links.append((SA[j],SA[pos],len(com_prefix)))

def upSearch(SA,reads,links,pos,pre_nodes):
    min_overlap=7
    deep=4
    read_id1 = SA[pos][0]; start1=SA[pos][1] #start1=0
    com_prefix = reads[read_id1]
    for j in xrange(pos-1,0-1,-1):
        if len(pre_nodes)==len(reads)-1: break
        if deep<1 : break
        read_id2 = SA[j][0]; start2=SA[j][1]
        if read_id1==read_id2 or read_id2 in pre_nodes : continue
        if len(com_prefix)< len(reads[read_id2][start2:])-1 : continue
        com_prefix = path.commonprefix([reads[read_id1],reads[read_id2][start2:]])
        if len(com_prefix)< min_overlap : break
        if len(com_prefix)!= len(reads[read_id2][start2:])-1 : continue
        deep-=1        
        pre_nodes.add(read_id2)
        #print read_id2,read_id1,com_prefix
        links.append((SA[j],SA[pos],len(com_prefix)))

def getLink(SA,reads):
    pos = 0
    links = []
    for i in xrange(len(SA)):
        if SA[i][1]!=0: continue        
        pre_nodes = set()
        downSearch(SA,reads,links,i,pre_nodes)
        upSearch(SA,reads,links,i,pre_nodes)
    return sorted(links, key=lambda p: p[2], reverse=True)

def getLen_read(reads):
    len_read = [ len(read) for read in reads]
    for pos in xrange(1,len(len_read)):
        len_read[pos]+=len_read[pos-1]
    return len_read

def getSATuple(SA,reads):
    len_read = getLen_read(reads)
    for i in xrange(len(SA)):
        read_id = bisect.bisect_right(len_read,SA[i])
        if read_id==0: SA[i] = (read_id,SA[i])
        else         : SA[i] = (read_id,SA[i]-len_read[read_id-1])
    return SA

def getOverlap(SA,reads):
    SA=getSATuple(SA,reads)
    return getLink(SA,reads)

