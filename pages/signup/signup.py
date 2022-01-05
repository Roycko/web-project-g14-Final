import flask
from flask import Blueprint, render_template,request,redirect
from interact_with_DB import interact_db
import datetime

# signup blueprint definition
signup = Blueprint('signup', __name__, static_folder='signup', static_url_path='/static', template_folder='templates')
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
        Registration_DT=datetime.datetime.now().timestamp()
        email=request.form['email']
        password=request.form['pass']
        #inster
        query="insert into Users(first_name,email_address,first_name,last_name,user_name,password,birth_date,Registration_DT) values ('%s','%s','%s','%s','%s','%s','%s',Registration_DT);" %(first_name,email,first_name,last_name,user_name,password,birth_date)
        interact_db(query=query,query_type='commit')
        flask.flash('insert success')
        return redirect('/assignment10')
