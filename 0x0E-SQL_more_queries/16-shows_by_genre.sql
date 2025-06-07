-- This query retrieves a list of TV show titles along with their associated genre names.
-- It uses LEFT JOINs to ensure all TV shows are included, even if they do not have a genre.
-- The results are ordered alphabetically by TV show title and then by genre name.
-- Columns returned:
--   - title: The title of the TV show (from tv_shows table)
--   - name: The name of the genre (from tv_genres table; may be NULL if no genre is associated)
SELECT tv_shows.title, tv_genres.name
FROM tv_shows 
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_genres.name;
