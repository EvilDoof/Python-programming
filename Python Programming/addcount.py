name = input("Enter the name of the file: ")
fname = open(name)
count = 0
for line in fname:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        print(words[1])
        count = count + 1
print("There were", count, "lines in the file with From as the first word")