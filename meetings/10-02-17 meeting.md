BS32011 Project A Meeting 3 Agenda (10/2/2017)
Attendees: David Martin, George Krontiris, Eleanor Adams, Roseanne Smith
Previous meeting discussion: David and Roseanne discussed using primer 3
Current meeting: Going over identification of primers again and discussed how to get a sequence into one line.
Next meeting: Use primer 3

Minutes:

We need to identify primer sequences for PCR. This is done using primer 3. 
Primer 3 is a web based interface.
We need to find primer that are common in both species. We need the primers to be around 200 bases on either side
of the restriction site that occurs in only one of the species.
In order for primer 3 to work the sequences must be saved on one line. 
We had prviously saved the sequences with new lines to make them easier to analyze.
We wrote a python script for this:
[Script to put sequence on one line](BS32011-class2017/toOneLine.py)

*split('\n') -gets rid of new lines
*[1:] -includes all lines other than the header

