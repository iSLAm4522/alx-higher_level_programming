-- This query selects the titles of TV shows that belong to the 'Comedy' genre.
-- It performs a join between the tv_genres, tv_show_genres, and tv_shows tables
-- to associate shows with their genres. The WHERE clause filters for shows
-- where the genre name is 'Comedy'. The results are ordered alphabetically by show title.
SELECT tv_shows.title
FROM tv_genres JOIN tv_show_genres JOIN tv_shows
ON tv_genres.id = tv_show_genres.genre_id
AND tv_show_genres.show_id = tv_shows.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title;
