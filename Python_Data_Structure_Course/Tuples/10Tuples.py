# In Summary, they are unmodifiable lists

# Tuple Syntax Just () instead of [] in lists
x = ('Glen', 'Sally', 'Joseph')
print(x[2]) #Joseph
#x.append('hh') #error
#x[1] = 'hhh' #error
# Sort() Does not work
# append or reverse too don't work
print(x)

#################

(x,y) = (4, 'fred') # x=4 y='fred' (Tuple Assignment)

###################

## Tuples and Dictionaries
d = {'Ziad' : 1, 'Ahmed' : 2}
print(d.items()) #gives back a list of tuples
# dict_items([('Ziad', 1), ('Ahmed', 2)])

###################

## Tuples Are Comparable
(10,1,2) < (5, 1, 2) # False: it compares only the frist on the left
# If Matched It looks to the next pair
print((0, 1, 200000) < (0, 3, 4)) #True

###################

## Sorting Lists of Tuples (Sort by key)
dd = {'a':10,'c':22, 'b':1}
print(sorted(dd.items())) # [('a', 10), ('b', 1), ('c', 22)] Sorted based on the frist(key) a, b, c

## Sorting Lists of Tuples (Sort by value)
aa = {'a':10,'c':22, 'b':1}
temp = list()
for k,v in aa.items() :
    temp.append( (v, k) )
print(temp) # [(10, 'a'), (22, 'c'), (1, 'b')]
temp = sorted(temp ,reverse=True)
print(temp) # [(22, 'c'), (10, 'a'), (1, 'b')]
