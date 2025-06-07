
-- This query retrieves the number of TV shows for each genre.
-- It joins the 'tv_genres' table with the 'tv_show_genres' association table on the genre ID.
-- For each genre, it counts how many times the genre appears in the association table (i.e., how many shows belong to that genre).
-- The results are grouped by genre and ordered in descending order by the number of shows per genre.
-- Output columns:
--   genre: The name of the TV genre.
--   number_of_shows: The total number of shows associated with that genre.
SELECT tv_genres.name AS genre, count(genre_id) AS number_of_shows
FROM tv_genres JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre_id
ORDER BY number_of_shows DESC;
