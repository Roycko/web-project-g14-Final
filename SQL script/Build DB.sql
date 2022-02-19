#   drop DATABASE web_project_g14;
CREATE DATABASE web_project_g14;

CREATE TABLE web_project_g14.Users (
user_id int auto_increment PRIMARY KEY,
email_address VARCHAR(30),
first_name varchar(20),-- Add in the sign up form
last_name varchar(20),-- Add in the sign up form
user_name VARCHAR(20),
password VARCHAR(20),
birth_date date,-- Add in the sign up form
Registration_DT datetime
);


CREATE TABLE web_project_g14.Carts (
user_id int ,
cart_id int ,
status varchar(20), -- close/ order / open - show only the open -- only one open cart for each user, if close/ order open new one automaticly 
constraint fk_users FOREIGN KEY (user_id) references Users(user_id),
constraint pk_Carts primary key (user_id,cart_id)
);

CREATE TABLE web_project_g14.Products (
product_id int auto_increment primary key ,
name varchar(60),
num_of_pcs int,
price int,
image_src varchar(60),
is_vegan bool,
is_gluten_free bool,
is_birthday_cake bool,
is_top_seller bool
);

CREATE TABLE web_project_g14.Product_in_Cart (
product_id int ,
user_id int ,
cart_id int ,
quantity int,
constraint pk_product_in_cart primary key (user_id,cart_id,product_id)
);

CREATE TABLE web_project_g14.Orders (
order_id int auto_increment  PRIMARY KEY,
user_id int,
cart_id int,
shipping_method VARCHAR(20),
address VARCHAR(20),
total_price float,
reservation_dt datetime,
constraint fk_carts FOREIGN KEY (user_id,cart_id) references Carts(user_id,cart_id)-- when click on payment from cart save here the cart (new raw in table with the cart price) , and when finish the order to update the status on the cart
);

CREATE TABLE web_project_g14.Events (
event_id int auto_increment primary key ,
is_personal bool,
event_type varchar(20),
event_name varchar(100),
status varchar(20),-- left, canceled, full booked, have place,personal 
event_dt datetime,
place varchar(20),
image_src varchar(60),
short_description varchar(400),
long_description varchar(1000),
Food_type varchar(20),
max_occupancy int,
amount int
);

CREATE TABLE web_project_g14.contact_us (
contact_id int auto_increment primary key  ,
first_name varchar(20),
last_name varchar(20),
email_address varchar(30),
message varchar(255)
);

CREATE TABLE web_project_g14.users_in_events (
event_id int,
user_id int,
constraint fk_users_event FOREIGN KEY (user_id) references Users(user_id),
constraint fk_users_event_2 FOREIGN KEY (event_id) references Events(event_id),
constraint pk_userInEvents primary key (event_id,user_id)
);
#   insert events records

insert into web_project_g14.Events(is_personal,event_type,event_name,status,event_dt,place,image_src,short_description,long_description,max_occupancy)
 values ('0','','Chocolate Workshop','Open',CURRENT_DATE(),'Office','/pages/events/static/img/Chocolate1.jpg','The chocolate workshop is a great activity for kids and adults, and is suitable for all ages.','The chocolate workshop is a great activity for kids and adults, and is suitable for all ages. The tour begins with a 15 minute video about the origins of chocolate, and proceeds to a workshop room. At the workshops, each participant can choose their desired workshop, and still work around the same table.',50);
insert into web_project_g14.Events(is_personal,event_type,event_name,status,event_dt,place,image_src,short_description,long_description,max_occupancy)
 values ('0','','Home Made Marshmellos','Open',CURRENT_DATE(),'Office','/pages/events/static/img/Company_Happy_Hour.jpg','We are bringing the bakery to you. you can get your cakes and chocolates where ever you want.','We are bringing the bakery to you, now offering contactless delivery nationwide so you can get your cakes and chocolates were ever you want to.',50);
insert into web_project_g14.Events(is_personal,event_type,event_name,status,event_dt,place,image_src,short_description,long_description,max_occupancy)
 values ('0','','Make your waffle','Open',CURRENT_DATE(),'Office','/pages/events/static/img/Waffle_Event.jpg','Our classic workshop runs almost every day in the year! It lasts about 90 minutes.','Our classic workshop runs almost every week in the year! It lasts about 90 minutes, no previous cooking experience is needed and you can make as many waffles as you can eat!',50);

#   insert product records

