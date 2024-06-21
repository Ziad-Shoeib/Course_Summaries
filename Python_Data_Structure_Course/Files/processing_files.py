# xfile = open("'test.txt'") #Full path doe not work as there are white spaces in the path
# for i in xfile:
#     print(i)

# inp = xfile.read() # this reads the full file including newlines /n

# Searching through a file #
# for line in xfile:
#    line = line.rstrip() #to remove extra newlines
#     if line.startswith('From: '):
#         print(line)   

# Flip The Sequence #
# for line in xfile:
#    line = line.rstrip() #to remove extra newlines
#     if not line.startswith('From: '):
#       continue
#     print(line) 

# Add Exceptions #
# fname = input('Enter the file name: ')
# try:
#     fhand = open(fname)
# except:
#     print('File Cannot be opened: ', fname)
#     quit()

# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count+=1
# print('There were', count, 'subject lines in', fname)                 

    