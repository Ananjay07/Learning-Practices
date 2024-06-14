-- OPERATOR: An Operator is a symbol that tells the compiler to perform specific mathematical, relational or logical operation to produce a desired result.
-- There are 4 types of Operators:-
-- 1) Arithmetic Operators (+,-,*,/,%) : used for mathematical calculations
-- 	i) Addition + 
select 21+5;
-- 	ii) Subtraction -
select 31-11;
-- 	iii) Mulitplication *
select 6*8;
-- iv) Division /
select 81/9;
-- v) Modulo %
select 5%3;

-- 2) Comparison Operators(=,>,<,>=,<=,<>/ or !=) : used to compare the operands and give result in True or False
-- 	i) Equals to =
SELECT 5=5;
-- 	ii) Greater Than{>}
SELECT 5>3;
-- 	iii) Less Than{<}
SELECT 3<5;
-- 	iv) Greater Than or Equals To{>=}
SELECT 5>=5;
-- 	v) Less Than or Equals To{<=}
SELECT 5<=6;
-- 	vi)Not Eqauls To{<> or !=}
SELECT 5<>6;
-- 3) Bitwise Operators(&,|,^) : compare each bit of the first operand to the correponding bit of the second operand and produce a final result.
-- 	i) Bitwise AND{&}: Result contains AND operated bits
SELECT 59 & 47;
-- b) Bitwise OR{|}: Result contains OR operated bits
SELECT 59 | 47;
-- c) Bitwise XOR{^}: Result contains XOR operated bits
SELECT 59 ^ 47;

-- 4) Logical Operators(AND, ALL, ANY, BETWEEN, EXISTS, IN, LIKE, NOT, OR, SOME) : connect two or more boolean expressions. Results are in True and False.
-- 	i) AND: Gives True if all conditions separated by AND are True
SELECT 4!=6 AND 12>6;
-- b) OR: Gives True if any of the conditions separated by OR is True
SELECT 5>4 AND 10=6;
-- c) NOT: Gives true if condition is False, false if condition is True
SELECT NOT 3<5;
-- d) LIKE: Gives true if operand matches a pattern
SELECT 'Hello' LIKE '%o';
-- e) BETWEEN: Gives true if operand is within the range of comparisons
SELECT 5 BETWEEN 1 AND 10;
