import sys
import re

def dnaformat(dna):
	dna = dna.upper()
	dna_re = re.compile('\W')
	dna = dna_re.sub('',dna)
	return dna

def rnaformat(rna):
	return dnaformat(rna)

def decodeFasta(fasta):
	datas = fasta.split('\n')
	res = []
	dna = ""
	for data in datas:
		if ">" in data : 
			if len(dna)>0: res.append(dna)
			dna= ""
			res.append(data)
		else : dna += data
	if len(dna)>0: res.append(dna)
	return res

def codon(code):
	assert len(code)==3
	if code=='UUU' or code=='UUC': return 'F'
	elif code=='UUA' or code=='UUG': return 'L'
	elif code=='CUU' or code=='CUC' or code=='CUA' or code=='CUG': return 'L'
	elif code=='AUU' or code=='AUC' or code=='AUA': return 'I'  
	elif code=='AUG': return 'M'
	elif code=='GUU' or code=='GUC' or code=='GUA' or code=='GUG': return 'V'  
	elif code=='UCU' or code=='UCC' or code=='UCA' or code=='UCG': return 'S'
	elif code=='CCU' or code=='CCC' or code=='CCA' or code=='CCG': return 'P'
	elif code=='ACU' or code=='ACC' or code=='ACA' or code=='ACG': return 'T'
	elif code=='GCU' or code=='GCC' or code=='GCA' or code=='GCG': return 'A'
	elif code=='UAU' or code=='UAC': return 'Y'
	elif code=='UAA' or code=='UAG': return '.'
	elif code=='CAU' or code=='CAC': return 'H'
	elif code=='CAA' or code=='CAG': return 'Q'
	elif code=='AAU' or code=='AAC': return 'N'
	elif code=='AAA' or code=='AAG': return 'K'
	elif code=='GAU' or code=='GAC': return 'D'
	elif code=='GAA' or code=='GAG': return 'E'
	elif code=='UGU' or code=='UGC': return 'C'
	elif code=='UGA': return '.'
	elif code=='UGG': return 'W'
	elif code=='CGU' or code=='CGC' or code=='CGA' or code=='CGG': return 'R'
	elif code=='AGU' or code=='AGC': return 'S'
	elif code=='AGA' or code=='AGG': return 'R'
	elif code=='GGU' or code=='GGC' or code=='GGA' or code=='GGG': return 'G'
	else : return "'Wrong here'"	

def translate(rna):
	prot=''
	for i in range(0,len(rna)/3):
		prot += codon(rna[i*3:i*3+3:])
	return prot

def transcript(dna):
	return dna.replace('T','U').replace('t','u')
