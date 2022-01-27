from flask import Blueprint, render_template,request,redirect,url_for
from utilities.general import *
# contact_us blueprint definition
contact_us = Blueprint('contact_us', __name__,static_folder='static',static_url_path='/pages/contact_us/static', template_folder='templates')
title ='Matamim | Contact Us'

# Routes
@contact_us.route('/contact_us')
def index():
    return render_template('contact_us.html',title = title)

@contact_us.route('/SaveContactUs' , methods = ["POST"])
def saveContact():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    email = request.form['email']
    msg = request.form['subject']
    saveContactToDB(firstname,lastname,email,msg)
    return redirect('/contact_us')