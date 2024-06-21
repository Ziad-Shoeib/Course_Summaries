import os
# Split a string
abc = 'With Three Words'
stuff = abc.split() #returns a list
print(stuff) # ['With', 'Three', 'Words']

# It is not only for spaces
# By default split() looks for spaces

line = 'frist;second;third'
thing = line.split(';')
print(thing) # It Prints: ['frist', 'second', 'third']


fhand = open('mboxshort.txt')

for line in fhand:
    if line.startswith('from') : 
        continue
    words = line.split()
    print(words)