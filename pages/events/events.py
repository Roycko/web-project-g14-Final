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
    query_events = "Select * from events"
    events = dbManager.fetch(query_events)
    return render_template('events.html',title = title, events = events)


@events.route('/bookEvent', methods = ["POST"])
def bookEvents_func():
    user_id = session['user_id']
    for k,v in request.form.items():
        event_id = k
    bookEventToDB(event_id,user_id)
    return redirect(url_for('events.index'))
