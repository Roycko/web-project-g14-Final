import json

from flask import Blueprint, render_template,request,redirect,url_for
from utilities.general import *
# home blueprint definition
home = Blueprint('home', __name__,static_folder='static',static_url_path='/pages/home/static',template_folder='templates')
title = 'Matamim | Home'

# Routes
@home.route('/home')
@home.route('/')
def home_func():
    cartForUser()
    query_products = "Select * from Products limit 3"
    main_products = dbManager.fetch(query_products)
    query_events = "Select * from events where is_personal=0 limit 3"
    main_events = dbManager.fetch(query_events)
    return render_template('home.html',title = title, products = main_products, events = main_events)

@home.route('/subscribe', methods=["POST"])
def subscribeFunc():
    email = request.form["email"]
    firstname = "Subscribe"
    lastname = "Subscribe"
    msg = "Subscribe"
    saveContactToDB(firstname,lastname,email,msg)
    return redirect(url_for('home.home_func'))


