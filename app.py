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


app.run(debug=True)
