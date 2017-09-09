import os

from flask import Flask
from flask import render_template

app = Flask(__name__)

# Examples can be found at http://flask.pocoo.org/docs/0.12/quickstart/

# This just prints whatever you want on the page.
# Exercise 1:
#   Modify the return value and try inserting HTML on the page.
#   See the results at https://[WORKSPACE-NAME]-[USERNAME].c9users.io
# Note that this is the index or default homepage for your application.
@app.route('/')
def hello_world():
    return 'Hello, World!'


# You can add variable parts to a URL.
# Exercise 2:
#   Print the username in bold if its your name.
#   See the results at
#   https://[WORKSPACE-NAME]-[USERNAME].c9users.io/username/<username>
@app.route('/username/<username>')
def show_user_profile(username):
  # Hint: Modify the "if" statement to check for your name.
  # Hint 2: You can add HTML to the string below to make the name bold
  if username:
    return 'Hello %s' % username
  # Always ensure the function returns a value or your application breaks in
  # unexpected ways.
  return 'Hello %s' % username


# Templates are powerful and dynamic.
# Exercise 3:
#   Similar to Exercise 2, print name in bold if its your name.
#   See the results at
#   https://[WORKSPACE-NAME]-[USERNAME].c9users.io/user/<name>
@app.route('/user/')
@app.route('/user/<name>')
def show_user_profile_with_template(name=None):
    # Hint: You need to edit profile.html this time.
    # In this exercise, we're utilizing the templating language
    # provided by Flask.
    # http://flask.pocoo.org/docs/0.12/quickstart/#rendering-templates
    return render_template('profile.html', name=name)


# Template inheritance makes templating even more powerful.
# main_page() and feature() use a base template (base.html) and extend it.
# 1) See https://[WORKSPACE-NAME]-[USERNAME].c9users.io/main and take note of
#    what happens when you navigate between 'Home' and 'Feature'.
# 2) Take a look at base.html, info.html, and feature.html to understand
#    how info.html and feature.html extend base.html.
# Exercise 4:
#   Create a route to your own page.
#   HINT: You need to create a function here and modify base.html.
@app.route('/main')
def main_page():
  return render_template('info.html')


@app.route('/feature')
def feature():
  return render_template('feature.html')


# This is adapted to work in C9.
if __name__ == '__main__':
  app.debug = True
  host = os.environ.get('IP', '0.0.0.0')
  port = int(os.environ.get('PORT', 8080))
  app.run(host=host, port=port)
