from flask import Flask
from flask import url_for
from flask import request
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/morning')
def good_morning():
    return 'good morning'

@app.route('/wish/<event>')
def wish(event):
    return 'Happy %s' % escape(event)

@app.route('/score/<int:myscore>')
def score(myscore):
    return '<h1> Your score is : %d '% myscore

@app.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method == 'POST'):
        return 'POST request'
    else:
        return 'GET request'

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return 'POST request'
    else:
        return 'GET request'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/cameras')
@app.route('/cameras/<brand>')
def listCameras(brand=None):
    
    allCameras = [{'name':'xt4', 'type':'Fujifilm'},
    {'name':'xt3', 'type':'Fujifilm'},
    {'name':'xh1', 'type':'Fujifilm'},
    {'name':'a7iii', 'type':'Sony'},
    {'name':'a6600', 'type':'Sony'},
    {'name':'gh5', 'type':'Panasonic'},
    {'name':'80d', 'type':'Canon'},
    {'name':'90d', 'type':'Canon'},
    {'name':'r5', 'type':'Canon'},
    {'name':'5d mark iv', 'type':'Canon'},
    {'name':'z6', 'type':'Nikon'},
    {'name':'d850', 'type':'Nikon'}
    ]

    return render_template('cameras.html', brand=brand, cameras=allCameras)

with app.test_request_context():
    print(url_for('wish', event='service anniversary'))
