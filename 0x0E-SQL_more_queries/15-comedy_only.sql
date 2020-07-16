-- script
SELECT ts.title FROM tv_shows ts LEFT JOIN tv_show_genres tsg ON ts.id=tsg.show_id LEFT JOIN tv_genres tg ON tg.id=tsg.genre_id WHERE name='Comedy' ORDER BY ts.title ASC;
