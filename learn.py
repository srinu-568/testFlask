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


'''
1. import Flask class -> an instance of this class is WSGI application.
2. param to Flask is the module or package required by Flask to know where to look for templates, static content etc.
3. route decorator will tell us, what URL should trigger our function.
4. the function name(hello_world in our case) is also used to generate URL.
5. run -> set FLASK_APP = hello.py
6. run -> flask run - this will start the dev web server.

DEBUG_MODE

7. run -> set FLASK_ENV = development -> flask run
    * it activates the debugger
    * it activates the automatic reloader
    * it enables debug mode on flask application


8. URL building
    * build urls using URL reversing method url_for, it takes 2 params, 1-function name, 2-args taken by function
    * change urls in one go instead of changing the hardcoded values at multiple places
    * if application is placed outside root, then url_for() takes care of adding the required 

    ex : with app.test_request_context():
            print(url_for('wish', event='service anniversary'))

        output : /wish/service%20anniversary

9. HTTP methods
    * @app.route('/home', methods=['GET', 'POST'])

10. static files
    * create a folder 'static' and place the contents there
    * the files are accessible using the 'static' end point
    * i.e. url_for('static', 'style.css')

11. Rendering templates
    * from flask import render_template
    * create a "templates" folder, i.e. Flask will look for templates in the "templates" folder.
    * render_template('home.html', key1=value1)
        a. first argument is the template name to be displayed.
        b. key/value pair(keyword argument) which need to be passed on to template. note, these values will be accessible in the template using the template language.
        c. inside the template, you will also have access to "session", "request" and "g" objects.
    * usage of jinja template language, i.e. usage of tags {{ }}, {% if %}, {% else %} etc inside the html.
        a. template inheritence is possible in jinja
    
    * from markupsafe import Markup
        a. usage of Markup, Markup.escape for escaping character in HTML strings.
    



'''