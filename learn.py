from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/morning')
def good_morning():
    return 'Good Morning Srinivas'

@app.route('/wish/<event>')
def wish_birthday(event):
    return 'Happy %s' % escape(event)

@app.route('/score/<int:myscore>')
def print_score(myscore):
    return 'Your score is : %d' % myscore