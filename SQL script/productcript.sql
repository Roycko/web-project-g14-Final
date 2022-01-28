insert into Products(name,num_of_pcs,price,image_src,is_birthday_cake,is_gluten_free,is_top_seller,is_vegan)
 values ('Raspberries Cheese Cake','1','15','/static/img/products/cheesecake1.jpg','1','0','1','0');
insert into Products(name,num_of_pcs,price,image_src,is_birthday_cake,is_gluten_free,is_top_seller,is_vegan)
 values ('Blue Berries Cheese Cake','2','15','/static/img/products/cheesecake4.jpg','0','0','1','0');
insert into Products(name,num_of_pcs,price,image_src,is_birthday_cake,is_gluten_free,is_top_seller,is_vegan)
 values ('Passion Fruit Cheese Cake','3','15','/static/img/products/cheesecake3.jpg','0','0','0','0');
insert into Products(name,num_of_pcs,price,image_src,is_birthday_cake,is_gluten_free,is_top_seller,is_vegan)
 values ('Raspberries Cheese Cake','4','15','/static/img/products/cheesecake2.jpg','1','1','1','1');

# truncate  table products;

insert into Product_in_Cart(product_id,user_id,cart_id,quantity)
 values ('3','1','1','2');
