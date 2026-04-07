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

create table classes (
	c_id int auto_increment,
	c_name varchar(100) not null,
	course_code int not null,
	p_id int not null,
	primary key(c_id),
	foreign key(p_id) references professors(p_id)
);

create table enrollment(
	e_id int auto_increment,
	s_id int not null,
	c_id int not null,
	primary key(e_id),
	foreign key(s_id) references students(s_id),
	foreign key(c_id) references classes(c_id)
	
);

insert into students(f_name, l_name, email, major, year) values ("John", "Doe", "john@gmail.com", "computer science", 2020);
insert into students(f_name, l_name, email, major, year) values ("James", "Smith", "james@gmail.com", "biology", 2015);
insert into students(f_name, l_name, email, major, year) values ("Paul", "Bond", "paul@gmail.com", "history", 2010);

select *
from students;

drop table students, professors, classes, enrollment;