# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from utility import fetdata
from utility import readfile
from utility import mem
from statistic import count
from statistic import gc
from statistic import geneFormat

def index(request):
    print '999'
    return render(request, 'downfile/index.html')


def download(request):
    cladeVal = request.POST['clade']
    genomeVal = request.POST['genome']
    seqTypeVal = request.POST['seqType']
    print cladeVal+"---"+genomeVal+"---"+seqTypeVal
    #fetdata.fetch_data_from_ucsc(clade = cladeVal, genome = genomeVal, seqType = seqTypeVal)
    webMC = mem.WebMC()
    key = str(genomeVal)+str(seqTypeVal)+'DNACount'
    value = webMC.mc.get(key)
    if value==None:
        fetdata.fetch_data_from_ucsc(clade = cladeVal, genome = genomeVal, seqType = seqTypeVal)
	fastaStr = readfile.readLocal('../../sequence/'+genomeVal+'-'+seqTypeVal+'.txt')
	fastaArr = geneFormat.decodeFasta(fastaStr)
	value =  count.fastaCount(fastaArr)
    	print gc.computingGC(fastaArr)
	webMC.mc.set(key,value)
	
    return render(request, 'downfile/d3.html', {'arr' : value})

def d3(request):
    return render(request,'downfile/d3.html')

