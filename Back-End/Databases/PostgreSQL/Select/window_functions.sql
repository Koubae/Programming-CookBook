SELECT depname, empno, salary, avg(salary) OVER (PARTITION BY depname) FROM empsalary;



--  ========================= < OVER + ORDER BY > ========================= --

SELECT depname, empno, salary,
        rank() OVER (PARTITION BY depname ORDER BY salary DESC)
FROM empsalary;




--  ========================= < OVER + WHERE > ========================= --

SELECT depname, empno, salary, enroll_date
FROM
    (SELECT depname, empno, salary, enroll_date,
            rank() OVER (PARTITION BY depname ORDER BY salary DESC, empno) AS pos
        FROM empsalary
    ) AS ss
WHERE pos < 3;