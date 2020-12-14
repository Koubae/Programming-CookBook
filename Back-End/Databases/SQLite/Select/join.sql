/* ============================ < One-to-Many Relationships > ============================ */

SELECT 

a.first_name || ' ' || a.last_name A author_name, 
b.title AS book_title
FROM author a
JOIN book b ON b.author_id = a.author_id
ORDER BY a.last_name ASC;



/* ============================ < Many-to-Many Relationships > ============================ */

SELECT 
a.first_name || ' ' || a.last_name AS author_name,
p.name AS publisher_name
FROM author a

JOIN author_publisher ap ON ap.author_id = a.author_id

JOIN publisher p ON p.publisher_id = ap.publisher_id

ORDER BY a.last_name ASC;

SELECT

a.first_name || ' ' || a.last_name AS author_name, 

COUNT (b.title) AS total_books

FROM author a 

JOIN book b ON b.author_id = a.author_id

GROUP BY author_name

ORDER BY total_books DESC, a.last_name ASC;

