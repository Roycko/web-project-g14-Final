--  drop DATABASE web_project_g14;
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

-- !!!!!!!! cart id not incremantel
CREATE TABLE web_project_g14.Carts (
user_id int ,
cart_id int ,
-- current_price float,-- prefer to calculte in the JS or code and not change in the DB all the time
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
