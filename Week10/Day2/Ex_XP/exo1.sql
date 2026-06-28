CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(50),
    item_price INTEGER
);

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);


INSERT INTO items (item_id, item_name, item_price)
VALUES 
	(1, 'Small desk', 100),
	(2, 'Large desk', 300),
	(3, 'Fan', 80);

INSERT INTO customers (customer_id, first_name, last_name)
VALUES 
	(1,'Greg','Jones'),
	(2,'Sandra','Jones'),
	(3,'Scott','Scott'),
	(4,'Trevor','Green'),
	(5,'Melanie','Johnson');


SELECT *
FROM items;


SELECT *
FROM items
WHERE item_price < 300;

SELECT *
FROM customers
WHERE last_name LIKE 'Smith';

SELECT *
FROM customers
WHERE last_name LIKE 'Jones';

SELECT *
FROM customers
WHERE first_name NOT LIKE 'Scott';