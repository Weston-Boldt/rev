drop table if exists domain;

create table domain (
    id integer primary key autoincrement,
    name text,
    backend_url text
);
