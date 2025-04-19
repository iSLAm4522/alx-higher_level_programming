-- 16. No link
-- Write a query to select the score and name from the second_table
-- where the name is not null and not empty.
-- The result should be ordered by score in descending order.

SELECT score, name
FROM second_table
WHERE name is NOT NULL and name != ''
ORDER BY score DESC;
