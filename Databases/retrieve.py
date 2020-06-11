#To retrieve the top 3 documents from the Playlist database

import sqlite3

comm = sqlite3.connect("Playlist.sqlite")
cur = comm.cursor()

cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Genre JOIN Track JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.id and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 10''')
for lst in cur.fetchall():
    print(lst)

#cur.execute('''SELECT title FROM Track WHERE title = 'hello'
#    ''')
#print(cur.fetchone())
#comm.close()