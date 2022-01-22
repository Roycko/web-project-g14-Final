from flask import Blueprint, render_template

# about blueprint definition
about = Blueprint('about', __name__,static_folder='static',static_url_path='/pages/about/static', template_folder='templates')
title ='Matamim | About'

# Routes
@about.route('/about')
def index():
    return render_template('about.html',title = title)
