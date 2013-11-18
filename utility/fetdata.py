'''
Created on 2013-11-18

@author: heruilong
'''
'''
Created on 2013-11-18

@author: heruilong
'''
import urllib
import urllib2
import webbrowser
import mechanize
import re
import os
def fetch_data_from_ucsc(clade ="mammal", genome="Human", seqType ="genomic"):
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
    
    url1 = "http://genome.ucsc.edu/cgi-bin/hgTables?hgsid="+hgsid+"&clade="+ clade +"&org=0&db=0&hgta_group=genes&hgta_track=xenoRefGene&hgta_table=xenoRefGene&hgta_regionType=genome&position=&hgta_outputType=sequence&hgta_outFileName="
    response2 = br.open(url1)
    #print response2.read()
    
    br.select_form(name="mainForm")
    br["hgta_outputType"] = ["sequence"]
    print "org:"
    print br["org"]
    br["org"] = [genome]
    
    br["clade"] = [clade]
    #print br["org"]
    response = br.submit(name="hgta_doTopSubmit")
    content =  response.read()

    #set mRNA | protein | DNA
    br.select_form(nr=0)
    print br['hgta_geneSeqType']
    br['hgta_geneSeqType'] = [seqType]
    response = br.submit()
    
    #last form
    br.select_form(nr = 0)
    response = br.submit(name="hgta_doGenomicDna")
    ''' 
    f= None 
    content = ""
    temp = response.readline()
    while(temp != 0):
        count = 1
        while(count < 1000000 and temp != 0):
            content = content + temp
            #content = response.read()
            count += 1
            temp = response.readline()
        print len(content)
         
        with open(os.path.join("../sequence/")+genome+"-"+seqType+".txt", "a") as f:
            f.write(content)
    '''
    f = None
    with open(os.path.join("../sequence/")+genome+"-"+seqType+".txt", "a") as f:
        for chunk in iter((lambda: response.read(4096)), ''):
            f.write(chunk)
        #    print "running"
        
   
    f.close()
    print "done"

if __name__ == "__main__":
    fetch_data_from_ucsc(clade="other", genome="S. cerevisiae", seqType="genomic")
    #fetch_data_from_ucsc()
