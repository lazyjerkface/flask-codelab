from flask import Flask
from flask import render_template
from flask import url_for
app = Flask(__name__)

# Examples can be found at http://flask.pocoo.org/docs/0.12/quickstart/

def build_routes():
  pages = [
    {'name': 'Main',
     'url': url_for('main_page')},
    {'name': 'hello world',
     'url': url_for('hello_world')},
    {'name': 'Username\'s Profile',
     'url': url_for('show_user_profile', username='Username')},
    {'name': 'User\'s Profile',
     'url': url_for('show_user_profile_with_template', name='User')}]
  return pages

	
@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/username/<username>')
def show_user_profile(username):
  return 'Hello %s' % username

 
@app.route('/user/')
@app.route('/user/<name>')
def show_user_profile_with_template(name=None):
    return render_template('profile.html', name=name)


@app.route('/')
def main_page():
  return render_template('bootstrap.html', pages=build_routes())


# Exercise: Create a route to your own page.