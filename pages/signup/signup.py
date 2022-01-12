import flask
from flask import Blueprint, render_template,request,redirect
from interact_with_DB import interact_db
import datetime
from flask import session
from flask import flash
import flask

# signup blueprint definition
signup = Blueprint('signup', __name__, static_folder='signup', static_url_path='/static', template_folder='templates')
title = 'Matamim | Sign Up'

# Routes
@signup.route('/signup')
def index():
    return render_template('signup.html',title = title)
@signup.route ('/insert_user',methods=['get','post'])
def insert_user_func():
        #get the date
        first_name=request.form['first_name']
        last_name = request.form['last_name']
        user_name=request.form['user_name']
        birth_date=request.form['birth_date']
        Registration_DT=datetime.datetime.now()#.timestamp()
        email=request.form['email']
        password=request.form['pass']
        # check if user_name available
        query="select * from Users where user_name='%s'" %(user_name)
        is_not_available=interact_db(query=query, query_type='fetch')
        if is_not_available:
            flask.flash('Please change your user name')
            return redirect('/signup')
        #insert
        query="insert into Users(first_name,email_address,last_name,user_name,password,birth_date,Registration_DT) values ('%s','%s','%s','%s','%s','%s','%s');" %(first_name,email,last_name,user_name,password,birth_date,Registration_DT)
        interact_db(query=query,query_type='commit')
        query = "select * from Users where user_name='%s' and password='%s' ;" % (user_name, password)
        users = interact_db(query=query, query_type='fetch')
        if users:
            for user in users:
                session['username'] = user[4]
                session['user_id'] = user[0]
        flask.flash('signup success :)')
        return redirect('/home')

@signup.route('/login',methods=["GET","POST"])
def login_func():  # put application's code here
    if request.method == 'POST':
        # no with the args in the 'post'(get-> args, post->form)
        user_name=request.form['user_name']
        password = request.form['pass']
        # this is the global veriable
        query = "select * from Users where user_name='%s' and password='%s' ;" % (user_name,password)
        users=interact_db(query=query, query_type='fetch')
        if users:
            for user in users:
                session['username']=user[4]
                session['user_id'] = user[0]
            return redirect('/home')
        else:
            flask.flash(' login no success')
            return redirect('/home')


@signup.route('/logout')
def logout_func():
    session['username']=''
    session['user_id']=''
    return redirect('/home')