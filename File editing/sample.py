fname = input('Enter file name:')
fhand = open(fname)
line = fhand.read()
line = line.rstrip()
line = line.upper()
print(line)

