from crypt import methods
from pickle import TRUE
from flask import Flask, redirect, render_template, request, url_for
import pandas as pd

import mysql.connector
app = Flask(__name__)

connection = mysql.connector.connect(host='localhost',
                                     database='Books',
                                     user='root',
                                     password='mysql123')

#cur.execute("SELECT * FROM Book")


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template("index.HTML")


@app.route('/Book', methods=['POST', 'GET'])
def Book():

    if request.method == 'POST':
        #Data = request.form.get
        id = request.form['id']
        Book_name = request.form['Book_name']
        Author_name = request.form['Author_name']
        Stock = request.form['Stock']
        cur = connection.cursor()
        cur.execute(''' INSERT INTO Book VALUES(%s,%s,%s,%s)''',
                    (id, Book_name, Author_name, Stock))

        connection.commit()
        cur.close()
        return f'Book Added'


@app.route('/list', methods=['POST', 'GET'])
def list():
    cur = connection.cursor()
    cur.execute('''SELECT * FROM Book''')
    data = cur.fetchall()
    return render_template('data.HTML', data=data)


if __name__ == "__main__":
    app.run(debug=TRUE)
