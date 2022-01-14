from flask import Blueprint, render_template,session
from interact_with_DB import interact_db,interact_db_json
import json
# cart blueprint definition
cart = Blueprint('cart', __name__, static_folder='cart', static_url_path='/static', template_folder='templates')
title ='Matamim | Your Cart'

# Routes
@cart.route('/cart')
def cart_func():
    query = f"select * from Carts where user_id = {session['user_id']} and status = 'active'"
    cart = interact_db(query,"fetch")
    if len(cart) == 0:
        maxCartQuery = f"select max(cart_id) as 'maxCart'  from carts  where user_id = {session['user_id']} group by user_id"
        maxCartId = interact_db(maxCartQuery,"fetch")
        print(maxCartId)
        if len(maxCartId) == 0:
            newCartQuery = f"insert into carts (user_id,cart_id,status) values ('{session['user_id']}','1','active')"
        else:
            maxCartId = maxCartId[0].maxCart
            print(maxCartId)
            newCartQuery = f"insert into carts (user_id,cart_id,status) values ('{session['user_id']}','{maxCartId+1}','active')"
        interact_db(newCartQuery,"commit")
    returnedCartQuery = f"select c.user_id, c.cart_id, p.*    from carts c join product_in_cart pic on c.cart_id = pic.cart_id join products p on pic.product_id = p.product_id where c.user_id = {session['user_id']} and c.status = 'active'"
    returnedCart = interact_db_json(returnedCartQuery,"fetch")
    return render_template('cart.html',title = title, products = returnedCart)

