--Paulina Landkocz, pwi
--Zadanie 1
CREATE VIEW ranking (displayname, liczba_odpowiedzi) AS 
SELECT displayname, COUNT(*)
FROM users JOIN posts A ON (users.id = A.owneruserid)
  JOIN posts B ON ( A.id=B.acceptedanswerid)
GROUP BY displayname
ORDER BY 2 DESC, 1 ASC;

SELECT * FROM ranking;

--Zadanie 2
WITH enlightened_users AS
(SELECT DISTINCT u.id, u.upvotes FROM users u JOIN badges b ON b.userid = u.id WHERE name='Enlightened')

    SELECT DISTINCT u.id, u.displayname, reputation 
    FROM users u LEFT JOIN 
    comments c ON (u.id=c.userid)
    JOIN posts p ON (p.id=c.postid)
    WHERE u.id NOT IN (SELECT id FROM enlightened_users) AND 
    u.upvotes > ANY(SELECT AVG(upvotes) FROM enlightened_users) AND 
    EXTRACT(year FROM p.creationdate)=2020
    GROUP BY u.id, u.displayname, u.reputation
    HAVING COUNT(*)>1;

--Zadanie3
WITH RECURSIVE rec(id, displayname) 
AS 
(SELECT u1.id, u1.displayname 
FROM users u1 JOIN posts p1 ON (u1.id = p1.owneruserid)
WHERE p1.body LIKE '%recurrence%'
UNION
SELECT u2.id, u2.displayname
FROM users u2 JOIN comments c ON (u2.id = c.userid)
    JOIN posts p2 ON (p2.id = c.postid)
    JOIN rec ON (p2.owneruserid = rec.id))
SELECT * FROM rec;