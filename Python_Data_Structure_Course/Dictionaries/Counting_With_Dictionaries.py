counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names : 
#     if name not in counts: 
#         counts[name] = 1
#     else: 
#         counts[name]+=1
# print(counts) # {'csev': 2, 'cwen': 2, 'zqian': 1}

# Using get method (Key you're looking for, the default value if key is not present)

for name in names : 
    counts[name] = counts.get(name, 0) + 1 #get name from counts
print(counts) # {'csev': 2, 'cwen': 2, 'zqian': 1}
