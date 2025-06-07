-- This query retrieves a list of TV show titles along with their associated genre names.
-- It performs a LEFT JOIN between the 'tv_shows' table and a derived table (R2) that maps show IDs to genre names.
-- The derived table (R2) is created by joining 'tv_genres' and 'tv_show_genres' on genre ID.
-- The LEFT JOIN ensures all TV shows are included, even if they have no associated genre (genre name will be NULL).
-- The results are ordered alphabetically by TV show title and then by genre name.
SELECT tv_shows.title, R2.name
FROM tv_shows 
LEFT JOIN (
    SELECT tv_show_genres.show_id, tv_genres.name
    FROM tv_genres JOIN tv_show_genres 
    ON tv_genres.id = tv_show_genres.genre_id
) AS R2
ON tv_shows.id = R2.show_id
ORDER BY tv_shows.title, R2.name;
