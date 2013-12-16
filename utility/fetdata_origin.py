'''
Created on 2013-10-13

@author: heruilong
'''
import urllib
import urllib2
import webbrowser
import mechanize
import re

def fetch_data_from_ucsc(clade ="mammal", genome="Human", seqType ="genomic"):
    br = mechanize.Browser()
    br.set_handle_robots(False) #ignore robots
    
    url = "http://genome.ucsc.edu/cgi-bin/hgTables?command=start"
    br.open(url)
    print "initial:"+br.geturl()
    br.select_form(name="hiddenForm")
    hgsid = br['hgsid']
    print "hgsid:"+ hgsid
   
    first_url = "http://genome.ucsc.edu/cgi-bin/hgTables"
    form0 = mechanize.HTMLForm('http://genome.ucsc.edu/cgi-bin/hgTables', method='Get')
    form0.new_control('hidden', 'hgsid',{'value':hgsid})
    form0.new_control('hidden', 'clade',{'value':''})
    form0.new_control('hidden', 'org',{'value':''})
    form0.new_control('hidden', 'db',{'value':''})
    form0.new_control('hidden', 'dbhgta_group',{'value':''})
    form0.new_control('hidden', 'hgta_track',{'value':''})
    form0.new_control('hidden', 'hgta_table',{'value':''})
    form0.new_control('hidden', 'hgta_regionType',{'value':''})
    form0.new_control('hidden', 'position',{'value':''})    
    form0.new_control('hidden', 'hgta_outputType',{'value':''})
    form0.new_control('hidden', 'hgta_outFileName',{'value':''})    
    form0.fixup()
    br.form = form0
    response = br.submit()
    content= response.read()
    print response.geturl()
        
    url2 ="http://genome.ucsc.edu/cgi-bin/hgTables?hgsid="+hgsid+"&clade="+clade+"&org="+genome.replace(' ', '+')+"&db=0&hgta_group=genes&hgta_track=xenoRefGene&hgta_table=xenoRefGene&hgta_regionType=genome&position=&hgta_outputType=sequence&hgta_outFileName="

    br.open(url2)
    
    br.select_form(name="mainForm")
    br["hgta_outputType"] = ["sequence"]
    print "org:"
    print br["org"]
    br["org"] = [genome]
    
    br["clade"] = [clade]
    print br["org"]
    response = br.submit(name="hgta_doTopSubmit")
    
    content= response.read()
    with open("mechanize_results1.html", "w") as f:
        f.write(content)
    print response.geturl()
    
    
    form1 = mechanize.HTMLForm('http://genome.ucsc.edu/cgi-bin/hgTables', method='Get')
    form1.new_control('hidden', 'hgsid',{'value':hgsid})
    form1.new_control('radio', 'hgta_geneSeqType',{'value':'genomic', 'checked':'checked'})
    form1.new_control('radio', 'hgta_geneSeqType',{'value':'protein'})
    form1.new_control('radio', 'hgta_geneSeqType',{'value':'mRNA'})
    
    
    form1.new_control('submit', 'hgta_doGenePredSequence',{'value':'submit'})
    form1.fixup()
    br.form = form1
    #form1.find_control("hgsid").readonly = False
    #br['hgsid'] = '349632407'
    br.form['hgta_geneSeqType'] = [seqType]
    if(seqType == "mRNA" or seqType == "protein"):
        response = br.submit()
        content= response.read()
        with open(genome+"-"+seqType+".txt", "w") as f:
            f.write(content)
    else:
        response = br.submit()
        content= response.read()
        with open("mechanize_results2.html", "w") as f:
            f.write(content)
        
        url = "http://genome.ucsc.edu/cgi-bin/hgTables?hgsid="+hgsid+"&hgta_geneSeqType=genomic&hgta_doGenePredSequence=submit"    
        #form2 = mechanize.HTMLForm('http://genome.ucsc.edu/cgi-bin/hgTables', method='Get')
        form2 = mechanize.HTMLForm(url, method='Get')
        form2.new_control('hidden', 'hgsid',{'value':hgsid})    
        form2.new_control('checkbox', 'hgSeq.promoter',{'value':'on'})    
        form2.new_control('hidden', 'boolshad.hgSeq.promoter',{'value':'0'})
        form2.new_control('text', 'hgSeq.promoterSize',{'value':'1000'})
        form2.new_control('checkbox', 'hgSeq.utrExon5',{'value':'on', 'checked':'checked'})
        form2.new_control('hidden', 'boolshad.hgSeq.utrExon5',{'value':'0'}) 
        form2.new_control('checkbox', 'hgSeq.cdsExon',{'value':'on'})
        form2.new_control('hidden', 'boolshad.hgSeq.cdsExon',{'value':'0'})
        form2.new_control('checkbox', 'hgSeq.utrExon3',{'value':'on'})
        form2.new_control('hidden', 'boolshad.hgSeq.utrExon3',{'value':'0'})
        form2.new_control('checkbox', 'hgSeq.intron',{'value':'on'})
        form2.new_control('hidden', 'boolshad.hgSeq.intron',{'value':'0'})
        form2.new_control('checkbox', 'hgSeq.downstream',{'value':'on'})
        form2.new_control('hidden', 'boolshad.hgSeq.downstream',{'value':'0'})
        form2.new_control('text', 'hgSeq.downstreamSize',{'value':'1000'})
        form2.new_control('radio', 'hgSeq.granularity',{'value':'gene','checked':'checked'})
        form2.new_control('radio', 'hgSeq.granularity',{'value':'feature'})
        form2.new_control('text', 'hgSeq.padding5',{'value':'0'})
        form2.new_control('text', 'hgSeq.padding3',{'value':'0'})
        form2.new_control('checkbox', 'hgSeq.splitCDSUTR',{'value':'on'})
        form2.new_control('hidden', 'boolshad.hgSeq.splitCDSUTR',{'value':'0'})
        form2.new_control('radio', 'hgSeq.casing',{'value':'exon', 'checked':'checked'})    
        form2.new_control('radio', 'hgSeq.casing',{'value':'cds'})    
        form2.new_control('radio', 'hgSeq.casing',{'value':'upper'})    
        form2.new_control('radio', 'hgSeq.casing',{'value':'lower'})    
        form2.new_control('checkbox', 'hgSeq.maskRepeats',{'value':'on'})
        form2.new_control('hidden', 'boolshad.hgSeq.maskRepeats',{'value':'0'})
        form2.new_control('radio', 'hgSeq.repMasking',{'value':'lower','checked':'checked'})
        form2.new_control('radio', 'hgSeq.repMasking',{'value':'N'})
        form2.new_control('submit', 'hgta_doGenomicDna',{'value':'get sequence'})    
        form2.fixup()    
        br.form = form2
        response = br.submit(name='hgta_doGenomicDna')
        content= response.read()
        with open("./sequence/"+genome+"-"+seqType+".txt", "w") as f:
            f.write(content)    

    
def add_select_to_form(form, name, attrs, options):
    form.new_control('select', name, attrs={'__select': attrs})
    for idx, option in enumerate(options):
        value, description, selected = option
        new_attrs = {
            '__select': attrs,
            'value': value,
            'contents': description,
            }
        if selected:
            new_attrs['selected'] = 'selected'
        form.new_control('select', name, attrs=new_attrs, index=idx)
    
  
if __name__ == "__main__":
   fetch_data_from_ucsc(clade="other", genome="S. cerevisiae", seqType="genomic")

    
    
    
    
    
   
    
    
    
    
    
    
    
