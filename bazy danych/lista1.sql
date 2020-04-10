--Paulina Landkocz, grupa Piotra Wieczorka
--Zadanie 1
SELECT creationdate 
FROM posts 
WHERE body LIKE '%Turing%' 
ORDER BY creationdate DESC;

--Zadanie2

SELECT id, title 
FROM posts 
WHERE creationdate>='10-10-2018' AND
EXTRACT (month FROM creationdate) BETWEEN 9 AND 12
AND title IS NOT NULL AND score >=9 
ORDER BY title ASC;

--Zadanie3

SELECT DISTINCT displayname, reputation 
FROM users u JOIN posts p ON (p.owneruserid=u.id) 
JOIN comments c ON (c.postid=p.id) 
WHERE p.body LIKE '%deterministic%' 
AND c.text LIKE '%deterministic%' 
ORDER BY reputation DESC;

--Zadanie4

SELECT DISTINCT u1.displayname 
FROM users u1 
JOIN ((SELECT distinct u.id FROM users u 
JOIN posts p ON (p.owneruserid = u.id)) 
EXCEPT 
(SELECT distinct u.id 
FROM users u 
JOIN comments c ON (u.id = c.userid))) u2 ON (u1.id = u2.id) 
ORDER BY u1.displayname ASC LIMIT 10;