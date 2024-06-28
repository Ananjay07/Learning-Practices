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

-- TCL (Transaction control language) Commands
-- TCL commands are used to manage transactions, maintain ACID properties, and control the flow of data modifications.
-- TCL commands ensure the consistency and durability of data in a database.

-- commit - Saves a transaction to the database
commit;
-- rollback - Undoes a transaction or change that hasn't been saved to the database
rollback;

-- savepoint - Temporarily saves a transaction for later rollback 
savepoint a;

In mysql it is having auto commit so is doesnot make anysense transaction commands in mysql
for this we have to use command start transaction


-- Triggers -- a system executes automatically when there is any modification to the database
-- It is of 6 types 



-- 5)before update -- activated before data in the table is modified.
-- 6)before delete --  activated before data is deleted/removed from the table. 

-- 1)after insert -- activated after data is inserted into the table.
DELIMITER //
CREATE TRIGGER model_after_insert
AFTER INSERT ON brands
FOR EACH ROW
BEGIN
  INSERT INTO brand_log (brand_id, b_name, inserted_at)
  VALUES (NEW.brand_id, NEW.b_name, NOW());
END //
DELIMITER ;

-- 2)after update -- activated after data in the table is modified. 
-- SQL trigger to log changes made to product information whenever an update occurs in the 'brands' table?
DELIMITER //
CREATE TRIGGER brand_after_update
AFTER UPDATE ON brands
FOR EACH ROW
BEGIN
  IF OLD.brand_id <> NEW.brand_id OR OLD.b_name <> NEW.b_name THEN
    INSERT INTO brand_log (brand_id, b_name, updated_at)
    VALUES (OLD.brand_id, OLD.b_name, NOW());
  END IF;
END //
DELIMITER ;


-- 3)after delete -- activated after data is deleted/removed from the table.
DELIMITER //
CREATE TRIGGER brand_after_delete
AFTER DELETE ON brands
FOR EACH ROW
BEGIN
  DECLARE has_brand INT DEFAULT (0);
  SELECT COUNT(*) INTO has_brand
  FROM brands
  WHERE brand_id = OLD.brand_id;

  IF has_brand > 0 THEN
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot delete brand with existing models. Update or delete model first.';
  END IF;
END //
DELIMITER ;

-- 4)before insert -- activated before data is inserted into the table. 
#Trigger for Automatic Payment Status on Payment Insert
DELIMITER //
CREATE TRIGGER set_default_payment_status
BEFORE INSERT ON payment
FOR EACH ROW
BEGIN
  IF NEW.status IS NULL THEN
    SET NEW.status = 'Pending';
  END IF;
END //
DELIMITER ;

-- Triggers can validate data before it's inserted or updated, ensuring it adheres to specific rules. 
-- Triggers can automatically maintain relationships between tables.
-- Triggers can implement complex business rules that might not be easily achievable with standard SQL statements. 
-- Triggers can enforce data access restrictions or security checks on specific events within the database.
-- Triggers can introduce overhead to data manipulation operations. Analyze their impact on performance and optimize them if necessary.
-- When using multiple triggers, their execution order can be important. Define the order in which triggers fire to ensure desired results.

