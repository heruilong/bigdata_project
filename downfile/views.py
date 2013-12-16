# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from utility import fetdata
from utility import readfile
from utility import ftp_download
from utility import mem
from statistic import count
from statistic import gc
from statistic import geneFormat
from statistic import assembly
from statistic import orf
from statistic import hamm
from statistic import edta
import os
def index(request):
    print '999'
    return render(request, 'downfile/index2.html')
'''
def download(request):
    cladeVal = request.POST['clade']
    genomeVal = request.POST['genome']
    seqTypeVal = request.POST['seqType']
    print cladeVal+"---"+genomeVal+"---"+seqTypeVal

    ftp_download.fetch_data_from_ucsc_ftp(clade = cladeVal, genome = genomeVal, seqType = seqTypeVal)
'''




def download(request):
    choice = request.POST['action']
    print "choice:"+ choice
    cladeVal = request.POST['clade']
    genomeVal = request.POST['genome']
    seqTypeVal = request.POST['seqType']
    fastqFile = request.POST['fastqFile']
    fastqLength = request.POST['fastqLength']
    print fastqFile
    print fastqLength
    if(choice == 'download'):
        print cladeVal+"---"+genomeVal+"---"+seqTypeVal
        #fetdata.fetch_data_from_ucsc(clade = cladeVal, genome = genomeVal, seqType = seqTypeVal)
        if(not os.path.exists(os.path.join("../../sequence/")+genomeVal+'-'+seqTypeVal+'.txt')):
    
            ftp_download.fetch_data_from_ucsc_ftp(clade = cladeVal, genome = genomeVal, seqType = seqTypeVal)
        return render(request, 'downfile/result.html',)
    elif(choice == 'ATCG_count'):
        print 'ATCG_count'
        webMC = mem.WebMC()
        key = str(genomeVal)+str(seqTypeVal)+'DNACount'
        value = webMC.mc.get(key)
        if value==None:
            '''
            #fetdata.fetch_data_from_ucsc(clade = cladeVal, genome = genomeVal, seqType = seqTypeVal)
        
            #ftp_download.fetch_data_from_ucsc_ftp(clade = cladeVal, genome = genomeVal, seqType = seqTypeVal)
	    fastaStr = readfile.readLocal('../../../sequence/'+genomeVal+'-'+seqTypeVal+'.txt')
	    fastaArr = geneFormat.decodeFasta(fastaStr)
	    value =  count.fastaCount(fastaArr)
            '''
            value = ATCG_count(genomeVal, seqTypeVal)
    	    #print gc.computingGC(fastaArr)
	    webMC.mc.set(key,value)
        return render(request, 'downfile/ACGT_count_result.html', {'arr' : value})
    elif(choice == 'chrs_length'):
        print 'chrs_length'
        webMC = mem.WebMC()
        key = str(genomeVal) + str(seqTypeVal) + 'chrs_length'
        value = webMC.mc.get(key)
        if value == None:
            value = chrs_length(genomeVal, seqTypeVal)
            webMC.mc.set(key, value)
        return render(request, 'downfile/chrs_len_result.html', {'arr': value})

    elif(choice == 'ATCG_percent'):
        print 'ATCG_percent'
        webMC = mem.WebMC()
        key = str(genomeVal) + str(seqTypeVal) + 'ATCG_percent'
        value = webMC.mc.get(key)
        if value == None:
            value = ATCG_percent(genomeVal, seqTypeVal)
            webMC.mc.set(key, value)
        return render(request, 'downfile/ACGT_count_result.html', {'arr': value})
    elif(choice == 'assembly'):
        print 'assembly'
        print 'begin assembly'       
        print fastqFile
        print fastqLength
        result = assembly_segments(fastqFile,int(fastqLength))
        if(len(result) <= 1):
            overlap = []
            segments = []
        else:       
            overlap = result[0]
            segments = result[1]
        #print segments
        #overlap1= [['a',1],['t',2]]
        #print overlap
        return render(request, 'downfile/suffix.html',{'arr':overlap, 'segments':segments})
    elif(choice == 'ATandCG_percent'):                           
        print 'ATandCG_percent'                                  
        webMC = mem.WebMC()                                   
        key = str(genomeVal) + str(seqTypeVal) + 'ATandCG_percent'
        value = webMC.mc.get(key)                             
        if value == None:                                     
            value = ATandCG_percent(genomeVal, seqTypeVal)       
            webMC.mc.set(key, value)                          
        return render(request, 'downfile/d3_result.html', {'arr': value})

    elif(choice == 'gc_content'):                                      
        print 'gc_content'
        webMC = mem.WebMC()
        key = str(genomeVal) + str(seqTypeVal) + 'gc_content'
        value = webMC.mc.get(key)
        #print value
        if value == None:
            value = gc_content(genomeVal, seqTypeVal)
            webMC.mc.set(key, value)
        return render(request, 'downfile/chrs_len_result.html', {'arr': value})
    elif(choice == 'protein_percent'):                                      
        print 'protein_percent'
        webMC = mem.WebMC()
        key = str(genomeVal) + str(seqTypeVal) + 'protein_percent'
        value = webMC.mc.get(key)
        if value == None:
            value = protein_percent(genomeVal, seqTypeVal)
            webMC.mc.set(key, value)
        return render(request, 'downfile/ACGT_count_result.html', {'arr': value})
    elif(choice == 'hamiltonDistance'):                                      
        print 'hamiltonDistance'
        value = hamiltonDistance(fastqFile, int(fastqLength))
        return render(request, 'downfile/chrs_len_result.html', {'arr': value})
    elif(choice == 'editDistance'):                                      
        print 'editDistance'
        value = editDistance(fastqFile, int(fastqLength))
        return render(request, 'downfile/chrs_len_result.html', {'arr': value})


