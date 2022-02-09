from flask import Blueprint, render_template,session,request,redirect,url_for
from utilities.general import *
import datetime
from flask import flash


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
    user_id = session['user_id']
    cart_id = getCart()[0][1]
    shippingMethod = request.form.get('shippingMethod')
    address = request.form['address']
    totalPrice = getCartPrice()
    reservation_dt = datetime.datetime.now().isoformat(timespec='seconds')#.timestamp()
    order_status = "In process"
    savePaymentToDB(user_id, cart_id, shippingMethod, address, totalPrice, order_status, reservation_dt)
    flash('Cart Paid')
    return redirect('/home')

