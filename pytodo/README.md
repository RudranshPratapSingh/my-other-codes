
# Python GUI TODO !

This repo contains source for the 
1. **Python GUI Task manager**.
2. **Python CLI TODO**
3. **Python Database Helper**

# Watch Video Tutorials 

## [Working With Database](https://youtu.be/xtQIdV8NEB4)


## Database Helpers For SQLITE3

### Opening A Database
```python
# import sqlite 3
import sqlite3

# open a database
conn = sqlite3.connect("database.db")
# will create one if doesn't already exists
```
### Creating A Table
```python
# create a table
conn.execute('''CREATE TABLE IF NOT EXISTS tablename(
	columnname datatype PRIMARY KEY,
	anothercolumn datatype attributes
)''')
```

### Inserting Data Based On Variables
```python
# call the function with number of required parameters
def  insertdata(task):
	query =  "INSERT INTO todo(task) VALUES(?);"
	# remember the comma after task
	# it's necessary
	conn.execute(query,  (task,))
	# to make sure that changes are reflected in the database
	conn.commit()
```

### Selecting Data From The Database
```python
# can use WHERE clause
query =  'SELECT * FROM todo;'
for rows in conn.execute(query):
	print(rows)
```

### Deleting Data From The Database
```python
# to delete data based on ID
def  deletebyid(taskid):
	query =  "DELETE FROM todo WHERE id =?;"
	conn.execute(query,  (taskid,))
	conn.commit()
```

### Updating Data In The Database
```python
# updating data
def  updatedata(taskid,  newtask):
	query =  "UPDATE todo SET task = ? WHERE id = ?;"
	conn.execute(query,  (newtask, taskid))
	conn.commit()
```