/*
CONSTRAINTS
NOT NULL - Ensures that a column cannot have a NULL value
UNIQUE - Ensures that all values in a column are different
PRIMARY KEY - A combination of a NOT NULL and UNIQUE. Uniquely identifies each row in a table
FOREIGN KEY - Prevents actions that would destroy links between tables
CHECK - Ensures that the values in a column satisfies a specific condition
DEFAULT - Sets a default value for a column if no value is specified
*/

-- DDL (Data Definition Language) Commands: they are used to define the database schema
-- 1) create database/objects
create database ola;
use ola;

-- creating tables:
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
    amount int(10) not null,
    mode varchar(30) check(mode in('upi','credit','debit','cash')),
    status varchar(30),
    foreign key(driver_id) references drivers(driver_id),
    foreign key(user_id) references users(user_id)
);

-- 2) drop database/objects => It is used to delete a database or objects like table

-- 3) alter table - to modify structure of database
alter table users
add email varchar(10);

-- delete a column 
alter table users
drop column email;

-- rename column 
alter table payment
rename column amount to amt ;

-- 4) truncate table tablename => deletes the data inside a table, but not the table itself

-- DML (Data Manipulation Language) commands: used to manipulate data present in the database
-- 1) #Inserting values into tables
insert into users values(001,'Ram',15,1232354624,'Mumbai');
insert into users values(002,'Jay',30,1232354624,'Delhi');
insert into users values(003,'Benett',50,1232354624,'Delhi');
insert into users values(004,'James',15,1232354624,'Mumbai');

#Inserting values into customer table
insert into drivers (driver_id, driver_name, driver_phoneno, d_vehicle) values
(101,'Ravi',306546213,'Ertiga'),
(102,'Rahul',654656545,'Swift'),
(103,'Lewis',323456578,'Safari'),
(104,'Purvesh',545781528,'Nexon'),
(105,'Max',356497512,'Swift Dzire');

#inserting values into payments table
insert into payment values(1,101,001,2700,'upi','completed');
insert into payment values(2,102,002,18000,'credit','completed');
insert into payment values(3,103,003,900,'debit','in process');

-- 2) update => update existing data within a table
update users
set address = 'Chennai'
where username = 'James';

-- 3) delete - Delete records from a database table
delete from drivers
where driver_name = 'Purvesh';
