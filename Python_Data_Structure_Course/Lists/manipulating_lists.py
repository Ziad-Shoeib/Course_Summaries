# Concatenate
a = [1,2,3]
b = [4,5,6]
c = a+b 
print(c)

# Slicing (final limit not taken)
t = [1,2,3,4,5,6,7,8,9]
print(t[1:3]) #[2,3]
print(t[:4]) #[1,2,3,4]
print(t[3:]) #[4,5,6,7,8,9]
print(t[:]) #[1,2,3,4,5,6,7,8,9]

# Methods
x = list()
print(dir(x))

#  building  list from scratch
# Creting n empty list nd using 'append' method
# The list stays in order and new elements are added at the end of the list
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

# is something in a list?
some = [1,9,21,10,16]
print(9 in some) # True
print(20 not in some) # True

# Lists are in order
feinds2 = ['Joseph', 'Glen', 'Sally']
feinds2.sort()
print(feinds2) # ['Glen', 'Joseph', 'Sally'] # AAplphabiticl Sort

# Built-in funtions and Lists
numss = [3,41,12,9,74,15]
print(len(numss))
print(max(numss))
print(min(numss))
print(sum(nums))
print(sum(numss)/len(nums))

