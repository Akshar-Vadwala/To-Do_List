# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 23:37:34 2023

@author: akshar
"""

from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__) #object of Flask for main script
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= 'your_password'
app.config['MYSQL_DB']= 'name_of_Database'



arrow = MySQL(app) #object of MySQL and pass app

@app.route('/')
def todo_list():
    cur = arrow.connection.cursor()
    cur.execute("SELECT TASK FROM TASKS")
    values = [ value[0] for value in cur.fetchall() ]#Add zeroth indexed element from tuple of fetchall() and store to list of values 
    cur.close()
    arrow.connection.commit()

    return render_template('todo.html',values=values)

@app.route('/add_item', methods=['POST', 'GET'])
def add_item():
    item= request.form['item']
    cur = arrow.connection.cursor()
    cur.execute("INSERT INTO TASKS (TASK) VALUES (%s)", (item,) ) #Insert task into table
    cur.close()
    
    return todo_list()

@app.route('/remove_item',methods=['POST', 'GET'])
def remove_item():
    item = request.form['del']
    cur = arrow.connection.cursor()
    
    cur.execute("DELETE FROM TASKS WHERE task=%s", (item,)) #Delete task from table

    cur.close()

    return todo_list()    

