
BS32011 Project A Meeting 4 Agenda (27/1/2017)
David Martin
George Krontiris
Eleanor Adams
Roseanne Smith 

Previous meeting: Aligning sequences on Jalview: Circular genomes may not have the same start and end point, as identified in Wildcat. We created a program to reallign the wildcat genome and this was uploaded onto github. AFter the meeting we met in the library to discuss using jalveiw. 
 
Current meeting: restriction analysis, by next week the presenter will provide 1-2 slides in the meeting to show progression.
Restriction enzyme classes: a) Cuts in site b) Cuts after/before site 
When comparing restriction sites between sequences, the unique ones are the ones that we care about.
Be careful with gaps in the alignment, the script must account for them.

For next week: Recalibrate position to add gaps
text.count(...)

*Moved to IT Suite D for computer use and used Xming to log in to life sciences server.

Adding -help after the command gives you the mandatory qualifiers.
history gives you all previous commands.
history > name.txt writes down your command history 

Used Xming to find restriction sites in our sequences as follows:

To make restrictions

1) programs, school of life sciences, general, xming (gets on to the life science server)
2) applications, general, terminal
3) mkdir "BS32011"
4) cd BS32011, git clone https://github.com/davidmam/BS32011-class2017.git
5) cd BS32011-class2017/sequences/
6) wossname restrict
7) restrict help (optional)
8) restrict
9) *filename*
10) more *restrict filename*
11) remember ls shows everything in directory 
12) git add 'filenames'
13) git commit -m 'message'
14) git pull
 <deal with any conflicts>
15) git push origin master

Notes for what things stand for:
In bases: N = A/T/G/C 
R = Purines A/G 
Y = Pyrimidines T/C 
S = Strongly bonded C-G 
W = Weakly bonded A-T 
K = C/A 
M = G/T
B = Not A 
D = Not C 
H = Not G 
v = Not T 
For next week: Count the gaps in the command prompt.
You can use the multiple alignment from jalview.
nano filename.txt is a text editor

