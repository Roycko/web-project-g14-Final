from flask import Blueprint, render_template

# edit_events blueprint definition
edit_events = Blueprint('edit_events', __name__,static_folder='static',static_url_path='/pages/edit_events/static', template_folder='templates')
title = 'Matamim | Edit your Event'

# Routes
@edit_events.route('/edit_events')
def index():
    return render_template('edit events.html',title = title)
