maxi = None
mini = None
while True:
    numi = input("Enter the number:")
    if (numi == "done"):
        break
    try:
        num = int(numi)
    except:
        print("Invalid input")
        continue
    if (maxi is None):
        maxi = int(num)
    elif (maxi < int(num)):
        maxi = int(num)
    if (mini is None):
        mini = int(num)
    elif (mini > int(num)):
        mini = int(num)
print("Maximum is", maxi)
print("Minimum is", mini)

