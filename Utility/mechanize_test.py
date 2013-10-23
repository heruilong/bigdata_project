'''
Created on 2013-10-13

@author: heruilong
'''
import urllib
import urllib2
import webbrowser
import mechanize


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


url = "http://localhost:8080/hrl_fun"
br = mechanize.Browser()
br.set_handle_robots(False) #ignore robots
br.open(url)
#br.select_form(name="form1")
#br["language"] = ["python"]
form2 = mechanize.HTMLForm('http://localhost:8080/hrl_fun/jsp_pages/process.jsp', method='post')
select_options = [
    ('10', '10 second', 0),
    ('300', '5 minutes', 1),
    ('86400', '1 day', 0),
    ]
select_attrs = {
    'id': 'some_id'}
add_select_to_form(form2, 'language', select_attrs, select_options)

form2.new_control('radio', 'hgta_geneSeqType', {'value':'fox000'})  
form2.new_control('radio', 'hgta_geneSeqType', {'value':'fire', 'checked':'checked'})    
form2.new_control('radio', 'hgta_geneSeqType', {'value':'fox'})    


form2.new_control('submit', 'submit',{'value':''})    
form2.fixup()

br.form = form2
print br['language']
#br['hgta_geneSeqType'] = ['fox']
print br['hgta_geneSeqType']
response = br.submit()
content= response.read()
with open("mechanize_results.html", "w") as f:
    f.write(content)
    
