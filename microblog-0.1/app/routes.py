from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    # The operation that converts a template into a complete HTML page is called rendering
    # To render the template I had to import a function 
    # - that comes with the Flask framework called render_template()
    return render_template('index.html', title='Home', user=user)
    # This function takes a template filename and a variable list of template arguments and 
    # - returns the same template, but with all the placeholders in it replaced with actual values.