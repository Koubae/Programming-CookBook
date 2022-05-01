SELECT select_list1
FROM table1
EXCEPT
SELECT select_list2
FROM table2


/* ============================ < Example  > ============================ */

CREATE TABLE t1(
    v1 INT
);

INSERT INTO t1(v1)
VALUES(1),(2),(3);

CREATE TABLE t2(
    v2 INT
);
INSERT INTO t2(v2)
VALUES(2),(3),(4);


SELECT v1
FROM t1
EXCEPT 
SELECT v2
FROM t2;


--  Example
SELECT ArtistId
FROM artists
EXCEPT
SELECT ArtistId
FROM albums;