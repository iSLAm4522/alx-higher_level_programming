-- Create a table named first_table with two columns: id and name
-- id is an integer
-- name is a string of 256 characters
-- The database name will be passed as an argument of the mysql command

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
