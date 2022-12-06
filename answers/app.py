#!/usr/bin/env python
# encoding: utf-8
'''
 ________  ________  ___           _____  ________    _____     
|\   __  \|\   __  \|\  \         / __  \|\   __  \  / __  \
\ \  \|\  \ \  \|\  \ \  \       |\/_|\  \ \  \|\  \|\/_|\  \
 \ \   __  \ \   ____\ \  \      \|/ \ \  \ \  \\\  \|/ \ \  \
  \ \  \ \  \ \  \___|\ \  \          \ \  \ \  \\\  \   \ \  \
   \ \__\ \__\ \__\    \ \__\          \ \__\ \_______\   \ \__\
    \|__|\|__|\|__|     \|__|           \|__|\|_______|    \|__|



   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0.

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


__author__ = "@"
__credits__ = ["You Name"]
__license__ = "Apache2"
__version__ = "0.1.1"
__maintainer__ = "Your Name"
__status__ = "Alpha"

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
