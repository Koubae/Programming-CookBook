PostgreSQL Functions
====================


### General notes

- **PostgreSQL has no named constants**. Unlike languages with const or enum, PL/pgSQL gives you no way to define `MY_CONSTANT = 3` as a reusable symbol. Functions fill that gap.


### Directive variable_conflict


It's a PL/pgSQL compiler directive (also called a preprocessor directive).
It tells the PL/pgSQL compiler: when a name is ambiguous, prefer the table column over the variable/parameter.

- `#variable_conflict error`:   Raise an error on any ambiguity (safest, default-ish)
- `#variable_conflict use_column`:  Ambiguous names resolve to the column
- `#variable_conflict use_variable`:    Ambiguous names resolve to the variable/parameter



### $BODY$

It's a dollar-quoted string delimiter — a PostgreSQL alternative to single quotes for wrapping the function body.
A function definition in PostgreSQL is ultimately just a string passed to CREATE FUNCTION. 
You could write it with single quotes:

The tag **BODY is arbitrary**, you could use $$, $fn$, $xyz$, anything. 
`$BODY$` is just a common convention that makes it clear you're delimiting the function body.

```sql
CREATE FUNCTION foo() RETURNS void AS
'
BEGIN
  -- function body here
END;
'
LANGUAGE plpgsql;
```

But that breaks the moment your function body contains single quotes.
PostgreSQL lets you use $$ or $tag$ as an alternative string delimiter:

```sql
CREATE FUNCTION foo() RETURNS void AS
$BODY$
BEGIN
  -- single quotes 'just work' in here
END;
$BODY$
LANGUAGE plpgsql;
```


### language plpgsql security definer

- `LANGUAGE plpgsqlp`: Tells PostgreSQL which language engine to use to interpret the function body string. 

PostgreSQL supports several:


- `sql`: Simple functions that are just a single SQL statement
- `plpgsql`: Procedural language with variables, loops, IF/ELSE, exceptions
- `plpython3u`: Python-based functions
- `c`: C extensions

### SECURITY DEFINER

Controls whose permissions the function runs with. There are two options:

- `SECURITY INVOKER`: (default) the function runs with the privileges of the caller (whoever calls the function).
- `SECURITY DEFINER`: the function runs with the privileges of the user who created/owns the function.


### VOLATILE  | STABLE | IMMUTABLE


Are volatility category that tells the PostgreSQL query planner what to expect from this function. There are three levels:


- `IMMUTABLE`: Same inputs → always same output, no side effects	Cache result, evaluate at plan time, use in indexes
- `STABLE`:	Same inputs → same output within a single query, no side effects	Cache result within one statement
- `VOLATILE`: Output can change anytime, may have side effects	Nothing — must call it every time


#### VOLATILE


It tells PostgreSQL this function has side effects (it does INSERTs) and can return different results for the same inputs. 
This **prevents** the optimizer from **caching results or reordering calls**. 




Locks
-----

### What is a "Row Exclusive lock"?

PostgreSQL has **table-level lock modes** that are automatically acquired by DML statements. The comment refers to the lock that `INSERT` takes on the **table** `table_lock`:

| Statement | Table-level lock acquired |
|---|---|
| `SELECT` | `ACCESS SHARE` |
| `SELECT FOR UPDATE` | `ROW SHARE` |
| **`INSERT`** | **`ROW EXCLUSIVE`** |
| `UPDATE` / `DELETE` | `ROW EXCLUSIVE` |
| `CREATE INDEX` | `SHARE` |
| `ALTER TABLE` | `ACCESS EXCLUSIVE` |


**Row Exclusive** means:
- **Other readers** (`SELECT`) are **not blocked** — the table remains readable.
- **Other writers** (`INSERT`, `UPDATE`, `DELETE`) are **also not blocked** at the table level.
- Only **heavy operations** like `ALTER TABLE` or `LOCK TABLE IN EXCLUSIVE MODE` are blocked.

By inserting into `table_lock` first, PostgreSQL takes a **row-level lock** on that `(col_1, col_2)` combination. Any concurrent call for the same archive+vault will **block** on this INSERT until the first transaction commits or rolls back. This serializes the critical section.

The `ON CONFLICT DO NOTHING` means: if the lock row already exists (from a previous call), don't error — just acquire the lock on the existing row. The row itself has no meaningful data; it exists purely to be locked.

```sql
-- Release the archive lock.
perform table_lock_release(
    col_1 => my_function.col_1,
    col_2 => my_function.col_2
);
```
