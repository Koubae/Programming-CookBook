create table users (
    id integer primary key autoincrement, 
    name text not null,
    password text not null, 
    expert boolean not null,
    admin boolean not null
);

create table questions (
    id integer primary key autoincrement,
    question_text text not null, 
    answer_text text,
    asked_by_id integer not null,
    expert_id integer not null
);