text = "X-DSPAM-Confidence:    0.8475"
index = text.find(':')
text = text[index+1:]
text = text.lstrip()
num = float(text)
print(num)