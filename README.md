
# Class Notes for BS32011 - 2017

This repository is the shared repository for class notes and code. The project overview is at https://github.com/davidmam/BS32011-2015 

## Sequences


| Common name | Scientific name | Sequence ID | Fasta File |
|---|---|---|---|
| Red Deer | _Cervus elaphus_ | AB245427 | [FASTA](sequences/reddeer.fasta) [Genbank](sequences/reddeer.gb) |
| Mountain Hare | _Lepus timidus_ | KR019013 | [FASTA](sequences/mountainhare.fasta) [Genbank](sequences/mountainhare.gb) |
| Ferret | _Mustela nigripes_ | NC_024942 | [FASTA](sequences/NC_024942.fasta) [Genbank](sequences/NC_024942.gb) |
| Weasel | _Mustela altaica_ | NC_021751 | [FASTA](sequences/Weasel.fasta) [Genbank](sequences/Weasel.gb) |
| Wildcat | _Felis silvestris_ | NC_028310 | [FASTA](sequences/NC_028310_wildcat.fasta) [Genbank](sequences/NC_028310_wildcat.gb) |
| Wildcat edited | _Felis silvestris_ | NC_028310 | [FASTA](sequences/NC_028310_wildcat_edited.fasta)  [Genbank] |
| Red fox | _Vulpes vulpes_ | JN711443 | [FASTA](sequences/JN711443_redfox.fasta) [Genbank](sequences/JN711443_redfox.gb) |


## Useful info

You can find a page of useful info for Git [here](git_info.md)

## Lab meetings

| Lab meeting date | 
|---|
|[Friday 20th January](meetings/20-01-17 meeting.md)|
|[Tuesday 24th January](meetings/24-01-17 meeting.md)|
|[Friday 27th January](meetings/27-01-17 meeting.md)|
|[Tuesday 31st January](meetings/31-01-17 meeting.md)|
|[Friday 3rd Febuary](meetings/3-02-17 meeting.md)|
|[Tuesday 7th Febuary](meetings/7-02-17 meeting.md)|
|[Friday 10th Febuary](meetings/10-02-17 meeting.md)|
|[Tuesday 14th Febuary](meetings/14-02-17 meeting.md)|


## Realignment of circular sequences 

[Python Script](sequences/sequencerealigner.py)

Wildcat was the only seqence that needed realligned:
[Wildcat Realigned Sequence](sequences/NC_028310_wildcat_edited.fasta)

##Restriction files

| Common name | Restriction File |
|---|---|
|Wildcat | [Restriction](sequences/nc_028310.restrict) |
|Red Fox | [Restriction](sequences/jn711443.restrict ) |
|Mountain hare | [Restriction](sequences/kr019013.restrict) |
|Red deer | [Restriction](sequences/ab245427.restrict ) |

##Restriction files with gaps 

| Common name | Gapped Restriction File |
|---|---|
|Wildcat | [Gapped Restriction](Restrictions with gaps/nc_028310_wildcat.txt) |
|Red Fox | [Gapped Restriction](Restrictions with gaps/jn711443_redfox.txt) |
|Mountain hare | [Gapped Restriction](Restrictions with gaps/kr019013_mountainhare.txt) |
|Red Deer | [Gapped Restriction](Restrictions with gaps/AB245427_reddeer.txt) |

##Infrequent cutters

[Wildcat and Red Fox](sequences/wildcat_redfox_enzymes.out )

[Mountain hare and Red deer](sequences/mountainhare_reddeer_enzymes.out )


#Sequences into one line

| Common name | One line file |
|---|---|
|Wildcat | [One line](sequences/NC_028310_wildcat_edited.fasta.one.txt ) |
|Red Fox | [one line](sequences/JN711443_redfox.fasta.one.txt  ) |
|Mountain hare | [one line](sequences/mountainhare.fasta.one.txt  ) |
|Red deer | [one line](sequences/reddeer.fasta.one.txt  ) |
##Chosen primers

| Name | Enzyme | Cuts | File containing possible primers |
|---|---|---|---|
|Wildcat and Red Fox |BseYI | Wildcat but not Red Fox | [Primers](sequences/primers for red fox and wildcat 1.txt) |
|Wildcat and Red Fox |DinI | Red Fox but not Wildcat | [Primers](sequences/primers for red fox and wildcat 2.txt) |


