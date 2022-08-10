-- Script that prints all the records of the second table
-- query all the records without the names which doesn't have name
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
