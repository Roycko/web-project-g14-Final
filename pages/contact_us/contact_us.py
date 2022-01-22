from flask import Blueprint, render_template

# contact_us blueprint definition
contact_us = Blueprint('contact_us', __name__,static_folder='static',static_url_path='/pages/contact_us/static', template_folder='templates')
title ='Matamim | Contact Us'

# Routes
@contact_us.route('/contact_us')
def index():
    return render_template('contact_us.html',title = title)
