# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from utility import fetdata

def index(request):
    print '999'
    return render(request, 'downfile/index.html');


def download(request):
    cladeVal = request.POST['clade']
    genomeVal = request.POST['genome']
    seqTypeVal = request.POST['seqType']
    #print clade + genome + seqType
    print cladeVal+"---"+genomeVal+"---"+seqTypeVal
    #fetdata.fetch_data_from_ucsc(clade = cladeVal, genome = genomeVal, seqType = seqTypeVal)
    return HttpResponse("hellworld----")