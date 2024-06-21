fhand = open('mbox_short.txt')

for line in fhand:
    line = line.rstrip()
    print(line.upper())