BS32011 Project A Meeting 3 Agenda (14/2/2017)
Attendees: David Martin, George Krontiris, Eleanor Adams, Roseanne Smith
Previous meeting discussion: Going over identification of primers again and discussed how to get a sequence into one line.
Current meeting: Using primer 3 to identify primers and visulaise using snapgene. Checked presence of primers of jalview. 
Next meeting: Look at possible primers and decide which will be most appropriate.

Minutes:

When using primer3 we get a variety of feilds we can edit.
We edited file of infrequent cutters into a table for easier analysis. 
We needed to use an enzyme that a cut site is present in one sequence and not the other.
Cuts must be infrequent and far enough apart so as not to interfere with each other: The restrict sites for the enzyme need to be reasonably spaced, eg 700 bases
After idtenifying an appropiate restriction site we looked at the retriction files to identify where on the seuqence it appears.
We want the target on primer3 to be 200 either side of the restriction site
We must remeber to canvert the gapped restriction site base number to the ungapped before putting into primer
We used the example primer input:
Nano primer3inputexample.txt   example primer file
Sequence ID – what are we calling it?
Opt primer size = 20
Between 400 and 800 bases for the whole section of sequence- we hope it cuts in the middle

Primer 3_core –o weaselexample.out primer3weaseExample.txt  –runs the programme
More weaselExample.out 
Several sets of primers will come back- need to look at these and decide if we think they are good, bad, indifferent 
– look at the parameters- do they have self hybridisation? Not very useful if they do as will bind to themselves rather than the template

Quick way of deleting a line in nano is ctrl k
Ctrl r to read a file in 
Can look on snapgene viewer to see where the restriction sites and primers are
Can choose enzymes from drop down menu on snapveiwer- shows us the cut sites- going back to the map will show the pattern where it vuts
Need to find a pair of primers and an ezyme that will give us a fragment in both species but will only cleave in 1
Find the primers common in both species, go to jalview – use the find option, copy sequence of primer from primer 3 git bash
In snapgene can import primers




