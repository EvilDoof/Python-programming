name = input("Enter the name of the file: ")
fname = open(name)
count = dict()
for line in fname:
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        timsplt = time.split(":")
        count[timsplt[0]] = count.get(timsplt[0], 0) + 1
lst = sorted(count.items())
for (k,v) in lst:
    print (k, v)
