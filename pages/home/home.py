import json

from flask import Blueprint, render_template, redirect, url_for,jsonify
from interact_with_DB import interact_db
# home blueprint definition
home = Blueprint('home', __name__,static_folder='static',static_url_path='/pages/home/static',template_folder='templates')
title = 'Matamim | Home'

# Routes
@home.route('/home')
@home.route('/')
def home_func():
    query_products = "Select * from Products limit 3"
    main_products = interact_db(query_products,"fetch")
    query_events = "Select * from events"
    main_events = interact_db(query_events, "fetch")
    return render_template('home.html',title = title, products = main_products, events = main_events)


