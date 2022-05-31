# -*- coding: utf-8 -*-
"""
Created on Tue May 31 10:22:40 2022

@author: anike
"""

from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Welcome!!"

@app.route('/second')
def second_function():
    return "Welcome to second function!!"

@app.route('/add')
def add():
    return "You are in Addition  Function"

@app.route('/sub')
def sub():
    return "You are in Subtraction Function"

@app.route('/multi')
def multi():
    return "You are in Multiplication  Function"

@app.route('/div')
def div():
    return "You are in Division  Function"

@app.route('/user/<username>')
def wel(username):
    return "Welcome %s" %username


if __name__=='__main__':
     app.run()