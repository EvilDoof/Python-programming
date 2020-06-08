#Reading all emails from a file and storing that infromation into a database

import sqlite3
import re

conn = sqlite3.connect("db1.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts") #Drops the table if it exists

cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)") #Creates the table

name = input("Enter the name of the file: ")
if (len(name) < 1): name = "mbox.txt" #Sets default file
fname = open(name)
line = fname.read() #Reads entire file as a single string

orgnames = re.findall("From \S+@(\S+)", line) #Reads all domain names from the file
for orgname in orgnames:
    cur.execute("SELECT count FROM Counts WHERE org = ?", (orgname,)) #Retrieves the row containing the org name
    row = cur.fetchone() #Fetches the data

    if row is None:
        cur.execute("INSERT INTO Counts (org, count) VALUES (?, 1)", (orgname,)) #Sets count to 1 if not present in table
    else:
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (orgname,)) #Updates th count by 1

conn.commit() #Commits all changes to the database

cur.execute("SELECT count FROM Counts ORDER BY count DESC LIMIT 1") #Fetches the top organisation by count
print(str(cur.fetchone()))

conn.close() #Closes the database