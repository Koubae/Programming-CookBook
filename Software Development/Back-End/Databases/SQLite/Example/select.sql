SELECT
    users.id,
    users.name,
    posts.description
FROM
    posts
INNER JOIN
    users ON users.id = posts.user_id;


SELECT
    posts.description as post,
    text as comment,
    name
FROM
    posts
INNER JOIN comments ON posts.id = comments.post_id
INNER JOIN users ON users.id = comments.user_id;


SELECT
    description as Post,
    COUNT(likes.id) as Likes
FROM
    likes,
    posts
WHERE
    posts.id = likes.post_id
GROUP BY
    likes.post_id;

