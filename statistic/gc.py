import sys

def computingGC(fastaArr):
	assert len(fastaArr)>0 and len(fastaArr)%2==0
        GCs = {}
        for i in xrange(0,len(fastaArr)/2):
		k,v = fastaArr[2*i],fastaArr[2*i+1]
		if len(v)==0: GCs[k] =0.0
                else: GCs[k] = 100.0*(v.count('C')+v.count('G'))/len(v)
	value = 0
        key = ''
        for (k,v) in GCs.items():
                if v>=value:
                        value=v
                        key=k
        
	if len(str(value))>9 : return key,str("%.6f"%value)
        else : return key,value

