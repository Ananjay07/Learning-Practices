create database cars;
use cars;
create table users
(
	user_id int(5) primary key,
    username varchar(20) not null,
    user_age varchar(3) not null,
    u_phone_no int(11) not null
);

create table brands
(
	brand_id int(3) primary key,
    b_name varchar(20) not null
);

create table model
(
	model_id int(5) primary key,
    brand_id int(5) not null,
    model varchar(10) not null,
    price int(10),
    make_year int(5),
    color varchar(20),
    foreign key(brand_id) references brands(brand_id)
);

create table payment
(
	pay_id int(5) primary key,
    user_id int(5) not null,
    model_id int(5) not null, 
    amt int(10) not null,
    pmode varchar(10) not null
);

insert into users values(001,'Ram',15,1232354624);
insert into users values(002,'Jay',30,1232354624);
insert into users values(003,'Benett',50,1232354624);
insert into users values(004,'James',15,1232354624);

insert into brands values(101,"Mercedes");
insert into brands values(102,"BMW");
insert into brands values(103,"Porsche");
insert into brands values(104,"Ford");

insert into model values(1001,101,"GLS 600",9800000,2023,"White"); 
insert into model values(1002,104,"Mustang",2900000,2021,"Red"); 
insert into model values(1003,102,"M4",5400000,2023,"Black"); 
insert into model values(1004,103,"Panamera",3600000,2022,"Beige");
insert into model values(1005,102,"Z4",6000000,2022,"Black");

insert into payment values(201,001,1001,1800000,"Credit");
insert into payment values(202,003,1004,2900000,"Credit");
insert into payment values(203,004,1002,900000,"Credit");
ALTER TABLE payment
ADD COLUMN timestamp TIMESTAMP;
UPDATE payment
SET timestamp = '2024-05-01 08:00:00'
WHERE pay_id = 1;
UPDATE payment
SET timestamp = '2024-05-01 08:10:00'
WHERE pay_id = 2;
UPDATE payment
SET timestamp = '2024-05-01 08:15:00'
WHERE pay_id = 3;

-- Subqueries - a query within another query
-- Types of subqueries:
-- 1) Single row subquery - Subqueries that can return only one or zero rows to the outer statement 
-- WHERE or HAVING is used
select username from users
where user_age=(select user_age from users
order by user_age
desc limit 1);  		-- This shows the eldest user using single row subquery

-- 2) Multiple-Row Subqueries - Subqueries that can return more than one row but only one column
-- IN, ANY or ALL is used
SELECT username FROM users
WHERE user_id IN (SELECT user_id FROM payment);			-- This shows all the users that have done the payment using Multiple Row subquery

-- 3) Correlateed queries - a subquery that refers to a column from the outer query
SELECT username, user_age
FROM users
WHERE user_age = (
    SELECT AVG(user_age)
    FROM payment
    WHERE users.user_id = payment.user_id);     	-- This shows the name and age of the users who are in the payment table using correlated subquery
    
-- Joins:
-- Inner join with subquery - 
SELECT u.username, p.pay_id, p.amt FROM users u
INNER JOIN (
    SELECT * FROM payment
) p ON u.user_id = p.user_id
WHERE p.model_id IN (
    SELECT m.model_id
    FROM model m
    INNER JOIN brands b ON m.brand_id = b.brand_id
    WHERE b.b_name = 'Mercedes'
);

-- RIGHT JOIN with date and time functions
SELECT u.username, p.pay_id, p.amt, p.pmode, p.timestamp
FROM users u
RIGHT JOIN payment p ON u.user_id = p.user_id
WHERE p.pay_id IS NULL OR p.pmode = 'Credit';

-- #Analytics functions
-- Window functions - used to perform operations on a set of rows while still retaining the original structure of the data
-- 1) RANK() - gives a rank to each row within a partition. If rows have the same value they will have same rank. 
SELECT model_id, model, price, RANK() OVER (ORDER BY price DESC) AS price_rank
FROM model;

-- 2) DENSE_RANK() - similar to RANK(), but it does not create gaps when there are ties. 
SELECT model_id, model, price, 
DENSE_RANK() OVER (ORDER BY price DESC) AS price_rank
FROM model;

-- 3) ROW_NUMBER() - assigns a unique row number to each record in a partitioned or ordered set
SELECT ROW_NUMBER() OVER (ORDER BY user_age DESC) AS row_num, user_id, username, user_age, u_phone_no
FROM users;

-- 4) CUME_DIST - shows the relative position of a row within a data set, indicating what fraction of the data set is at or below a particular value
SELECT model_id, amt,
       CUME_DIST() OVER (ORDER BY amt) AS cumulative_distribution
FROM payment;

-- 5) The LAG() - provides access to a row at a specified physical offset prior to the current row within the partition
SELECT model, price, color, LAG(price) OVER (PARTITION BY color ORDER BY price) AS lag_price
FROM model;

-- 6) The LEAD() - provides access to a row at a specified physical offset after the current row within the partition.
SELECT model, price, color, LEAD(price) OVER (PARTITION BY color ORDER BY price) AS lag_price
FROM model;