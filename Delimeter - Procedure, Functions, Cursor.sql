-- #DELIMETER
-- Delimeter - command used to change the standard delimiter(like a semicolon (;)), to a different character
-- Deterministic - It indicates that the function will always return the same result for the same input values

-- PROCEDURE
-- It is a set of SQL statements that can be saved and reused
-- Creating a procedure:
use cars;
DELIMITER //
CREATE PROCEDURE select_all_models()
BEGIN
    SELECT * FROM model;
END //
DELIMITER ;

CALL select_all_models();

-- deleting a procedure:
DROP PROCEDURE select_all_models;

-- FUNCTION
-- A function is a reusable block of code that performs a specific task and can return a value
-- Function to calculate total revenue for a product
DELIMITER //
CREATE FUNCTION getBrandDetails(brandId INT)
RETURNS VARCHAR(255)
DETERMINISTIC
BEGIN
    DECLARE brandDetails VARCHAR(120);
    SELECT CONCAT('Brand Name: ', b_name) INTO brandDetails
    FROM brands
    WHERE brand_id = brandId;
    RETURN brandDetails;
END //

DELIMITER ;

SELECT getBrandDetails();

-- IN
-- IN is a  part of procedures and it allow you to pass values into the procedure
DELIMITER //
CREATE PROCEDURE get_product_details(IN mid int)
BEGIN
    SELECT * FROM model WHERE model_id = mid;
END //

CALL get_product_details(1001);

drop procedure get_product_details;

-- OUT 
-- OUT is a part of procedure and it allow you to return values from a procedure
DELIMITER //
CREATE PROCEDURE get_product_count(OUT brand INT)
BEGIN
    SELECT COUNT(*) INTO brand FROM brands;
END //
drop procedure get_product_count;
CALL get_product_count(@brand);
SELECT @brand as brand;

-- #CURSOR
-- Cursors - used to retrieve and process rows one by one from the result set of a query.
-- They are declared using the DECLARE CURSOR statement, specifying the SELECT query whose result set will be processed.
-- Two types of cursor :-
-- 	i)User-Defined Cursors - declared by the user to process rows retrieved from a query result set and they are useful when you need to perform custom operations on individual rows

DELIMITER //
DECLARE @brand_count INT;
SELECT @brand_count = COUNT(*)
FROM brands;
PRINT 'Number of brands we have: ' + CAST(@brand_count AS VARCHAR(10));
DELIMITER ;

-- 	ii) Pre-defined Cursors - system-defined cursors provided by the DBMS. They are often associated with built-in functions or stored procedures that return result sets
DELIMITER //
DECLARE @total_price INT;

SELECT @total_price = SUM(price)
FROM payment
WHERE b_name = 'Mercedes';
PRINT 'Price of Mercedes: ' + CAST(@total_price AS VARCHAR(20));
DELIMITER ;
