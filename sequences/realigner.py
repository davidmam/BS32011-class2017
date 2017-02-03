# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

filename = '../multiple alignment/fox.fasta'
#ask the user for the number of bases to move from the start. Convert the text to an integer

# open the file to read in the sequence

fh = open(filename)

header = fh.readline().strip()
sequence = fh.read().replace('\n','')
fh.close()

restrict = 'jn711443.restrict'

fh = open(restrict)

ofh = open(restrict+'.txt', 'w')

line = fh.readline()

while line[:7] != '  Start':
    ofh.write(line)
    line = fh.readline()

ofh.write(line)

gapcount = 0

for line in fh.readlines():
    try:    
        fields = line.split()
        if len(fields) > 7:
            newgapcount = sequence[:int(fields[0]) + gapcount].count('-')
            while newgapcount > gapcount:
                gapcount = newgapcount
                newgapcount = sequence[:int(fields[0]) + gapcount].count('-')
            fields[0] = str(int(fields[0])+gapcount)
            fields[1] = str(int(fields[1])+gapcount)
            fields[5] = str(int(fields[5])+gapcount)
            fields[6] = str(int(fields[6])+gapcount)
            ofh.write('\t'.join(fields) + '\n')
        else:
            ofh.write(line)
    except:
        print('Error processing line '+line)
ofh.close()
fh.close()
