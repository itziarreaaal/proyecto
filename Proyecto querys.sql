use sevenandhalf;
#2 listo
select distinct cardgame_id, player_id, bet_points from player_game_round pg where bet_points = (SELECT MAX(bet_points) FROM player_game_round pgr where pgr.cardgame_id = pg.cardgame_id);

#3 listo
select distinct cardgame_id, player_id, bet_points from player_game_round pg where bet_points = (SELECT min(bet_points) FROM player_game_round pgr where pgr.cardgame_id = pg.cardgame_id );

#8
select cardgame_id as Id_Game, avg(bet_points) as Average_Bet
from player_game_round 
group by cardgame_id;

#7 listo

select cardgame_id, count(distinct player_id)
from player_game_round
where is_bank like 1 
group by cardgame_id;

#9
select cardgame_id as Id_Game, avg(bet_points) as Average_Bet
from player_game_round 
where round_num like 1
group by cardgame_id;

#10
select  distinct cardgame_id, avg(bet_points), max(round_num)
from player_game_round
group by cardgame_id;

