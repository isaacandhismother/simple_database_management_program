import sqlite3

# Creating a cursor that provides a connection with a database

conn = sqlite3.connect('employee.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, surname TEXT, "
          "age INTEGER)")
