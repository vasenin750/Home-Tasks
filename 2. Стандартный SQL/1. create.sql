create table customers
(
id serial primary key,
name varchar(100) not null,
email varchar(255) unique not null
)

create table orders
(
id serial primary key,
customer_id integer not null,
foreign key (customer_id) references customers (id) on delete cascade,
order_date timestamptz default now()
)

create table orders_items
(
id serial primary key,
order_id integer not null,
foreign key (order_id) references orders (id) on delete cascade,
product_name varchar(100) not null,
quantity integer not null check (quantity>0),
price float not null check (price>=0)
)






/* 
--drop
drop table customers
drop table orders
drop table orders_items 
*/