CREATE TABLE FirstTab (
     id integer, 
     name VARCHAR(10)
)
-- we create a new table called FirstTab with 2 columns, one is ID, type integer, and one is name, type string max character 10
INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar')
-- we add into table 4 rows, each one is an ID and name except last one which is a NULL ID but with name. 
SELECT * FROM FirstTab
-- retrieve all details of all rows from table
CREATE TABLE SecondTab (
    id integer 
)
-- create another table called SecondTab with one column, ID
INSERT INTO SecondTab VALUES
(5),
(NULL)
-- add value into table, one of them is Null value

SELECT * FROM SecondTab

-- retrieve all details of all rows from table


--q1 What will be the OUTPUT of the following statement?

--     SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )

-- retrieve all details of ID from firsttab that are not null value in secondtab.  

-- Q2. What will be the OUTPUT of the following statement?

--     SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

-- retrieve all details of ID from firsttab except the one where id=5 in secondtab.  

-- Q3. What will be the OUTPUT of the following statement?

--     SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

-- retrieve all details of ID from firsttab except the one where id is in secondtab.  

-- Q4. What will be the OUTPUT of the following statement?

--     SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )

-- retrieve all details of ID from firsttab except the one where id is in secondtab is not null  


