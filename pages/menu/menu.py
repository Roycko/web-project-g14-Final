from flask import Blueprint, render_template,request,redirect,url_for
import datetime
from flask import session
from flask import flash
import flask
from 
from utilities import *
from utilities.general import *
import math

# menu blueprint definition
menu = Blueprint('menu', __name__,static_folder='static',static_url_path='/pages/menu/static', template_folder='templates')
title = 'Matamim | Menu'

# Routes
@menu.route('/menu')
def index():
    products = get_all_products_as_table()
    num_of_row=int(math.ceil(len(products)/3))
    return render_template('menu.html',title = title,temp_products=products,products=products,num_of_row=num_of_row)
#######################################################################
# New Code- dont work well, need to get the qt, product_id from the form ###########
 ######################################################################
@menu.route('/addProduct', methods=['POST'])
def add_to_cart():
    # products = request.form
    cart = getCartID()[0][0]
    products = get_all_products()
    # query = "select * from Products ;"
    # products=dbManager.fetch(query)
    product=1
    quantity=1
    for i in range(len(products)):
        if 'submit'+str(i) in request.form:
            quantity = request.form.get("qt" + str(i))
            product = i
    #add only if the product not already in the cart
    Products_in_cart=getCart()
    in_cart=False
    for i in range(len(Products_in_cart)):
        if Products_in_cart[i][2]==product:
            in_cart=True
    if (in_cart):
        flash('Already in Cart')
    else:
        insertProductToCart(product, quantity, cart)
        flash('Product Added')
    return redirect(url_for('menu.index'))

    #######################################################################
########################## End New Code ###############################
   #######################################################################

@menu.route('/menu_search', methods=['get'])
def menu_search_func():
    products = menu_search(0, 0, 0, 0, 1)
    # name = request.form['name']
    if request.args.get("radAnswer") == 'vegan':
             products=menu_search(1,0,0,0,0)
    if request.args.get("radAnswer") == 'gluten':
            products = menu_search(0, 1, 0, 0, 0)
    if request.args.get("radAnswer") == 'birthday':
             products = menu_search(0, 0, 1, 0, 0)
    if request.args.get("radAnswer") == 'top':
            products = menu_search(0, 0, 0, 1, 0)
    num_of_row = int(math.ceil(len(products)/ 3))
    return render_template('menu.html',title = title,products=products,temp_products=products,num_of_row=num_of_row)