def protein_percent(genomeVal='Human', seqTypeVal='genomic'):                    
    rltvPath = '../../../sequence/' + genomeVal + '-' + seqTypeVal + '.txt' 
    absPath = os.path.join(os.path.dirname(__file__), rltvPath)             
    value = orf.getOrfLen(absPath)                                              
    return value   

                   

def gc_content(genomeVal='Human', seqTypeVal='genomic'):
    rltvPath = '../../../sequence/' + genomeVal + '-' + seqTypeVal + '.txt'
    absPath = os.path.join(os.path.dirname(__file__), rltvPath)
    value = gc.getGCs(absPath)
    return value


def assembly_segments(filename='SRR062635', length=10):
    rltvPath = '../../../fastq/' + filename
    absPath = os.path.join(os.path.dirname(__file__), rltvPath)
    print absPath
    print length
    result = assembly.getAssembly(absPath, length)
    return result

def hamiltonDistance(filename='SRR062635', length=10):                
    rltvPath = '../../../fastq/' + filename                                 
    absPath = os.path.join(os.path.dirname(__file__), rltvPath)             
    result = hamm.getHamm(absPath, length)                          
    return result

def editDistance(filename='SRR062635', length=10):                                 
    rltvPath = '../../../fastq/' + filename                                 
    absPath = os.path.join(os.path.dirname(__file__), rltvPath)             
    result = edta.getDist(absPath, length)                                          
    return result                                                           
 

def ATCG_count(genomeVal='Human', seqTypeVal='genomic'):
    rltvPath = '../../../sequence/' + genomeVal + '-' + seqTypeVal + '.txt'
    absPath = os.path.join(os.path.dirname(__file__), rltvPath)
    count = 0
    countRes = [0,0,0,0]
    with open(absPath, 'r') as f:
        for line in f:
            if ">" in line:
                continue
            else:
                c_a = line.count('A') + line.count('a')
                c_c = line.count('C') + line.count('c')
                c_g = line.count('G') + line.count('g')
                c_t = line.count('T') + line.count('t')
                countRes[0] = countRes[0] + c_a
                countRes[1] = countRes[1] + c_c
                countRes[2] = countRes[2] + c_g
                countRes[3] = countRes[3] + c_t
    return countRes


def chrs_length(genomeVal='Human', seqTypeVal='genomic'):
    rltvPath = '../../../sequence/' + genomeVal + '-' + seqTypeVal + '.txt'
    #rltvPath = './'+genomeVal + '-' + seqTypeVal + '.txt'
    absPath = os.path.join(os.path.dirname(__file__), rltvPath)
    count = -1
    #countRes = [0,0,0,0]
    chrs = []
    length = 0
    with open(absPath, 'r') as f:
        for line in f:
            if ">" in line:
                #print count
                chrs.append(length)
                count = count + 1
                length = 0
            else:
                #print length
                chrs[count] = chrs[count] + len(line) - 1
    return chrs


