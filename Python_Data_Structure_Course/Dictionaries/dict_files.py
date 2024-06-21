# The General Pattern to count the words in a line of text 
# is to split the line into words, then loop through the words 
# and use a dictionary to track teh count of each word independently

counts = dict()
print("Enter Text")
line = input('')
words = line.split()
print('Words:', words)
print('Counting...')
for word in words: 
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)

# Looping Through a Dictionary
for key in counts: 
    print(key, counts[key])