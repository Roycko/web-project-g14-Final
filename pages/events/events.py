from flask import Blueprint, render_template,session,request,redirect,url_for
from utilities.general import *
import datetime
from flask import flash

# events blueprint definition
events = Blueprint('events', __name__,static_folder='static',static_url_path='/pages/events/static', template_folder='templates')
title = 'Matamim | Our Events'

# Routes
@events.route('/events')
def index():
    return render_template('events.html',title = title)

@events.route('/saveExistingEvent', methods = ['POST'])
def saveExistingEvent_func():
    event_type = 'Existing_Event'
    event_name = request.form.get('event_name')
    event_date = request.form.get('event_date')
    Amount = request.form['Amount']
    fname = request.form['fname']
    Lname = request.form['Lname']
    email = request.form['email']
    Phone = request.form['Phone']
    event_res_dt = datetime.datetime.now().isoformat(timespec='seconds')#.timestamp()
    event_status = 'approved'
    saveExistingEventToDB(event_type, event_name, event_date, Amount, fname, Lname, email, Phone, event_res_dt, event_status)
    flash('existing event ordered')
    return redirect('/home')

@events.route('/savePrivateEvent', methods = ['POST'])
def savePrivateEvent_func():
    p_event_type = "Private Event"
    p_event_name = request.form.get('p_event_name')
    Food_prefernces = request.form.get('Food_prefernces')
    p_event_date = request.form.get('p_event_date')
    PAmount = request.form['PAmount']
    Pfname = request.form['Pfname']
    PLname = request.form['PLname']
    Pemail = request.form['Pemail']
    PPhone = request.form['PPhone']
    Address = request.form['Address']
    p_event_res_dt = datetime.datetime.now().isoformat(timespec='seconds')#.timestamp()
    p_event_status = "In process"
    savePrivteEventToDB(p_event_type, p_event_name, Food_prefernces, p_event_date, PAmount, Pfname, PLname, Pemail, PPhone, Address, p_event_res_dt, p_event_status)
    flash('private event ordered')
    return redirect('/home')