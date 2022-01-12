from flask import Blueprint, render_template, redirect
from flask import request
# session is global veriable- relevent for all the pages
from interact_with_DB import interact_db

# popSign blueprint definition
popSign = Blueprint('popSign', __name__, static_folder='static', static_url_path='/popSign', template_folder='templates')


