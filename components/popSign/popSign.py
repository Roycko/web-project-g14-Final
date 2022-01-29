from flask import Blueprint, render_template, redirect
from flask import request
# session is global veriable- relevent for all the pages

# popSign blueprint definition
popSign = Blueprint('popSign', __name__,static_folder='static',static_url_path='/pages/popSign/static', template_folder='templates')


