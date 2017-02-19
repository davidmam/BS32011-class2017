
AGENDA:

Date: 31/01/17
Time: 12 noon
Location: Carnelley C2.20
Attendees: David Martin, Eleanor Adams (secretary), George Krontiris (presenter), Roseanne Smith (chair)

Previous meeting: Used Xming to create restriction maps.

Current meeting: Created a script on Python that rewrites positions to include gaps.

Next meeting: Compare alignments for restriction sites present in both or unique to one.

Minutes: 

George and Ellie had problems with git crashing when trying to create restriction sites on Xming.
David showed us how to correct this by using git-config global. 
Our current FASTA sequences did not include the gaps that are created when the multiple alignment was done.
This meeting David showed us how to include the gaps from the multiple alignement in our current sequences.
This was done using sypder python. 

[Python script to add gaps to sequence using multiple alignment](sequences/realigner.py)

Before next meeting we are going to attempt to add gaps to our own sequences. 
