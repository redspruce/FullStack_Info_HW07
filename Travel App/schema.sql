-- Insert code to create Database Schema
-- This will create your .db database file for use
drop table if exists trips;
create table trips (
	trip_id integer primary key,
	triptitle text not null,
	destination text not null,
	creator text not null,
	friend text not null
);

drop table if exists users;
create table users (
	user_id integer primary key,
	username text not null,
	password text not null
);

-- drop table if exists friends;
-- create table friends (
-- 	id integer primary key,
-- 	trip_id text not null,
-- 	user_id text not null,
-- 	friend_id text not null,
-- 	FOREIGN KEY(trip_id) REFERENCES trips(trip_id),
-- 	FOREIGN KEY(user_id) REFERENCES users(user_id)
-- );


-- drop table if exists orders;
-- create table orders (
-- 	order_id integer primary key,
-- 	name_of_part text not null,
-- 	manufacturer_of_part text not null,
-- 	customer_id integer not null,
-- 	FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
-- );

-- drop table if exists orders_customers;
-- create table orders_customers (
-- 	orders_customers_id integer primary key,
-- 	order_id integer not null,
-- 	customer_id integer not null,
-- 	FOREIGN KEY(order_id) REFERENCES orders(order_id),
-- 	FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
-- );