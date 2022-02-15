import flask
from flask import Blueprint, render_template,request,redirect,flash
from utilities.general import *
import datetime
from flask import session
from flask import flash
import flask
from utilities.entities.user import User
from utilities.general import get_all_users

# signup blueprint definition
signup = Blueprint('signup', __name__,static_folder='static',static_url_path='/pages/signup/static', template_folder='templates')
title = 'Matamim | Sign Up'

# Routes
@signup.route('/signup')
def index():
    return render_template('signup.html',title = title)
@signup.route ('/insert_user',methods=['post'])
def insert_user_func():
        #get the date
        first_name=request.form['first_name']
        last_name = request.form['last_name']
        user_name=request.form['user_name']
        birth_date=request.form['birth_date']
        Registration_DT=datetime.datetime.now().isoformat(timespec='seconds')#.timestamp()
        email=request.form['email']
        password=request.form['pass']
        # check if user_name available
        is_not_available=is_email_not_availabe(email)
        is_user_pass_not=is_user_pass_not_availabe(user_name,password)
        if is_not_available or is_user_pass_not:
            if is_not_available:
                flash('Email already exists')
            if is_user_pass_not:
                flash('change username+pass')
            return redirect('/signup')
        else:
            newUser = User(email,first_name,last_name,user_name,password,birth_date,Registration_DT)
            newUser.registerUser()
            session['username'] = user_name
            session['user_id'] = newUser.getUserId()
            session['email_address'] = newUser.getEmail()
            flash('signup success :)')
            return redirect('/home')

@signup.route('/login',methods=["POST"])
def login_func():  # put application's code here
    if request.method == 'POST':
        # no with the args in the 'post'(get-> args, post->form)
        user_name=request.form['user_name']
        password = request.form['pass']
        # this is the global veriable
        query = "select * from Users where user_name='%s' and password='%s' ;" % (user_name,password)
        users=dbManager.fetch(query)
        if users:
            for user in users:
                session['username']=user[4]
                session['user_id'] = user[0]
                session['email_address'] = user[1]
            return redirect('/home')
        else:
            flask.flash(' login no success')
            return redirect('/home')


@signup.route('/logout')
def logout_func():
    session['username']=''
    session['user_id']=''
    session['email_address'] = ''
    return redirect('/home')