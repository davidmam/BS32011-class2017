# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 16:40:11 2017

@author: David
"""

filea = 'Weasel2.restrict.txt'
fileb = 'Ferret.restrict.txt'

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
sitecountboth={}
while linea and lineb:
    if linea[0] == lineb[0]:
        sitecountboth[linea[3]] = sitecountboth.get(linea[3],0) +1
        #sitecountb[lineb[3]] = sitecountb.get(lineb[3],0) +1
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

enz = set( [ x for x in sitecounta.keys() if sitecounta[x] < maxcuts] +  
[ x for x in sitecountb.keys() if sitecountb[x] < maxcuts])

sites=[]
for x in set(list(sitecounta.keys())+ list(sitecountb.keys())+ list(sitecountboth.keys())):
    sites.append([x,sitecounta.get(x,0), sitecountb.get(x,0),sitecountboth.get(x,0)])

efh=open('enzymes.out','w')
for r in sorted(sites, key = lambda x: sum(x[1:3])):
    print(r, file=efh)
efh.close()
print('infrequent unique cutters = '+str(enz))