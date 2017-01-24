# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 12:20:48 2017

@author: David
"""

# ask the user for the file to change. Store the filename in 'filename'
filename = input('Enter the filename to change: ')

#ask the user for the number of bases to move from the start. Convert the text to an integer
bases = int(input('how many bases to move from the start to the end?: '))

# open the file to read in the sequence

fh = open(filename)

header = fh.readline().strip()
sequence = fh.read().replace('\n','')
fh.close()

print('length of sequence is ', len(sequence))
print(header)

# python counts letters starting at 0
# index is [start from here : up to but not including this one]
newsequence = sequence[bases:]+sequence[:bases]

ofh  = open(filename+'.edited','w')
print(header, 'edited join[{bases}-end, start-{bases}]'.format(bases=bases), file=ofh)
#range gives a list of numbers range(start, end, step)
# for will assign pos to each member of the list in turn and run the code.
for pos in range(0,len(newsequence),60):
    if len(newsequence)- pos > 60:
        print(newsequence[pos: pos+60], file=ofh)
    else:
        print(newsequence[pos:], file=ofh)

ofh.close()