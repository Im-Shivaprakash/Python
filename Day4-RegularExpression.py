'''
Regular Expression

re - inbuilt module
'import re'

4 important functions:

    -findall
    - search
    - split
    - sub

meta character - special meaning
. - any character
\ - used in special sequence
^ - to check the start of the string
$ - to check the end
+ - one or more occurance
* - zero or more occurance
{} - to specify number of occurance
| - either of thr re's
[] - set of characters

special sequence 
\d - digits - 0-9
\D - non digits
\s - white space characters - \n,\t space
\S - non white space characters
\w - word character - alphabets,digits,underscore
\W - non word character 

'''


'''
import re
s = "Life is beautiful!!!"
sre = "is"
l = re.findall(sre, s)
print(l)

ifre = "if"
l = re.findall(ifre, s)
print(l)

ire = "i."
l = re.findall(ire, s)
print(l)

sre = "^Life"
l = re.findall(sre, s)
print(l)

ire = 'i[sft]'
l = re.findall(ire,s)
print(l)

'''


'''
import re
s = "12/12/2022 29/02/1990 hi Hello 01/11/2000 welcome"
datere = "[0-9]"
l = re.findall(datere, s)
print(l)

charre = "[a-zA-Z0-9]"
l = re.findall(charre, s)
print(l)

datere = "[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]"
udatere = "[0-9]{2}/[0-9]{2}/[0-9]{4}"
l = re.findall(datere,s)
ul = re.findall(udatere,s)
print(l)
print(ul)

import re
s = "12/12/2022 29/02/1990 hi Hello 01/11/2000 welcome"
vcre = "[aeiou][^aeiou0-9 /]"
nvre = "[^aeiou]"
l = re.findall(vcre,s)
print(l)

import re
s = "hin + \hello + \welc*omet" #formatted string
spre = r"[\nt]"   #raw string
l = re.findall(spre, s)
print(l)

import re
s = "12/12/2022 29/02/1990 hi Hello 01/11/2000 welcome"
dre = "\d{2}/\d{2}/\d{4}"
l = re.findall(dre, s)
print(l)


import re
s = "Apple _2 a1#12 or_ange qwerty qw@er"
sl = s.split()
varnre = "^[_a-zA-Z]\w*$"
for i in sl:
    l = re.findall(varnre, i)
    if len(l) > 0:
        print(l)

import re
names = "Harry Potter hi John hello J Karthi welcome Samuel Dodzi Akaama python 3"

nre = "[A-Z][a-z]+ [A-Z][a-z]+ [A-Z][a-z]+|[A-Z][a-z]+ [A-Z][a-z]+|[A-Z][a-z]+|[A-Z] [A-Z][a-z]+"
l = re.findall(nre, names)
print(l)

'''