def ATCG_percent(genomeVal='Human', seqTypeVal='genomic'):
    rltvPath = '../../../sequence/' + genomeVal + '-' + seqTypeVal + '.txt'
    #rltvPath = './' + genomeVal + '-' + seqTypeVal + '.txt'
    absPath = os.path.join(os.path.dirname(__file__), rltvPath)
    count = -1
    countRes = []
    temp = [0,0,0,0]
    with open(absPath, 'r') as f:
        for line in f:
            if ">" in line:
                temp = [ 0,0,0,0]
                countRes.append(temp)
                count = count + 1
            else:
                c_a = line.count('A') + line.count('a')
                c_c = line.count('C') + line.count('c')
                c_g = line.count('G') + line.count('g')
                c_t = line.count('T') + line.count('t')
                countRes[count][0] = countRes[count][0] + c_a
                countRes[count][1] = countRes[count][1] + c_c
                countRes[count][2] = countRes[count][2] + c_g
                countRes[count][3] = countRes[count][3] + c_t
    return countRes

def ATandCG_percent(genomeVal='Human', seqTypeVal='genomic'):
    rltvPath = '../../../sequence/' + genomeVal + '-' + seqTypeVal + '.txt'
    #rltvPath = './' + genomeVal + '-' + seqTypeVal + '.txt'
    absPath = os.path.join(os.path.dirname(__file__), rltvPath)
    count = -1
    total = 0
    countRes = [0,0]
    with open(absPath, 'r') as f:
        for line in f:
            if ">" in line:
                #temp = [ 0,0,0,0]
                #countRes.append(temp)
                count = count + 1
            else:
                c_a = line.count('A') + line.count('a')
                c_c = line.count('C') + line.count('c')
                c_g = line.count('G') + line.count('g')
                c_t = line.count('T') + line.count('t')
                countRes[0] = countRes[0] + c_a +c_t
                countRes[1] = countRes[1] + c_g +c_c
                total = total + c_a + c_t + c_g + c_c
                #countRes[2] = countRes[2] + c_g
                #countRes[3] = countRes[3] + c_t
    countRes[0] = countRes[0] / total
    countRes[1] = countRes[1] / total
    return countRes




def d3(request):
    return render(request,'downfile/d3.html')


def readLocal(rltvPath):
    absPath = os.path.join(os.path.dirname(__file__),rltvPath)
    f = open(absPath,'r')
    return f.read()

if __name__ == "__main__":
    ATCG_count('other', 'Sea hare')

'''
def download(request):
    cladeVal = request.POST['clade']
    genomeVal = request.POST['genome']
    seqTypeVal = request.POST['seqType']
    print cladeVal+"---"+genomeVal+"---"+seqTypeVal
    #fetdata.fetch_data_from_ucsc(clade = cladeVal, genome = genomeVal, seqType = seqTypeVal)
    
    ftp_download.fetch_data_from_ucsc_ftp(clade = cladeVal, genome = genomeVal, seqType = seqTypeVal)

    webMC = mem.WebMC()
    key = str(genomeVal)+str(seqTypeVal)+'DNACount'
    value = webMC.mc.get(key)
    if value==None:
        #fetdata.fetch_data_from_ucsc(clade = cladeVal, genome = genomeVal, seqType = seqTypeVal)
        
        ftp_download.fetch_data_from_ucsc_ftp(clade = cladeVal, genome = genomeVal, seqType = seqTypeVal)
	fastaStr = readfile.readLocal('../../../sequence/'+genomeVal+'-'+seqTypeVal+'.txt')
	fastaArr = geneFormat.decodeFasta(fastaStr)
	value =  count.fastaCount(fastaArr)
    	print gc.computingGC(fastaArr)
	webMC.mc.set(key,value)
	
    return render(request, 'downfile/d3.html', {'arr' : value})

def d3(request):
    return render(request,'downfile/d3.html')
'''
