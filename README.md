bigdata_project
===============

jjjjjj


'''
Created on 2013-11-19

@author: heruilong
'''
import ftplib 
import urllib
import urllib2
import webbrowser
import mechanize
import re
import os
import gzip
import zipfile
import tarfile
def fetch_data_from_ucsc_ftp(clade ="mammal", genome="Human", seqType ="genomic"): 
    genome = genome.replace(' ', "%20")   
    br = mechanize.Browser()
    br.set_handle_robots(False) #ignore robots
    
    br.addheaders = [("UserAgent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"), 
                 ("Accept-Encoding" , "gzip, deflate"),
                 ("Accept" , "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
                 ("Accept-Language" , "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3"),
                 ("Connection" , "keep-alive"),
                 ("Referer", "http://genome.ucsc.edu/")]
    url = "http://genome.ucsc.edu/cgi-bin/hgTables?command=start"
    response1 = br.open(url)
    br.select_form(name="hiddenForm")
    hgsid = br['hgsid']
    
    print clade
    print genome
    url1 = "http://genome.ucsc.edu/cgi-bin/hgTables?hgsid="+hgsid+"&clade="+ clade +"&org="+genome+"&db=0&hgta_group=genes&hgta_track=xenoRefGene&hgta_table=xenoRefGene&hgta_regionType=genome&position=&hgta_outputType=sequence&hgta_outFileName="
    response2 = br.open(url1)
    genome = genome.replace("%20", " ")
    br.select_form(name="mainForm")
    db_select = br['db']
    db_option = db_select[0]
    
    print db_option

    
    if(seqType == "genomic"):
        getDNA(genome, seqType,db_option)
    elif(seqType == "mRNA"):
        getmRNA(genome, seqType,db_option)
    
    
    '''
    genome = genome.replace("%20", " ")
    save_name = genome+"-"+seqType+ ".gz"
    filename1 = db_option + ".fa.gz"
    #filename1 = "aplCal1" + ".fa.gz"
    filename2 = "chromFa.tar.gz"
    ftp = ftplib.FTP("hgdownload.cse.ucsc.edu")
    ftp.login("", "")
    ftp.cwd("/goldenPath/"+ db_option +"/bigZips/")
    #ftp.cwd("/goldenPath/"+ "aplcal1" +"/bigZips/")

    f1 = open(save_name, 'ab')
    try:
        print "try 1"
        ftp.retrbinary("RETR " + filename1 ,f1.write)
    except:
        print "1 Error"
    
    try:
        print "try 2"
        ftp.retrbinary("RETR " + filename2 ,f1.write)
    except:
        print "2 Error"
    f1.close()
    '''
    unzip_and_write(genome,seqType)
    print "done"
    

def getDNA(genome="Human", seqType="genomic", db_option="hg19"): 
    ftp = ftplib.FTP("hgdownload.cse.ucsc.edu")
    ftp.login("", "")
    ftp.cwd("/goldenPath/"+ db_option +"/bigZips/")
    
    #genome = genome.replace("%20", " ")
    save_name1 = genome+"-"+seqType+ ".gz"
    save_name2 = genome+"-"+seqType+ ".tar.gz"
    filename1 = db_option + ".fa.gz"
    #filename1 = "aplCal1" + ".fa.gz"
    filename2 = "chromFa.tar.gz"
    file_path = get_file_path()
    #ftp.cwd("/goldenPath/"+ "aplcal1" +"/bigZips/")

    if filename1 in ftp.nlst():
        print "gz"
        f1 = open(file_path +save_name1, 'ab')
        try:
            ftp.retrbinary("RETR " + filename1 ,f1.write)
        except:
            print "download gz Error"
    elif filename2 in ftp.nlst():
        print "tar.gz"
        f1 = open(get_file_path()+save_name2, 'ab')
        try:
            ftp.retrbinary("RETR " + filename2 ,f1.write)
        except:
            print "download tar.gz Error"   
    f1.close()     
    
    '''
    f1 = open(get_file_path()+save_name2, 'ab')
    try:
        print "try 2"
        ftp.retrbinary("RETR " + filename2 ,f1.write)
    except:
        print "2 Error"
    f1.close()
    '''
def getmRNA(genome="Human", seqType="mRNA", db_option="hg19"):
    ftp = ftplib.FTP("hgdownload.cse.ucsc.edu")
    ftp.login("", "")
    ftp.cwd("/goldenPath/"+ db_option +"/bigZips/")
    
    genome = genome.replace("%20", " ")
    save_name = genome+"-"+seqType+ ".gz"
    filename = "mrna.fa.gz"
    #filename1 = "aplCal1" + ".fa.gz"
    #ftp.cwd("/goldenPath/"+ "aplcal1" +"/bigZips/")

    f1 = open(get_file_path()+save_name, 'ab')
    try:
        print "try 1"
        ftp.retrbinary("RETR " + filename ,f1.write)
    except:
        print "1 Error"
    
    f1.close()
    

    
def unzip_and_write(genome="Human", seqType="genomic"):
    path = get_file_path()
    tar_filename = genome+"-"+seqType+".tar.gz"
    if os.path.exists(path+tar_filename):
        unzip_tar_file(genome, seqType)
    else:
        unzip_gz_file(genome, seqType)
    '''
    f1 = gzip.open(file_path+gz_filename, 'rb')
    f2 = None
    with open(get_file_path()+txt_filename, "w") as f2:
        for chunk in iter((lambda: f1.read(4096)), ''):
            f2.write(chunk)
    f1.close()
    f2.close()
    '''

    print "unzip done"
    
def unzip_gz_file(genome="Human", seqType="genomic"):
    gz_filename = genome+"-"+seqType+ ".gz"
    txt_filename = genome+"-"+seqType+ ".txt"
    file_path = get_file_path()
    f1 = gzip.open(file_path+gz_filename, 'rb')

    with open(file_path+txt_filename, "w") as f2:
        for chunk in iter((lambda: f1.read(4096)), ''):
            f2.write(chunk)
    f1.close()
    f2.close()

def unzip_tar_file(genome="Human", seqType="genomic"):
    tar_gz_filename = genome+"-"+seqType+ ".tar.gz"
    txt_filename = genome+"-"+seqType+ ".txt"
    file_path = get_file_path()
    tar = tarfile.open(file_path+tar_gz_filename, "r:gz")
    '''
    for tarinfo in tar:
        print tarinfo.name, "is", tarinfo.size, "bytes in size and is",
        if tarinfo.isreg():
            print "a regular file."
        elif tarinfo.isdir():
            print "a directory."
        else:
            print "something else."
    '''
    f1 = open(file_path+txt_filename, "a")
    for member in tar.getmembers():
        f=tar.extractfile(member)
        content=f.read()
        f1.write(content)
    f1.close()
    tar.close()

def get_file_path():
    path = os.path.join("../../sequence/")
    if not os.path.exists(path):
        os.makedirs(path)
    return path

if __name__ == "__main__":
    fetch_data_from_ucsc_ftp(clade="vertebrate", genome="Chicken", seqType="genomic")
    #fetch_data_from_ucsc()
    #S. cerevisiae other Sea hare
    #unzip_gz_file(genome="Chicken", seqType="genomic")
