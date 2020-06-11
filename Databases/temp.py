#Assignment required program

import sqlite3

comm = sqlite3.connect("rosterdb.sqlite")
cur = comm.cursor()

cur.execute('''SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X''')

print(cur.fetchone())

comm.close()
