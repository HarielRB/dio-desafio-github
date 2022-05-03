drop database if exists movie_control;
create database movie_control;
use movie_control;
CREATE TABLE movies(
id  int not null primary key auto_increment,
movie_type int not null,
movie_name varchar(100),
total_ep int, 
atual_ep int,
last_view timestamp default  current_timestamp);

insert into movies(movie_type, movie_name, total_ep, atual_ep, last_view)
values("0", "Broklyn 99", 36, 16, current_timestamp()), 
("1", "Guardiões da Galáxia", null, null, current_timestamp());

insert into movies(movie_type, movie_name, total_ep, atual_ep, last_view)
values("0", "The Walking Dead", 16, 16, current_timestamp()), 
("1", "Senhor dos Aneis: Sociedade do Anel", null, null, current_timestamp()),
("1", "Senhor dos Aneis: As Duas Torres", null, null, current_timestamp());

update movies set last_view = "2020-06-25 10:00:00" where id = 1;

insert into movies(movie_type, movie_name, total_ep, atual_ep, last_view)
values("0", "Todo Mundo Odeia o Chris", 16, 16, "2010-01-01 16:00:00");

select * from movies;