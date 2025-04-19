-- Lists all records in second_table with score >= 10, ordered by top scores

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
