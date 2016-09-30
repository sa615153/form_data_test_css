from flask import render_template,request,g,url_for,flash,redirect
from app import app
from forms import LoginForm


@app.route('/login', methods= ['GET', 'POST'])
def login():
    print('2')
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for Name: ' + form.user_name.data)
        flash('passwd: ' + str(form.password.data))
        flash('remember_me: ' + str(form.remember_me.data))
        flash('*********************************************'
              '')

        flash('request.form.get(\'user_name\')'+request.form.get('user_name'))
        flash('request.form.get(\'password\')' + request.form.get('password'))
        return redirect('/show')
    return render_template('login.html',
                           title = 'Sign In',
                           form = form)


@app.route('/show', methods= ['GET', 'POST'])
def index():
    return render_template('show.html')