create database ola1;
use ola1;
create table users
(
	user_id int(5) primary key,
    username varchar(20) not null,
    user_age varchar(3) not null,
    u_phone_no int(11) not null,
    address varchar(40) not null
);
create table drivers
(
	driver_id int(5) primary key,
    driver_name varchar(20) not null,
    driver_phoneno int(11) not null,
    d_vehicle varchar(20) not null
);
create table payment
(
	pay_id int(5) primary key,
    driver_id int(5) not null,
    user_id int(5) not null,
    amt int(10) not null,
    mode varchar(30) check(mode in('upi','credit','debit','cash')),
    status varchar(30),
    foreign key(driver_id) references drivers(driver_id),
    foreign key(user_id) references users(user_id)
);

insert into users values(001,'Ram',15,1232354624,'Mumbai');
insert into users values(002,'Jay',30,1232354624,'Delhi');
insert into users values(003,'Benett',50,1232354624,'Delhi');
insert into users values(004,'James',15,1232354624,'Mumbai');

insert into drivers (driver_id, driver_name, driver_phoneno, d_vehicle) values
(101,'Ravi',306546213,'Ertiga'),
(102,'Rahul',654656545,'Swift'),
(103,'Lewis',323456578,'Safari'),
(104,'Purvesh',545781528,'Nexon'),
(105,'Max',356497512,'Swift Dzire');

insert into payment values(1,101,001,2700,'upi','completed');
insert into payment values(2,102,002,18000,'credit','completed');
insert into payment values(3,103,003,900,'debit','in process');

-- There are 6 types of joins:
-- 1) Inner Join - Matching values from both tables should be present
SELECT users.username, user_age, payment.amt FROM users
INNER JOIN payment ON users.user_id = payment.user_id;   -- here inner join is used to join columns from users, drivers and payment table


-- 2) Left Outer Join - All the rows from the left table should be present and matching rows from the right table are present
SELECT users.username, user_age, payment.amt FROM users
LEFT JOIN payment ON users.user_id = payment.user_id;

-- 3) Right Join-> All the rows from the right table should be present and only matching rows from the left table are present 
SELECT users.username, user_age, payment.amt FROM payment
RIGHT JOIN users ON users.user_id = payment.user_id;

-- 4) Full Join-> All the rows from both the table should be present 
SELECT * FROM users
FULL JOIN payment;

#5.Self Join-> It is a regular join, but the table is joined by itself
SELECT u1.username, u2.username FROM users u1
INNER JOIN users u2 ON u1.u_phone_no = u2.u_phone_no
WHERE u1.user_id <> u2.user_id;

#6.Cross Join-> It is used to view all the possible combinations of the rows of one table and with all the rows from second table
SELECT * FROM users
CROSS JOIN drivers;
