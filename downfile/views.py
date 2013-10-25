# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from utility import fetdata
from utility import readfile
from statistic import count

def index(request):
    print '999'
    return render(request, 'downfile/index.html')


def download(request):
    cladeVal = request.POST['clade']
    genomeVal = request.POST['genome']
    seqTypeVal = request.POST['seqType']
    #print clade + genome + seqType
    print cladeVal+"---"+genomeVal+"---"+seqTypeVal
    #fetdata.fetch_data_from_ucsc(clade = cladeVal, genome = genomeVal, seqType = seqTypeVal)
    fastaStr = readfile.readLocal('../statistic/fasta_test.txt')
    print count.fastaCount(fastaStr)
    return render(request, 'downfile/d3.html', {'arr' : count.fastaCount(fastaStr)})

def d3(request):
    return render(request,'downfile/d3.html')

