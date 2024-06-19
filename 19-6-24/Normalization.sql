-- #NORMALIZATION
-- Normalization - It is a process of organizing tables in a database to reduce data redundancy and improve data integrity.

-- The different types of normalization are:
-- 1) First Normal Form (1NF)
-- Condition:
-- 	i)Each table cell contains a single atomic value.
-- 	ii) No repeating group

CREATE TABLE customers (
  CID INT PRIMARY KEY,
  CName VARCHAR(50) NOT NULL,
  CDetails VARCHAR(255)
);
INSERT INTO customers VALUES (1, 'Max Verstappen', '1234567890, Netherlands');   		-- This is not 1NF because CDetails has multiple values (phone no and address) in same column.

-- To convert into 1NF we create separete columns for phone no and address
CREATE TABLE customer1NF (
  CID INT PRIMARY KEY,
  CName VARCHAR(50) NOT NULL,
  Phone_No VARCHAR(20),
  Address VARCHAR(255)
);

INSERT INTO customer1NF VALUES (1, 'John Doe', '123-456-7890', '1 Main St');
DROP TABLE customers;

-- 2) Second Normal Form (2NF)
-- Table must be in 1NF.
-- All non-key attributes (columns) must depend on the entire primary key.
-- If a table has a composite primary key, each non-key attribute must depend on the entire composite key, not just on part of it.
CREATE TABLE orders (
  OID INT PRIMARY KEY,
  CID INT, 
  PID INT NOT NULL,
  Product_Name VARCHAR(50) NOT NULL,
  Quantity INT NOT NULL,
  FOREIGN KEY (CID) REFERENCES customers1NF(CID)
);

INSERT INTO Orders VALUES (101, 001, 1001, 'Shirt', 2);

-- This table violates 2NF because Product_Name depends only on PID, and not the primary key OID
-- To make it 2NF we create another table for products
CREATE TABLE orders2NF 
(
  OID INT PRIMARY KEY,
  CID INT,
  PID INT NOT NULL,
  Quantity INT NOT NULL,
  FOREIGN KEY (CID) REFERENCES customer1nf(CID)
);

CREATE TABLE products
(
	PID INT PRIMARY KEY,
    Product_Name VARCHAR(50) NOT NULL,
    Product_color VARCHAR(50) NOT NULL
);

DROP TABLE orders;

-- 3. Third Normal Form (3NF)
-- Table must be in 2NF
-- No transitive dependencies should exist
-- Every non-key attribute must depend on the primary key, and only the primary key


-- # BCNF
-- Boyce-Codd Normal Form (BCNF) is a higher level of normalization than 3NF.
-- It eliminates some anomalies that can arise from non-trivial functional dependencies in 3NF relations.