SELECT COUNT(*)
FROM ACTORS;

-- INSERT INTO actors (first_name, last_name, birth_date, number_oscars)
-- VALUES('Jack','Black','',1);

-- when trying to fill in with only name or missing values etc, the outcome are: 
-- ERROR:  null value in column "birth_date" of relation "actors" violates not-null constraint
-- DETAIL:  Failing row contains (5, Jack, Black, null, null).
-- SQL state: 23502
 
-- ERROR:  INSERT has more target columns than expressions
-- LINE 4: INSERT INTO actors (first_name, last_name, birth_date, numbe...
--                                             ^
-- ERROR:  invalid input syntax for type date: ""
-- LINE 5: VALUES('Jack','Black','',1);
--                               ^

-- The constraint of each colummn prevents to insert values with missing info, or wrong format. 
-- however, an empty string for the name might work so need to adjust constraints. 