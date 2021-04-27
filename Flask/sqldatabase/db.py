import sqlite3
conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.ececute(
    """
    CREATE TABLE students (
        name TEXT,
        addr TEXT,
        city TEXT,
        pin TEXT)
    """
    )
print("Table created successfully")
conn.colne()

from flask import Flask, render_template, url_for, request
import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_student():
    return render_template(('student.html'))

@app.route('/addrec', methods=['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin