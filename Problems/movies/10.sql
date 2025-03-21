SELECT DISTINCT name from people where id in (SELECT person_id from directors where movie_id in (SELECT id FROM movies WHERE id in (SELECT movie_id FROM ratings WHERE rating >= 9.0)));

