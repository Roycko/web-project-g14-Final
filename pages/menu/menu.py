from flask import Blueprint, render_template,request,redirect,url_for
from interact_with_DB import interact_db
import datetime
from flask import session
from flask import flash
import flask
from utilities.general import *
import math

# menu blueprint definition
menu = Blueprint('menu', __name__,static_folder='static',static_url_path='/pages/menu/static', template_folder='templates')
title = 'Matamim | Menu'

# Routes
@menu.route('/menu')
def index():
    query = "select * from Products ;"
    products = interact_db(query=query, query_type='fetch')
    num_of_row=int(math.ceil(len(products)/3))
    return render_template('menu.html',title = title,temp_products=products,products=products,num_of_row=num_of_row)
#######################################################################
# New Code- dont work well, need to get the qt, product_id from the form ###########
 ######################################################################
    @menu.route('/addProduct', methods=['POST'])
    def add_to_cart():
        # products = request.form
        cart = getCart()[0][1]
        quantity = request.form.get("qt")
        product = request.form.get("current_product")
        insertProductToCart(product, quantity, cart)
        return redirect(url_for('menu.index'))

    #######################################################################
########################## End New Code ###############################
   #######################################################################

@menu.route('/menu_search', methods=['get'])
def menu_search_func():
    query = "select * from Products ;"
    # name = request.form['name']
    if request.args.get("radAnswer") == 'vegan':
             query = "select * from Products where is_vegan=1 ;"
    if request.args.get("radAnswer") == 'gluten':
             query = "select * from Products where is_gluten_free=1;"
    if request.args.get("radAnswer") == 'birthday':
             query = "select * from Products where is_birthday_cake=1 ;"
    if request.args.get("radAnswer") == 'top':
            query = "select * from Products where is_top_seller=1 ;"
    if request.args.get("radAnswer") == 'all':
            query = "select * from Products;"
    # if request.form.get("vegan") != None:
    #     is_vegan = '1'
    # else:
    #     is_vegan = '0'
    # if request.form.get("gluten") != None:
    #     is_gluten_free = '1'
    # else:
    #     is_gluten_free = '0'
    # if request.form.get("birthday") != None:
    #     is_birthday = '1'
    # else:
    #     is_birthday = '0'
    # if request.form.get("top") != None:
    #     is_top = '1'
    # else:
    #     is_top = '0'
    # if request.form.get("all") != None:
    #     is_all = '1'
    # else:
    #     is_all = '0'
    products = interact_db(query=query, query_type='fetch')
    num_of_row = int(math.ceil(len(products)/ 3))
    return render_template('menu.html',title = title,products=products,temp_products=products,num_of_row=num_of_row)