# from flask_wtf import Form
from flask import render_template, request
from app import app

from app.models.forms import LoginForm

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():

    # form = LoginForm()
    form = LoginForm()
    print('I am here')

    # print(str(form.validate_on_submit()))

    # print('Method: ', request.method)
    # print(form.validate_on_submit())
    
    print(form.username.data, form.password.data, form.remember_me.data)

    # print(FlaskForm.validate(self))

    if form.is_submitted():
        print('form.validate(): ', form.validate())
    print('form.is_submitted(): ', form.is_submitted())
    #print('form.validate_on_submit(): ', form.validate_on_submit())
    print(form.errors)

    print('form')
    print(form)

    '''
    if form.validate_on_submit():
        print('true?')
    else: 
        print('false?')
    '''

    return render_template('login.html', form=form)
