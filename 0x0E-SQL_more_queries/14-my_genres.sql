-- Retrieves the names of all genres associated with the TV show titled 'Dexter'.
-- Joins the tv_genres, tv_show_genres, and tv_shows tables to match genres to the specified show.
-- Results are ordered alphabetically by genre name.
SELECT tv_genres.name
FROM tv_genres JOIN tv_show_genres JOIN tv_shows
ON tv_genres.id = tv_show_genres.genre_id 
AND tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;
