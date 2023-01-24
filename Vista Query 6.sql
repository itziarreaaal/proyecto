CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `admin2`@`%` 
    SQL SECURITY DEFINER
VIEW `6_alt` AS
    SELECT 
        `pgr`.`cardgame_id` AS identiﬁcador_partida,
        SUM((CASE
            WHEN (tbl_sibank.points_j > tbl_nobank.max_points_j) THEN 1
            WHEN (tbl_sibank.points_j < tbl_nobank.max_points_j) THEN 0
        END)) AS rondas_ganadas_banca
    FROM
        ((player_game_round pgr
        JOIN (SELECT 
            pgr.cardgame_id AS cardgame_id,
                pgr.round_num AS round_num,
                MAX(tblint.points_j) AS max_points_j
        FROM
            (player_game_round pgr
        JOIN (SELECT 
            pgr.cardgame_id AS cardgame_id,
                pgr.round_num AS round_num,
                pgr.player_id AS player_id,
                SUM((pgr.starting_round_points + pgr.ending_round_points)) AS points_j
        FROM
            player_game_round pgr
        WHERE
            (pgr.is_bank = 0)
        GROUP BY pgr.cardgame_id , pgr.round_num , pgr.player_id) tblint ON (((tblint.cardgame_id = pgr.cardgame_id)
            AND (tblint.round_num = pgr.round_num))))
        WHERE
            (pgr.is_bank = 0)
        GROUP BY pgr.cardgame_id , pgr.round_num) tbl_nobank ON (((tbl_nobank.cardgame_id = pgr.cardgame_id)
            AND (tbl_nobank.round_num = pgr.round_num))))
        JOIN (SELECT 
            pgr.cardgame_id AS cardgame_id,
                pgr.round_num AS round_num,
                pgr.player_id AS player_id,
                SUM((pgr.starting_round_points + pgr.ending_round_points)) AS points_j
        FROM
            player_game_round pgr
        WHERE
            (pgr.is_bank = 1)
        GROUP BY pgr.cardgame_id , pgr.round_num , pgr.player_id) tbl_sibank ON (((tbl_sibank.cardgame_id = pgr.cardgame_id)
            AND (tbl_sibank.round_num = pgr.round_num))))
    WHERE
        (pgr.is_bank = 1)
    GROUP BY pgr.cardgame_id