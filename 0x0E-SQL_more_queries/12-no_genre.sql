-- This query retrieves the titles and genre IDs of all TV shows that do not have any associated genres.
-- It performs a LEFT JOIN between the 'tv_shows' and 'tv_show_genres' tables on the show ID.
-- The WHERE clause filters the results to include only those shows where the genre_id is NULL,
-- indicating that the show has no genre assigned.
-- The results are ordered alphabetically by the show's title and then by genre_id (which will be NULL).
SELECT title, genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;
