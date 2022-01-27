from flask import Blueprint, render_template,session
from utilities.general import *
# payment blueprint definition
payment = Blueprint('payment', __name__, static_folder='payment', static_url_path='/static', template_folder='templates')
title = 'Matamim | Complete your purchase'

# Routes
@payment.route('/payment')
def index():
    finalPrice = getCartPrice()
    if getCartPrice() != 0:
        return render_template('payment.html',title = title,finalPrice = finalPrice)
    else:
        return render_template('payment.html', title=title)



@payment.route('/saveOrder', methods = ['POST'])
def saveOrder_func():

    ##move relevant cart to status = "Inactive" where user_id = session['user_id'] and status = "Active"
    return True