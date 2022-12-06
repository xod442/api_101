#!/usr/bin/env python
# encoding: utf-8
'''
Stuff here:
'''
import json
from flask import Flask

app = Flask(__name__)

" API Endpoint "
@app.route('/', methods=['POST','GET'])
def welcome():
    welcome = 'Greetings! - Click here -> To see my cat videos http://my.catvideos.com'
    return welcome

" API Endpoint "
@app.route('/name/<name>', methods=['POST','GET'])
def name(name):
    welcome = 'Greetings! %s - Click here -> To see my cat videos http://my.catvideos.com' % (name)
    return welcome

" API Endpoint "
# subtract -, multiply *, divide = /
@app.route('/add/<arg1>/<arg2>', methods=['POST','GET'])
def add(arg1,arg2):
    sum = int(arg1) + int(arg2)
    return str(sum)

" API Endpoint "
@app.route('/subtract/<val1>/<val2>', methods=('GET', 'POST'))
def subrtact_numbers(val1, val2):
    sum = int(val1) - int(val2)
    return str(sum)

" API Endpoint "
@app.route('/multiply/<val1>/<val2>', methods=('GET', 'POST'))
def multiply_numbers(val1, val2):
    sum = int(val1) * int(val2)
    return str(sum)

" API Endpoint "
@app.route('/divide/<val1>/<val2>', methods=('GET', 'POST'))
def devide_numbers(val1, val2):
    sum = int(val1) / int(val2)
    return str(sum)

app.run(debug=True)
