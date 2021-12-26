from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Vojtech'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Giorgio'},
            'body': 'Forza Milan per sempre!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

