from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Adam'}
    posts = [
        {
                'author': {'username': 'John'},
                'body': 'Beautiful day in Melbourne!'
        },
        {
                'author': {'username': 'Susan'},
                'body': 'Barcelona ftw!'
        },
        {       'author': {'username': 'David'},
                'body': "Surf's up!"
        },
        {       'author': {'username': 'Juno'},
                'body': 'We are going hang-gliding today'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts) 

@app.route('/login', methods=['GET', 'POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign in', form=form)
