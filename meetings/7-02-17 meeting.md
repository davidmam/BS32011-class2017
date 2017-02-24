BS32011 Project A Lab Meeting (7/02/2017)
Attendees: David Martin, Roseanne Smith
Previous meeting discussion: Created a python script that would identify infrequent cutters
Current meeting: Discuss using primer 3.
Next meeting: Primer 3 with whole lab group

George and Ellie did not attend this meeting. Roseanne and David discussed using primer 3.

An introduction to Primer3 to search for primers. This requires an input file (primer3inputexample.txt) to generate an output file (primer3outputexample.txt). Target refers to around restriction site and is of the form (start,length). Left is forward, right is reverse and internal should be set to 0. Product size is in the range 200-800 so it is easily seen on a gel when separated. primer3_core, use nanos to paste input file, error if blank lines. Rewrite using Python:
fh=open(sequences/reddeer.fasta)
fh.readline()
oneline=fh.read().replace(‘\n’, ‘ ‘)
len/(oneline)
open(‘seqoneline.txt, ‘w’).write(oneline)
nanoprimer
SEQUENCE_TEMPLATE = ctrl r seqoneline.txt
SEQUENCE_TARGET= (8000,200)
PRIMER_PRODUCT_SIZE_RANGE=200-800
sequence tags=individual focus on global=min, max, tm, optsize.  Check melting temperature is consistent among species.
