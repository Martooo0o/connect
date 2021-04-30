drop table if exists posts;
drop table if exists users;
	create table posts (
		id integer primary key autoincrement,
		name text not null,
		content text not null,
		likes integer not null
);
	create table users (
		id integer primary key autoincrement,
		username text not null
);

