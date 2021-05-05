import sqlite3
conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute(
    """
    CREATE TABLE students (
        name TEXT NOT NULL,
        addr TEXT,
        city TEXT,
        pin TEXT NOT NULL)
    """
    )
print("Table created successfully")
conn.colne() 