-- Script that prints all with same score
-- query that prints all by grouping by score
SELECT score, COUNT(score) AS number FROM  second_table GROUP BY score ORDER BY score DESC;
