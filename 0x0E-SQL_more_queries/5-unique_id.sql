
-- Creates a table unique_id with id column having UNIQUE and DEFAULT constraints

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
