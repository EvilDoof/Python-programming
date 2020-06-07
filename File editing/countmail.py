#To make a dictionary of all mailing ids and count the id with the maximum emails
name = input("Enter the file: ")
fname = open(name)
count = dict()

for line in fname:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        count[words[1]] = count.get(words[1], 0) + 1

maxmail = None
maxcount = 0
for k,v in count.items():
    if maxmail is None or maxcount < v:
        maxmail = k
        maxcount = v
print(maxmail, maxcount)