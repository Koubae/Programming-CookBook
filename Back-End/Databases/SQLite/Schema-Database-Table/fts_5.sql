-- sqlite

-- Create an Virtual FTS5 table with two columns 

-- Syntax
CREATE VIRTUAL TABLE table_name 
USING FTS5(/*column1,column2...*/);



CREATE VIRTUAL TABLE posts 
USING FTS5(title, body);


INSERT INTO posts(title,body)
VALUES('Learn SQlite FTS5','This tutorial teaches you how to perform full-text search in SQLite using FTS5'),
('Advanced SQlite Full-text Search','Show you some advanced techniques in SQLite full-text searching'),
('SQLite Tutorial','Help you learn SQLite quickly and effectively');


/* ============================ < Match > ============================ */

SELECT * 
FROM posts 
WHERE posts MATCH 'fts5';

SELECT * 
FROM posts 
WHERE posts MATCH 'text' 
ORDER BY rank;


SELECT * 
FROM posts 
WHERE posts MATCH 'learn SQLite';

SELECT * 
FROM posts 
WHERE posts = 'fts5';


SELECT * 
FROM posts('fts5');

-- Boolean operators

SELECT * 
FROM posts 
WHERE posts MATCH 'learn NOT text';


SELECT * 
FROM posts 
WHERE posts MATCH 'learn OR text';


SELECT * 
FROM posts 
WHERE posts MATCH 'sqlite AND searching';


SELECT * 
FROM posts 
WHERE posts MATCH 'search AND sqlite OR help';


SELECT * 
FROM posts 
WHERE posts MATCH 'search AND (sqlite OR help)';

/* ============================ < Prefix searches > ============================ */

SELECT * 
FROM posts
WHERE posts = 'search*';

/* ============================ < Built-in auxiliary functions > ============================ */

SELECT highlight(posts,0, '<b>', '</b>') title, 
       highlight(posts,1, '<b>', '</b>') body
FROM posts 
WHERE posts MATCH 'SQLite'
ORDER BY rank;



-- NOTE: Notice that you cannot add types, constraints, or PRIMARY KEY declaration in the CREATE VIRTUAL TABLE statement for creating an FTS5 table. If you do so, SQLite will issue an error.

-- Like creating a normal table without specifying the primary key column, SQLite adds an implicit rowid column to the FTS5 table.


-- NOTE: The bm25() returns a value that represents the accuracy of the current match, the lower value means a better match.


-- NOTE: The highlight() auxiliary function returns a copy of the text with search terms surrounded by a specified markup e.g.,<b>search term </b>

-- NOTE: The snippet() selects a short fragment of text in order to maximize the number of search terms it contains.