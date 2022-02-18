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
    query_events = "Select * from events where is_personal = 0"
    events = dbManager.fetch(query_events)
    return render_template('events.html',title = title, events = events)


@events.route('/bookEvent', methods = ["POST"])
def bookEvents_func():
    user_id = session['user_id']
    for k,v in request.form.items():
        event_id = k
    bookEventToDB(event_id,user_id)
    return redirect(url_for('events.index'))

@events.route('/savePrivateEvent' , methods = ["POST"])
def privateEvent_func():
    event_name = request.form["p_event_name"]
    food_type = request.form["Food_prefernces"]
    event_date = request.form["p_event_date"]
    print(event_date)
    amount = request.form["PAmount"]
    place = request.form["Address"]
    is_personal = 1
    status = "Open"
    addPersonalEvent(is_personal, event_name, status, event_date, place, food_type, amount)
    return redirect(url_for('events.index'))