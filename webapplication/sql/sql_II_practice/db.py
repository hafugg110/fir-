import os
import json
import sqlite3


class DatabaseDriver(object):
    """
    Database driver for the Task app.
    Handles with reading and writing data with the database.
    """

    def __init__(self):
        self.conn = sqlite3.connect("database.db", check_same_thread=False)
        self.create_task_table()

    def create_task_table(self):
        try:
            self.conn.execute(
                """
                CREATE TABLE students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT, 
                    addr TEXT, 
                    city TEXT, 
                    pin TEXT)
                """
            )
        except Exception as e:
            print(e)

    def get_all_tasks(self):
        cursor = self.conn.execute(
            """
            SELECT * FROM students;
            """
        )
        tasks = []
        for row in cursor:
            tasks.append({"id": row[0],
                        "name": row[1], 
                        "addr": row[2],
                        "city": row[3],
                        "pin": row[4]})

        return tasks

    def insert_task_table(self, nm, addr, city, pin):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO students(name, addr, city, pin) VALUES(?, ?, ?, ?)", (nm, addr, city, pin)
        )
        self.conn.commit()
        return cursor.lastrowid

    def get_task_by_id(self, id):
        cursor = self.conn.execute("SELECT * FROM students WHERE ID = ?", (id,))

        for row in cursor:
            return {
                "id": row[0],
                "name": row[1], 
                "addr": row[2],
                "city": row[3],
                "pin": row[4]
                }

        return None

    # def update_task_by_id(self, id, description, done):
    #     self.conn.execute(
    #         """ 
    #         UPDATE students 
    #         SET description = ?, done = ?
    #         WHERE id = ?;
    #         """,
    #         (description, done, id),
    #     )
    #     self.conn.commit()

    # def delete_task_by_id(self, id):
    #     self.conn.execute(
    #         """
    #         DELETE FROM students
    #         WHERE id = ?;
    #         """,
    #         (id,),
    #     )
    #     self.conn.commit()



# From: https://goo.gl/YzypOI
def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance

# Only <=1 instance of the database driver
# exists within the app at all times
DatabaseDriver = singleton(DatabaseDriver)