import sqlite3

conn = sqlite3.connect('test.db')
conn.execute('''CREATE TABLE IF NOT EXISTS todo(
    id INTEGER PRIMARY KEY,
    task TEXT NOT NULL
);''')

def show():
    query = "SELECT * FROM todo;"
    return conn.execute(query)

def insertdata(task):
    query = "INSERT INTO todo(task) VALUES(?);"
    conn.execute(query, (task,))
    conn.commit()


def deletebyid(taskid):
    query = "DELETE FROM todo WHERE id =?;"
    conn.execute(query, (taskid,))
    conn.commit()

def deletebytask(taskval):
    query = "DELETE FROM todo WHERE task =?;"
    conn.execute(query, (taskval,))
    conn.commit()


def updatedata(taskid, newtask):
    query = "UPDATE todo SET task = ? WHERE id = ?;"
    conn.execute(query, (newtask, taskid))
    conn.commit()
