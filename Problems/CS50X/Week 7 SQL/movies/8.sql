SELECT name FROM people WHERE id IN(SELECT person_id FROM stars WHERE movie_id =(select id from movies WHERE title = 'Toy Story'));

