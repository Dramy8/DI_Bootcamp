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

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )

-- retrieve number of rows from firsttab that are not null value in secondtab. 
-- since there is NULL the NOT IN condition will always be false., the output will be 0.  

-- Q2. What will be the OUTPUT of the following statement?

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

-- retrieve number of rows from firsttab excluding the row where id=5 in secondtab. so count will be 2.   

-- Q3. What will be the OUTPUT of the following statement?

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

-- retrieve all rows from firsttab except the one where id is in secondtab. 
-- since there is NULL the NOT IN condition will always be false., the count output will be 0.  

-- Q4. What will be the OUTPUT of the following statement?

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )

-- retrieve all rows from firsttab except the one where id is in secondtab is not null. so this is the case for 2 rows. so count is 2.  


