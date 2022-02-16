from utilities.db.db_manager import dbManager
from utilities.entities.user import User
from utilities.entities.product import Product
from flask import session,flash

def get_all_users():
    query = "select * from Users"
    res = dbManager.fetch(query)
    users_list = []
    for row in res:
        user = User(row[1],row[2],row[3],row[4],row[5],row[6],row[7])
        users_list.append(user)
    return users_list

def get_all_products():
    query = "select * from Products"
    res = dbManager.fetch(query)
    products_list =[]
    for row in res:
        product = Product(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
        products_list.append(product)
    return products_list

def get_all_products_as_table():
    query = "select * from Products"
    res = dbManager.fetch(query)
    return res
# def hasAcart():
#     query = f"select * from Carts where user_id = {session['user_id']} and status = 'active'"
#     cart = dbManager.fetch(query)
#     if len(cart) == 0:
#         return False
#     else:
#         return True


## ------------- CARTS ---------------- ##

def hasActiveCart():
    query = f"select * from Carts where user_id = {session['user_id']} and status = 'active'"
    cart = dbManager.fetch(query)
    if cart:
        return True
    else:
        return False

def getCart():
    returnedCartQuery = f"select c.user_id, c.cart_id, p.*,pic.quantity from carts c join product_in_cart pic on c.user_id = pic.user_id and c.cart_id=pic.cart_id right join products p on pic.product_id = p.product_id where pic.user_id = {session['user_id']} and c.status = 'active'"
    returnedCart = dbManager.fetch(returnedCartQuery)
    return returnedCart

def getCartID():
    returnedCartQuery = f"select  c.cart_id from carts c where c.user_id = {session['user_id']} and c.status = 'active'"
    returnedCart = dbManager.fetch(returnedCartQuery)
    return returnedCart

def createCart():
    maxCartQuery = f"select max(cart_id) as 'maxCart'  from carts  where user_id = {session['user_id']} group by user_id"
    maxCartId = dbManager.fetch(maxCartQuery)
    print(maxCartId)
    if maxCartId:
        maxCartId = maxCartId[0].maxCart
        print(maxCartId)
        newCartQuery = f"insert into carts (user_id,cart_id,status) values ('{session['user_id']}','{maxCartId + 1}','active')"

    else:
        newCartQuery = f"insert into carts (user_id,cart_id,status) values ('{session['user_id']}','1','active')"
    dbManager.commit(newCartQuery)
    returnedCartQuery = f"select c.user_id, c.cart_id, p.* ,pic.quantity from carts c join product_in_cart pic on c.user_id = pic.user_id join products p on pic.product_id = p.product_id where pic.user_id = {session['user_id']} and c.status = 'active'"
    returnedCart = dbManager.fetch(returnedCartQuery)
    return returnedCart

def updateCart(product,quantity,cart):
    updateQuery = f"update product_in_cart set quantity = {quantity} where cart_id = {cart} and product_id = {product}"
    dbManager.commit(updateQuery)


## ------------- Products ---------------- ##

def removeProducts(products,cart):
    quary = f"select product_id from product_in_cart where user_id = {session['user_id']} and cart_id = {cart}"
    notIn = dbManager.fetch(quary)
    products = list(products)
    # res_list =[]
    # print(notIn)
    row = [str(item[0]) for item in notIn]
    print(row)
    print(products)
    removed = list(set(row) - set(products))
    print(removed)
    print(tuple(removed))
    # print(len(tuple(removed)))
    if len(removed) == 0:
        return True
    if len(removed) == 1:
        quary2 = f"delete from product_in_cart where product_id = {removed[0]} and user_id = {session['user_id']} and cart_id = {cart}"
    else:
        quary2 = f"delete from product_in_cart where product_id in {tuple(removed)} and user_id = {session['user_id']} and cart_id = {cart}"
    print(dbManager.commit(quary2))

def insertProductToCart(product,quantity,cart):
        quary2 = f" insert into Product_in_Cart(product_id, user_id, cart_id, quantity) values({product}, {session['user_id']}, {cart}, {quantity})";
        dbManager.commit(quary2)




## ------------- Users ---------------- ##


def getUser(email):
    query = f"select * from users where email_address='{email}'"
    res = dbManager.fetch(query)
    return res[0]

def update_user(email,password, firstName, lastName):
    if password !='':
        query = f"UPDATE users SET password={password}, first_name='{firstName}', last_name='{lastName}' where email_address='{email}'"
    else:
        query = f"UPDATE users SET first_name='{firstName}', last_name='{lastName}' where email_address='{email}'"
    affected_rows = dbManager.commit(query)
    return affected_rows == 1

def is_email_not_availabe(email):
    query = "select * from Users where email_address='%s'" % (email)
    return dbManager.fetch(query)

def is_user_pass_not_availabe(user_name,password):
    query = "select * from Users where user_name='%s' and password='%s' ;" % (user_name, password)
    return dbManager.fetch(query)

## ------------- Contact us ---------------- ##


def saveContactToDB(fname,lname,email,msg):
    query = f"insert into contact_us (first_name,last_name,email_address,message) values ('{fname}','{lname}','{email}','{msg}')"
    affected_rows = dbManager.commit(query)
    return affected_rows ==1

## ------------- Orders (payments) ---------------- ##

def getCartPrice():
    cart = getCart()
    fPrice =0
    for row in cart:
        price = row[5]*row[11]
        fPrice +=price
    finalPrice = fPrice
    return finalPrice

def closeCart(cart_id):
    status = "inactive"
    query = f"UPDATE carts SET status='{status}' where cart_id='{cart_id}' and user_id = '{session['user_id']}'"
    affected_rows = dbManager.commit(query)
    return affected_rows == 1

def savePaymentToDB(user_id, cart_id, shippingMethod, address, totalPrice, order_status, reservation_dt):
    query = f"insert into orders (user_id, cart_id, shipping_method, address, total_price, order_status, reservation_dt) values ('{user_id}','{cart_id}', '{shippingMethod}','{address}', '{totalPrice}', '{order_status}', '{reservation_dt}')"
    closeCart(cart_id)
    affected_rows = dbManager.commit(query)
    return affected_rows ==1

def cartForUser():
    if session['user_id'] is not None:
        if not hasActiveCart():
            createCart()
    return True

def menu_search(is_vegan,is_gluten_free,is_birthday_cake,is_top_seller,all):
    query = "select * from Products;"
    if is_vegan == 1:
        query = "select * from Products where is_vegan=1 ;"
    if is_gluten_free == 1:
        query = "select * from Products where is_gluten_free=1;"
    if is_birthday_cake == 1:
        query = "select * from Products where is_birthday_cake=1 ;"
    if  is_top_seller == 1:
        query = "select * from Products where is_top_seller=1 ;"
    if all == 1:
        query = "select * from Products;"
    products = dbManager.fetch(query)
    return products

## ------------- Events ---------------- ##
def checkForCapacity(event_id):
    query_capacity = f"select max_occupancy from events where event_id = {event_id}"
    max_capacity = dbManager.fetch(query_capacity)[0][0]
    user_query = f"select * from users_in_events where event_id={event_id} and user_id={session['user_id']}"
    if len(dbManager.fetch(user_query))==1:
        flash('Already Booked!')
        return False
    query = f"select count(distinct user_id,event_id) as 'amount' from users_in_events where event_id = {event_id}"
    cur_capacity = dbManager.fetch(query)[0][0]
    if cur_capacity >= max_capacity:
        flash("Event is Full")
        return False
    else:
        flash("Event Booked!")
        return True
    # print(max_capacity)
    # print(cur_capacity)

def bookEventToDB(event_id, user_id):
    if checkForCapacity(event_id):
        query = f"insert into users_in_events (event_id, user_id) VALUES ({event_id},{user_id})"
        exec = dbManager.commit(query)
        return exec == 1
    return True

def getMyEvents():
    query = f"select e.*, ue.event_id as e_id, ue.user_id from events e left join users_in_events ue on e.event_id=ue.event_id where ue.user_id = {session['user_id']} and e.event_dt > NOW()"
    myEvents = dbManager.fetch(query)
    return myEvents

