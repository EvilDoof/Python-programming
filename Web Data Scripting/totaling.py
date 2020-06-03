import re
name = input("Enter the file name: ")
fname = open(name)
line = fname.read()
num = re.findall("[0-9]+", line)
total = sum(num)
print(total)