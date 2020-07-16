-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT g.name, SUM(tsr.rate) as rating FROM tv_genres g JOIN tv_show_genres tsg ON g.id=tsg.genre_id JOIN tv_show_ratings tsr ON tsg.show_id=tsr.show_id GROUP BY name ORDER BY rating DESC;
