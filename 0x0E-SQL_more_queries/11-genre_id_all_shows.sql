-- script
SELECT ts.title, tsg.genre_id FROM tv_shows ts LEFT JOIN tv_show_genres tsg ON ts.id=tsg.show_id ORDER BY title,genre_id ASC;
