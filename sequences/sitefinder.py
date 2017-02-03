# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 16:40:11 2017

@author: David
"""

filea = 'jn711443.restrict.txt'
fileb = 'nc_028310.restrict.txt'

maxcuts = 5

fha = open(filea)
fhb = open(fileb)

ofha = open(filea+'.out', 'w')
ofhb = open(fileb+'.out', 'w')

def getline(fh):
    line=fh.readline()
    fields = line.split()
    return fields
    
linea = getline(fha)

while not linea or linea[0] != 'Start':
    linea = getline(fha)

lineb = getline(fhb)

while not lineb or lineb[0] != 'Start':
    lineb = getline(fhb)

linea = getline(fha)
lineb = getline(fhb)

sitecounta = {}
sitecountb = {}

while linea and lineb:
    if linea[0] == lineb[0]:
        sitecounta[linea[3]] = sitecounta.get(linea[3],0) +1
        sitecountb[lineb[3]] = sitecountb.get(lineb[3],0) +1
        linea = getline(fha)
        lineb = getline(fhb)
    elif linea[0] < lineb[0]: #found A
        ofha.write('\t'.join(linea)+'\n')
        sitecounta[linea[3]] = sitecounta.get(linea[3],0) +1
        linea = getline(fha)
    else:
        ofhb.write('\t'.join(lineb)+'\n')
        sitecountb[lineb[3]] = sitecountb.get(lineb[3],0) +1
        lineb = getline(fhb)

fha.close()
fhb.close()
ofha.close()
ofhb.close()

enz = set( [ x for x in sitecounta.keys() if sitecounta[x] < 5] +  
[ x for x in sitecountb.keys() if sitecountb[x] < 5])

print('infrequent unique cutters = '+str(enz))