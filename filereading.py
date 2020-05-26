fname = input("Enter file name:")
fhand = open(fname)
count = 0
total = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        index = line.find(':')
        line = line[index+1:]
        num = float(line)
        count = count + 1
        total = total + num
avg = total / count
print('Average spam confidence:', avg)
