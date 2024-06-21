# A list element can be any python obect even another list
# A list can be empty
# Does not have to be the same type of data
print([1,2,3])
print(['red','green','blue'])
print([1,[5,6],7])
print(['red',1,2])

# Indexed from 0
test = [1,2,3,4]
print(test[1])

# Strings are "immutable" - we can't change the contents of a string - we must make a new string to make any change
# Lists re 'mutable" - we can change an element of a list using the index operator
loot = [3,5,6,7]
loot[0]=5
print(loot)

# Range Function #
# the range function returns a list of numbers that range from zero to one less than the paramter
print(range(4)) # [0,1,2,3]
freinds = ["Ziad","Ahmed","Fathey"]
print(list(range(len(freinds)))) #[0,1,2]

for i in range(len(freinds)) : #If we want to know their order or number or loop to a specific rage
    freind = freinds[i]
    print("Happy New Year: ", freind)