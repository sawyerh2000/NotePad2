import sqlite3 as sql
from datetime import *

conn = sql.connect('notes.db', check_same_thread=False)

cursor = conn.cursor()

#cursor.execute("""DROP table Notes""")

#Create a table if one isn't already created:
cursor.execute('''CREATE TABLE IF NOT EXISTS Notes (
    note    TEXT
    )''')



conn.commit()

conn.close()

#addNotes function to add some text into the database from the webapp.
def addNotes(note):
    conn = sql.connect('notes.db', check_same_thread=False)
    cursor = conn.cursor()
    now = datetime.now()
    currtime = now.strftime("%H:%M:%S")
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    s = str(note)
    start=31
    end=s.index("'", 31)
    ls =[]
    s=s[start:end] + " - " + currtime + " " + d1
    ls.append(s)
    cursor.execute("""INSERT INTO Notes VALUES (?)""", ls)
    conn.commit()
    conn.close()
    ls.clear()


#getNotes function to print out the database entries onto a webpage
def getNotes():
    conn = sql.connect('notes.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("""SELECT note from Notes""")
    notelist=cursor.fetchall()
    conn.commit()
    conn.close()
    notelist = map(stripNotes, notelist)
    newlist = []
    for i in notelist:
        newlist.append(i)
    return newlist

#aid function to strip strings in notelist
def stripNotes(words):
    words=str(words)
    words = words.strip("(,')")
    return words





