# Casting Dictionaries to lists
jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(list(jjj)) #Will Print only the keys
print(list(jjj.keys())) # Will give you keys in the list
print(list(jjj.values())) # Will Get the values
print(list(jjj.items())) # This is a tuple actually (read only list)[('chuck', 1), ('fred', 42), ('jan', 100)]

for aaa,bbb in jjj.items() :
    print(aaa, bbb)
#Will Print: 
    # chuck 1
    # fred 42
    # jan 100