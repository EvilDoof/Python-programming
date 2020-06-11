#To create a database of a playlist from an exported iTunes XML File

import xml.etree.ElementTree as ET
import sqlite3

name = input("Input the name of the file: ")
fname = open(name)

comm = sqlite3.connect("Playlist.sqlite")
cur = comm.cursor()

cur.executescript('''DROP TABLE IF EXISTS Artist;
                DROP TABLE IF EXISTS Genre;
                DROP TABLE IF EXISTS Album;
                DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);''')

def findtext(val, key):
    found = False
    for child in val:
        if found:
            return child.text
        if (child.tag == 'key') and (child.text == key):
            found = True
    return found

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')

for ele in all:
    if (findtext(ele, "Track ID") is False): continue

    name = findtext(ele, "Name")
    artist = findtext(ele, "Artist")
    album = findtext(ele, "Album")
    genre = findtext(ele, "Genre")
    length = findtext(ele, "Total Time")
    rating = findtext(ele, "Rating")
    count = findtext(ele, "Track Count")
    #len INTEGER, rating INTEGER, count INTEGER

    cur.execute("INSERT OR IGNORE INTO Artist (name) VALUES (?)", (artist,))
    cur.execute("SELECT id FROM Artist WHERE name = ?", (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)", (album, artist_id))
    cur.execute("SELECT id FROM Album WHERE title = ?", (album,))
    album_id = cur.fetchone()[0]

    cur.execute("INSERT OR IGNORE INTO Genre (name) VALUES (?)", (genre,))
    cur.execute("SELECT id FROM Genre WHERE name = ?", (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ?)''', 
        ( name, album_id, genre_id, length, rating, count ) )

    comm.commit()

comm.close()
fname.close()