import sqlite3 as sql

conn = sql.connect('notes.db', check_same_thread=False)

cursor = conn.cursor()

#cursor.execute("""DROP table Notes""")
cursor.execute('''CREATE TABLE IF NOT EXISTS Notes (
    'note'    STRING
    )''')

conn.commit()

conn.close()

def addNotes(note):
    conn = sql.connect('notes.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO Notes VALUES (?)""", (note,))
    conn.commit()
    conn.close()
    
def getNotes():
    conn = sql.connect('notes.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("""SELECT * from Notes""")
    print(cursor.fetchall())
    conn.close()




getNotes()


