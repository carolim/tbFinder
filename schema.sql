drop table if exists textbooks;
create table textbooks (id integer primary key,
						dept text,
						code integer,
						name text,
						link text);