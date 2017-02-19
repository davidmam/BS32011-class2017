BS32011 Project A Lab Meeting (3/2/2017)
Attendees: David Martin, George Krontiris, Eleanor Adams, Roseanne Smith
Previous meeting discussion: Created a script on Python that rewrites positions to include gaps.
Current meeting: Worked with David to create a python script that would identify infrequent cutters
Next meeting: Look at identification of primers using primer 3

We need to be able to create a script that will be able to identify which resctictions are present in one sequence but not the other.
This would allow us to perform a cut on one species and not the other when the enzyme is used.
Then, by identifying primers and carrying out a PCR reaction we would be able to preform an electrophoresis.
This would allow us to identify between the species using only the mitochondrial DNA.

There was a problem with the previous script (rewriting positions with gaps) when run from the sequences folder not multiple alignment.
sitefinder.py got rid of roughly 3/4 restriction sites.
Candidate sites need to be selected by finding infrequent cutters and checking in Jalview if there is a suitable gap.

[Restriction site finder](BS32011-class2017/sequences/sitefinder.py)

