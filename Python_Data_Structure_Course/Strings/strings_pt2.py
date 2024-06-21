## Part 2 ##
# The "in" keword can also be used to check to see if one string is "in" another string
# The "in" expression is a logical expression that returns True or False and can be used in an if statement

fruit = "Banana"
print ('n' in fruit)
print ('m' in fruit)
print ('nan' in fruit)

# Upper Case letters lower than Lower Case Letters
print("a">"A") #True
print("a"<"A") #False
print("ahme">"Ahmed") #True

#Upper to Lower and Lower to Upper
print("Hi There".lower())
print("Hi There".upper())

#Class String Methods 
stuff = 'Hello World'
print(dir(stuff))

#Searching a String
fruit2 = 'Banana'
pos = fruit2.find('na')
print(pos)

aa = fruit2.find('z')
print(aa) #If Substring is not found it gives -1

# Search and Replace
great2 = 'Hello Bob'
nstr = great2.replace('Bob', 'Jane') #Does not change great2 only a copy
print(nstr)
nstr = great2.replace('o','X') # Note that this is multi replace
print(nstr)

great3 = "Banana"
nstr = great3.replace('n','l')
print(nstr)


# Stripping White Spaces
great4 = '  Hello Bob   '
print(great4.rstrip()) #right
print(great4.lstrip()) #left
print(great4.strip()) #Both Sides

# Prefixes
line = 'Please have a nice day'
print(line.startswith("Please"))
print(line.startswith("p"))

#Parsing and Eztracting
data = 'From stephen.marquard@uct.az.za Sat Jan 5 09:14:16 2008'
atops = data.find('@')
print(atops) #21 (Position)
sppos = data.find(' ',atops) # to tell that you want further than a specific position
print(sppos)
host = data[atops+1 : sppos]
print(host)

print(len('banana'))
print(data[data.find('.'):data.find('.')+3])

strex = "X-DSPAM-Confidence: 0.8475"
num = float(strex[strex.find(" "):len(strex)])
print(num+1)