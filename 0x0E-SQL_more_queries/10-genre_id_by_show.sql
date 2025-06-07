-- Retrieves the title of each TV show along with its associated genre ID.
-- Joins the 'tv_shows' and 'tv_show_genres' tables on the show ID.
-- Results are ordered alphabetically by show title and then by genre ID.
SELECT title, genre_id
FROM tv_shows JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
