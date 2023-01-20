#Creacion de base de datos para proyecto
create database sevenandhalf;
use sevenandhalf;
create table if not exists player(
player_id varchar(25) primary key not null,
player_name varchar(40), 
player_risk tinyint,
human tinyint(1));

create table if not exists deck(
deck_id char(3) primary key not null,
deck_name varchar(25));

create table if not exists card(
card_id char(3) primary key not null,
card_name varchar(25),
card_value decimal(3,1),
card_priority tinyint,
card_real_value tinyint,
deck_id char(3) unique);

create table if not exists cardgame(
cardgame_id int auto_increment primary key not null,
players tinyint,
rounds tinyint,
start_hour datetime,
end_hour datetime,
deck_id char(3));

create table if not exists player_game(
cardgame_id int, 
player_id varchar(25),
primary key(cardgame_id, player_id),
foreign key(cardgame_id) references cardgame(cardgame_id),
foreign key(player_id) references player(player_id),
initial_card_id char(3),
starting_points tinyint,
ending_points tinyint);

create table if not exists player_game_round(
round_num tinyint auto_increment primary key not null,
cardgame_id int,
player_id varchar(25),
is_bank tinyint(1),
bet_points tinyint,
cards_value decimal(4,1),
starting_round_points tinyint,
ending_round_points tinyint);





