-- Retrieves the title of each TV show and its associated genre ID.
-- Uses a LEFT JOIN to include all TV shows, even those without a genre.
-- Results are ordered alphabetically by show title, then by genre ID.
SELECT title, genre_id
FROM tv_shows LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
