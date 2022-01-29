from flask import Blueprint, render_template,session,request,redirect,url_for
from utilities.general import *
from utilities.entities.product import *
from utilities.entities.user import *
import json
# cart blueprint definition
cart = Blueprint('cart', __name__,static_folder='static',static_url_path='/pages/cart/static', template_folder='templates')
title ='Matamim | Your Cart'

# Routes
@cart.route('/cart')
def cart_func():
    # if hasActiveCart():
    returnedCart= getCart()
    # else:
    #     returnedCart = createCart()
    return render_template('cart.html',title = title, products = returnedCart)

@cart.route('/saveChanges' , methods = ['POST'])
def save_cart():
    products = request.form
    cart = getCart()[0][1]
    removeProducts(products,cart)
    for product,quantity in products.items():
        quan = quantity
        updateCart(product,quan,cart)
    return redirect(url_for('cart.cart_func'))


