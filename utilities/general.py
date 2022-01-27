from utilities.db.db_manager import dbManager
from utilities.entities.user import User
from utilities.entities.product import Product
from flask import session

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

# def hasAcart():
#     query = f"select * from Carts where user_id = {session['user_id']} and status = 'active'"
#     cart = dbManager.fetch(query)
#     if len(cart) == 0:
#         return False
#     else:
#         return True

def hasActiveCart():
    query = f"select * from Carts where user_id = {session['user_id']} and status = 'active'"
    cart = dbManager.fetch(query)
    if len(cart) == 0:
        return False
    else:
        return True

def getCart():
    returnedCartQuery = f"select c.user_id, c.cart_id, p.*,pic.quantity from carts c join product_in_cart pic on c.user_id = pic.user_id right join products p on pic.product_id = p.product_id where pic.user_id = {session['user_id']} and c.status = 'active'"
    returnedCart = dbManager.fetch(returnedCartQuery)
    return returnedCart

def createCart():
    maxCartQuery = f"select max(cart_id) as 'maxCart'  from carts  where user_id = {session['user_id']} group by user_id"
    maxCartId = dbManager.fetch(maxCartQuery)
    print(maxCartId)
    if len(maxCartId) == 0:
        newCartQuery = f"insert into carts (user_id,cart_id,status) values ('{session['user_id']}','1','active')"
    else:
        maxCartId = maxCartId[0].maxCart
        print(maxCartId)
        newCartQuery = f"insert into carts (user_id,cart_id,status) values ('{session['user_id']}','{maxCartId+1}','active')"
    dbManager.commit(newCartQuery)
    returnedCartQuery = f"select c.user_id, c.cart_id, p.* ,pic.quantity from carts c join product_in_cart pic on c.user_id = pic.user_id join products p on pic.product_id = p.product_id where pic.user_id = {session['user_id']} and c.status = 'active'"
    returnedCart = dbManager.fetch(returnedCartQuery)
    return returnedCart

def updateCart(product,quantity,cart):
    updateQuery = f"update product_in_cart set quantity = {quantity} where cart_id = {cart} and product_id = {product}"
    dbManager.commit(updateQuery)

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

def saveContactToDB(fname,lname,email,msg):
    query = f"insert into contact_us (first_name,last_name,email_address,message) values ('{fname}','{lname}','{email}','{msg}')"
    affected_rows = dbManager.commit(query)
    return affected_rows ==1

