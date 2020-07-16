-- List all genres not linked to the show Dexter
SELECT name FROM tv_genres WHERE name NOT IN (SELECT tv_genres.name FROM tv_shows inner join tv_show_genres ON tv_shows.id=tv_show_genres.show_id inner join tv_genres ON tv_genres.id=tv_show_genres.genre_id WHERE tv_shows.title='Dexter') ORDER BY name ASC;
