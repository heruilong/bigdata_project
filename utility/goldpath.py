'''
Created on 2013-11-19

@author: heruilong
'''
import urllib
import urllib2
import webbrowser
import mechanize
import re
import os
import gzip
def fetch_data_from_ucsc(clade ="mammal", genome="Human", seqType ="genomic"):
    br = mechanize.Browser()
    br.set_handle_robots(False) #ignore robots
    
    br.addheaders = [("UserAgent","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"), 
                 ("Accept-Encoding" , "gzip, deflate"),
                 ("Accept" , "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
                 ("Accept-Language" , "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3"),
                 ("Connection" , "keep-alive"),
                 ("Referer", "http://genome.ucsc.edu/")]
    url = "http://hgdownload.soe.ucsc.edu/goldenPath/sacCer3/bigZips/chromFa.tar.gz"
    response1 = br.open(url)
    f = None
    with open(os.path.join("../../sequence/")+"chromFa"+".tar.gz", "w") as f:
        #for chunk in iter((lambda: response.read(4096000)), ''):
            f.write(response1.read())
            #print chunk
        
   
    f.close()
    print "done"

    handle = gzip.open(os.path.join("../../sequence/")+"chromFa"+".tar.gz", 'w')
    #with open(os.path.join("../../sequence/")+"chromFa"+".tar.gz", 'w') as out:
    for line in handle:
        print line
    handle.close()
    print "finish"

if __name__ == "__main__":
    fetch_data_from_ucsc(clade="other", genome="S. cerevisiae", seqType="genomic")
    #fetch_data_from_ucsc()