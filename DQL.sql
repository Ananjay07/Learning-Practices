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
    make_year int(5),
    color varchar(20),
    foreign key(brand_id) references brands(brand_id)
);

insert into users values(001,'Ram',15,1232354624);
insert into users values(002,'Jay',30,1232354624);
insert into users values(003,'Benett',50,1232354624);
insert into users values(004,'James',15,1232354624);

insert into brands values(101,"Mercedes");
insert into brands values(102,"BMW");
insert into brands values(103,"Porsche");
insert into brands values(104,"Ford");

insert into model values(1001,101,"GLS 600",2023,"White"); 
insert into model values(1002,104,"Mustang",2021,"Red"); 
insert into model values(1003,102,"M4",2023,"Black"); 
insert into model values(1004,103,"Panamera",2022,"Beige"); 

-- DQL(Data Query Language) - used for performing queries on the data within schema objects
-- 1) GROUP BY - used to group rows that have the same values into summary rows
SELECT username, COUNT(*) AS Number
FROM users
GROUP BY username;
-- GROUP BY can also be used while using aggregate function like COUNT, MAX, MIN, AVG, SUM, etc

-- 2) ORDER BY - used for ordering rows in a specific way
-- 	i) BASIC - ORDER BY x (any datatype)

-- 	ii) ASCENDING
SELECT *
FROM model
ORDER BY make_year ASC;

-- 	iii) DESCENDING
SELECT *
FROM users
ORDER BY user_age DESC;

-- 3) HAVING BY - used in conjunction with the GROUP BY to filter groups based on a specified condition. 
-- The HAVING clause works similarly to the WHERE clause
SELECT username, user_age
FROM users
GROUP BY username, user_age
HAVING user_age > 18;

-- 4) SELECT - used to retrieve rows selected from one or more tables.
-- 	i) SELECT  distinct columns
-- The DISTINCT Clause after SELECT eliminates duplicate rows from the result set
SELECT DISTINCT model,make_year FROM model;

-- 	ii) SELECT all columns
SELECT * FROM brands;

-- D) SELECT with LIKE(%) - helps in searching using some syllables of the word
SELECT * FROM users WHERE username LIKE "%ay%";
SELECT * FROM model WHERE model LIKE "%mu%";

-- E) SELECT with CASE or IF
-- a) CASE
SELECT user_id,
	   username,
       CASE WHEN user_age > 18 THEN 'Can Drive' ELSE "Can't drive" END AS 'Remark'
FROM users;

-- b) IF
SELECT model,
	   make_year,
       IF(make_year > 2022, 'New', 'Old')AS 'Remark'
FROM model;

-- F) SELECT with a LIMIT
SELECT * 
FROM users
ORDER BY user_id
LIMIT 2;

-- G) SELECT with WHERE
SELECT * FROM model WHERE model = "Panamera";