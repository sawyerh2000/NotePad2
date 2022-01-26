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
    today = date.today()
    curr = now.strftime("%H:%M:%S") + " " + today.strftime("%m/%d/%Y")
    d1 = today.strftime("%m/%d/%Y")
    s = str(note)
    start=31
    end=s.index("'", 31)
    s=s[start:end] + " - " + curr
    cursor.execute("""INSERT INTO Notes VALUES (?)""", [s])
    conn.commit()
    conn.close()



#getNotes function to print out the database entries onto a webpage
def getNotes():
    notelist=[]
    conn = sql.connect('notes.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("""SELECT note from Notes""")
    curlist=cursor.fetchall()
    for i in curlist:
        notelist.append(i[0])
    conn.commit()
    conn.close()
    print(*notelist)
    return notelist
    
