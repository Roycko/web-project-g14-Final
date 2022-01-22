from flask import Blueprint, render_template

# events blueprint definition
events = Blueprint('events', __name__,static_folder='static',static_url_path='/pages/events/static', template_folder='templates')
title = 'Matamim | Our Events'

# Routes
@events.route('/events')
def index():
    return render_template('events.html',title = title)
