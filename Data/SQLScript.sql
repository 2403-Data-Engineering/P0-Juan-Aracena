create table students (
	s_id int auto_increment,
	f_name varchar(50) not null,
	l_name varchar(50) not null,
	email varchar(100) not null,
	major varchar(100) not null,
	year int not null,
	primary key(s_id)
);

create table professors (
	p_id int auto_increment,
	f_name varchar(50) not null,
	l_name varchar(50) not null,
	department varchar(100) not null,
	email varchar(100) not null,
	primary key(p_id)
);

create table class (
	c_id int auto_increment,
	c_name varchar(100) not null,
	primary key(c_id)
);

insert into students(f_name, l_name, email, major, year) values ("John", "Doe", "john@gmail.com", "computer science", 2020);
insert into students(f_name, l_name, email, major, year) values ("James", "Smith", "james@gmail.com", "biology", 2015);
insert into students(f_name, l_name, email, major, year) values ("Paul", "Bond", "paul@gmail.com", "history", 2010);

select *
from students;