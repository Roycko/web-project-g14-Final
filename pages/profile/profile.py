from flask import Blueprint, render_template,session,request,flash,redirect,url_for
from utilities import general
from utilities.entities import user

# profile blueprint definition
profile = Blueprint('profile', __name__,static_folder='static',static_url_path='/pages/profile/static', template_folder='templates')
title ='Matamim | Profile'

# Routes
@profile.route('/profile')
def index():
    events = general.getMyEvents()
    personalEvents = general.getMyPersonalEvents()
    user = general.getUser(session['email_address'])
    return render_template('profile.html',title = title, user = user, myEvents=events, personalEvents = personalEvents)

@profile.route('/update_user', methods =['post'])
def updateUser():
    user = general.getUser(session['email_address'])
    firstName = request.form['FirstName']
    lastName = request.form['LastName']
    password = request.form['Password']
    general.update_user(session['email_address'],password, firstName, lastName)
    return redirect(url_for('profile.index'))

@profile.route('/deleteEvent', methods = ["post"])
def deleteEvent_func():
    for k,v in request.form.items():
        eventID=k
    general.deleteMyEvent(eventID)
    return redirect(url_for('profile.index'))
