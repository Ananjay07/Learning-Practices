-- String Functions - set of built-in functions that allow you to manipulate and operate on string data.
-- 1) CHAR_LENGTH(str): This function returns the length of the given string str in characters.
SELECT CHAR_LENGTH('Hello This Is Me!');

-- 2) ASCII(str): This function returns the ASCII code value of the leftmost character in the string str.
SELECT ASCII('B');
SELECT ASCII('Ajsf');

-- 3) CONCAT(str1, str2, ...) - joins two or more string values together.
SELECT CONCAT('I', ' ', 'am', ' ', 'Jam');

-- 4) INSTR(str, substr) - returns the position of the first occurrence of the substr in str.
SELECT INSTR('Hello, World!', 'o');
SELECT INSTR('Hello, World!', 'x');

-- 5) LCASE(str) LOWER(str) and UCASE(str) or UPPER(str) -  convert the given string to lowercase and uppercase
SELECT LCASE('MY NAME iS MAX');
SELECT UCASE('my nAme is LEwis'); 

-- 6) SUBSTR(str, start, length): This function extracts a substring from the string str starting at the position start and with a length of length characters.
SELECT SUBSTR('Max is here', 1, 3);

-- H) LPAD(str, len, padstr): This function pads the string str on the left side with the padstr string
--    repeated as many times as necessary to make the total length equal to len.
SELECT LPAD('Hello', 10, '*');

-- I) RPAD(str, len, padstr): This function pads the string str on the right side with the padstr string
--    repeated as many times as necessary to make the total length equal to len.
SELECT RPAD('Hello', 10, '*');

-- J) TRIM(str), RTRIM(str), LTRIM(str): These functions remove leading and/or trailing spaces from the string str.
--    TRIM removes leading and trailing spaces, RTRIM removes trailing spaces, and LTRIM removes leading spaces.
SELECT TRIM('   Hello, World!   ');
SELECT RTRIM('   Hello, World!   ');
SELECT LTRIM('   Hello, World!   ');

-- Date and Time Functions - a set of built-in functions that allow you to manipulate and perform operations on date and time data types.
-- A) CURRENT_DATE(): This function returns the current date in the format 'YYYY-MM-DD'.
SELECT CURRENT_DATE() AS today;

-- B) DATEDIFF(date1, date2): This function returns the number of days between two date values. 
-- The result can be positive or negative, depending on whether date1 is greater or less than date2.
SELECT DATEDIFF('2023-05-10', '2023-05-01') AS day_difference;

-- C) DATE(expression): This function extracts the date part from a date or datetime expression.
SELECT DATE('2023-05-01 12:34:56') AS result;

-- D) CURRENT_TIME(): This function returns the current time in the format 'HH:MM:SS'.
SELECT CURRENT_TIME() AS now;

-- E) LAST_DAY(date): This function returns the last day of the month for a given date.
SELECT LAST_DAY('2023-05-01') AS last_day_of_may;

-- F) SYSDATE(): This function returns the current date and time as a value in the format 'YYYY-MM-DD HH:MM:SS'.
SELECT SYSDATE() AS `Timestamp`;

-- G) ADDDATE(date, interval): This function adds a time interval to a date value and returns the new date.
SELECT ADDDATE('2023-05-01', INTERVAL 7 DAY) AS one_week_later;

-- Numeric Functions - a set of built-in functions that allow you to perform various mathematical operations and calculations on numeric data types 
-- A) AVG(expression): This function returns the average value of the non-null values in a group.
--    It's commonly used with the GROUP BY clause.
SELECT AVG(price) AS avg_price
FROM products;

-- B) COUNT(expression): This function returns the number of non-null values in a group.
--    It can be used with or without the GROUP BY clause.
SELECT COUNT(*) AS total_products
FROM products;

-- C) POW(base, exponent): This function returns the value of base raised to the power of exponent.
SELECT POW(2, 3) AS result;

-- D) MIN(expression): This function returns the minimum value in a group. It's often used with the GROUP BY clause.
SELECT MIN(price) AS min_price
FROM products;

-- E) MAX(expression): This function returns the maximum value in a group. It's often used with the GROUP BY clause.
SELECT MAX(stock) AS max_stock, location
FROM products
GROUP BY location;

-- F) ROUND(number, [decimals]): This function rounds a number to a specified number of decimal places. 
--    If decimals is omitted, it rounds to the nearest integer.
SELECT ROUND(3.1416, 2) AS result;
SELECT ROUND(3.1416) AS result;

-- G) SQRT(number): This function returns the square root of a non-negative number.
SELECT SQRT(25) AS result;

-- H) FLOOR(number): This function returns the largest integer value that is less than or equal to the given number.
SELECT FLOOR(3.8) AS result;
SELECT FLOOR(-3.8) AS result;