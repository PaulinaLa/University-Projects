-- Paulina Landkocz, pwi
-- Zadanie 1
SELECT u.id, displayname, reputation, COUNT (DISTINCT p.id) FROM users u JOIN posts p ON(u.id=p.owneruserid)
JOIN postlinks pl ON (pl.postid = p.id)
JOIN posts r ON (pl.relatedpostid=r.id)
WHERE linktypeid = 3
GROUP BY u.id, displayname, reputation
HAVING count(DISTINCT p.id)>0
ORDER BY 4 DESC, displayname ASC
LIMIT 20;

-- Zadanie 2
SELECT u.id, displayname, reputation, COUNT(c.id), AVG(c.score)
FROM users u
  JOIN badges  b ON (b.userid = u.id)
  LEFT JOIN posts  p ON (p.owneruserid = u.id)
  LEFT JOIN comments c ON (c.postid = p.id)
WHERE b.name = 'Fanatic'
GROUP BY u.id, displayname, reputation
HAVING COUNT(c.id) <= 100
ORDER BY 4 DESC, displayname ASC
LIMIT 20;

-- Zadanie 3
ALTER TABLE users ADD PRIMARY KEY (id);

ALTER TABLE badges ADD CONSTRAINT fk_user_id FOREIGN KEY (userid) REFERENCES users(id);

ALTER TABLE posts DROP COLUMN viewcount;

DELETE FROM posts WHERE body='' OR body IS NULL;

-- Zadanie 4
CREATE SEQUENCE posts_id;
SELECT setval('posts_id', max(id)) FROM posts;
ALTER TABLE posts ALTER COLUMN id
  SET DEFAULT nextval('posts_id');
ALTER SEQUENCE posts_id OWNED BY posts.id;

INSERT INTO posts(posttypeid, parentid, owneruserid, body, score, creationdate)
SELECT 3, postid, userid, text, score, creationdate FROM comments;

