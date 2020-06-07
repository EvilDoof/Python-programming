name = input("Enter the file name: ")
fname = open(name)
words = list()
for line in fname:
    line = line.rstrip()
    piece = line.split()
    for word in piece:
        if word not in words:
            words.append(word)
words.sort()
print(words)