insert into web_project_g14.Products(name,num_of_pcs,price,image_src,is_birthday_cake,is_gluten_free,is_top_seller,is_vegan)
 values ('Raspberries Cheese Cake1','1','15','/static/img/products/cheesecake1.jpg','1','0','1','0');
insert into web_project_g14.Products(name,num_of_pcs,price,image_src,is_birthday_cake,is_gluten_free,is_top_seller,is_vegan)
 values ('Blue Berries Cheese Cake1','2','15','/static/img/products/cheesecake4.jpg','0','0','1','0');
insert into web_project_g14.Products(name,num_of_pcs,price,image_src,is_birthday_cake,is_gluten_free,is_top_seller,is_vegan)
 values ('Passion Fruit Cheese Cake1','3','15','/static/img/products/cheesecake3.jpg','0','0','0','1');
insert into web_project_g14.Products(name,num_of_pcs,price,image_src,is_birthday_cake,is_gluten_free,is_top_seller,is_vegan)
 values ('Raspberries Cheese Cake1','4','15','/static/img/products/cheesecake2.jpg','1','1','1','1');

insert into web_project_g14.Products(name,num_of_pcs,price,image_src,is_birthday_cake,is_gluten_free,is_top_seller,is_vegan)
 values ('Raspberries Cheese Cake2','1','15','/static/img/products/cheesecake1.jpg','1','0','1','0');
insert into web_project_g14.Products(name,num_of_pcs,price,image_src,is_birthday_cake,is_gluten_free,is_top_seller,is_vegan)
 values ('Blue Berries Cheese Cake2','2','15','/static/img/products/cheesecake4.jpg','0','0','1','0');
insert into web_project_g14.Products(name,num_of_pcs,price,image_src,is_birthday_cake,is_gluten_free,is_top_seller,is_vegan)
 values ('Passion Fruit Cheese Cake2','3','15','/static/img/products/cheesecake3.jpg','0','0','1','0');
insert into web_project_g14.Products(name,num_of_pcs,price,image_src,is_birthday_cake,is_gluten_free,is_top_seller,is_vegan)
 values ('Raspberries Cheese Cake2','4','15','/static/img/products/cheesecake2.jpg','1','1','1','1');

insert into web_project_g14.Products(name,num_of_pcs,price,image_src,is_birthday_cake,is_gluten_free,is_top_seller,is_vegan)
 values ('Raspberries Cheese Cake3','1','15','/static/img/products/cheesecake1.jpg','1','0','1','0');
insert into web_project_g14.Products(name,num_of_pcs,price,image_src,is_birthday_cake,is_gluten_free,is_top_seller,is_vegan)
 values ('Blue Berries Cheese Cake3','2','15','/static/img/products/cheesecake4.jpg','0','0','1','0');
insert into web_project_g14.Products(name,num_of_pcs,price,image_src,is_birthday_cake,is_gluten_free,is_top_seller,is_vegan)
 values ('Passion Fruit Cheese Cake3','3','15','/static/img/products/cheesecake3.jpg','0','1','0','0');
insert into web_project_g14.Products(name,num_of_pcs,price,image_src,is_birthday_cake,is_gluten_free,is_top_seller,is_vegan)
 values ('Raspberries Cheese Cake3','4','15','/static/img/products/cheesecake2.jpg','1','1','1','1');

insert into web_project_g14.Products(name,num_of_pcs,price,image_src,is_birthday_cake,is_gluten_free,is_top_seller,is_vegan)
 values ('Raspberries Cheese Cake4','1','15','/static/img/products/cheesecake1.jpg','1','0','1','0');
insert into web_project_g14.Products(name,num_of_pcs,price,image_src,is_birthday_cake,is_gluten_free,is_top_seller,is_vegan)
 values ('Blue Berries Cheese Cake4','2','15','/static/img/products/cheesecake4.jpg','0','0','1','0');
insert into web_project_g14.Products(name,num_of_pcs,price,image_src,is_birthday_cake,is_gluten_free,is_top_seller,is_vegan)
 values ('Passion Fruit Cheese Cake4','3','15','/static/img/products/cheesecake3.jpg','1','0','0','0');
insert into web_project_g14.Products(name,num_of_pcs,price,image_src,is_birthday_cake,is_gluten_free,is_top_seller,is_vegan)
 values ('Raspberries Cheese Cake4','4','15','/static/img/products/cheesecake2.jpg','1','1','1','1');

# insert user record

insert into web_project_g14.Users(email_address,first_name,last_name,user_name,password,birth_date,registration_DT)
 values ('testuser@google.com','test','user','test_user','AB123123','1995-02-22','2022-02-05 14:41:16');
