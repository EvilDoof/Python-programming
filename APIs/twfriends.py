#Used to see the friends of the Twitter user entered from the database

import sqlite3

comm = sqlite3.connect("twfriends.sqlite")
cur = comm.cursor()

while True:
    acc = input("Enter the user name or enter to quit: ")
    if (len(acc) < 1): break

    cur.execute("SELECT id FROM Friends WHERE name = ?", (acc,))
    try:
        id = cur.fetchone()[0]
    except:
        print("Account not found")
        continue

    cur.execute("SELECT Friends.name FROM Friends JOIN Links ON Links.friend2 = Friends.id WHERE Links.friend1 = ?", (id,))
    
    lst = cur.fetchall()
    if (len(lst) == 0):
        print("Account friend list not obtained yet")
        continue
    print("The friends are:\n")
    for name in lst:
        print(name[0])
    print("")

comm.close()