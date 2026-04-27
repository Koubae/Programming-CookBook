PostgreSQL Functions
====================


### Directive variable_conflict


It's a PL/pgSQL compiler directive (also called a preprocessor directive).
It tells the PL/pgSQL compiler: when a name is ambiguous, prefer the table column over the variable/parameter.

- `#variable_conflict error`:   Raise an error on any ambiguity (safest, default-ish)
- `#variable_conflict use_column`:  Ambiguous names resolve to the column
- `#variable_conflict use_variable`:    Ambiguous names resolve to the variable/parameter

