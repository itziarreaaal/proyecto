import Date as d
import mysql.connector
mydb = mysql.connector.connect(
  host="proy.mysql.database.azure.com",
  user="admin2",
  password="Proyecto*",
  db="sevenandhalf"
)
# try:
if mydb.is_connected():
  print("conexión existosa")
  cursor = mydb.cursor()
  cursor.execute("SELECT database();")
  registro=cursor.fetchone()
  print("Conectado la bd:", registro)


# for x in cartasEN:
#     cursor.execute("INSERT INTO card (card_id, card_name, card_value, card_priority, card_real_value, deck_id) VALUES (%s,%s,%s,%s,%s,%s)", (x, cartasEN[x]['literal'], cartasEN[x]['value'], cartasEN[x]['priority'], cartasEN[x]['realValue'], 'POK'))
#     mydb.commit()

# cursorr = mydb.cursor()
# cursorr.execute("select distinct cardgame_id, player_id, bet_points from player_game_round pg where bet_points = (SELECT MAX(bet_points) FROM player_game_round pgr where pgr.cardgame_id = pg.cardgame_id")
# resultadosr = cursorr.fetchall()
# for fila2 in resultadosr:
#   d.rep += "".ljust(5) + str(fila2[0]).ljust(9) + '               ' + str(fila2[1]).ljust(3) + '       ' + str(
#     fila2[2]).ljust(3) + '            ' + '\n'
# print(d.rep)

# cursorr = mydb.cursor()
# cursorr.execute(
#   "select distinct cardgame_id, player_id, bet_points from player_game_round pg where bet_points = (SELECT MAX(bet_points) FROM player_game_round pgr where pgr.cardgame_id = pg.cardgame_id)")
# resultadosr = cursorr.fetchall()
#
# for fila2 in resultadosr:
#   d.rep += "\n" + "".ljust(45) + str(fila2[0]).ljust(3) + '         ' + str(fila2[1]).ljust(9) + '            ' + str(fila2[2]).ljust(3) + '            ' + '\n'
# print(d.rep)

# cursorr = mydb.cursor()
# cursorr.execute(
#   "select distinct cardgame_id, player_id, bet_points from player_game_round pg where bet_points = (SELECT min(bet_points) FROM player_game_round pgr where pgr.cardgame_id = pg.cardgame_id)");
#
# resultadosr = cursorr.fetchall()
#
# for fila2 in resultadosr:
#   d.reptres += "\n" + "".ljust(45) + str(fila2[0]).ljust(3) + '         ' + str(fila2[1]).ljust(9) + '            ' + str(fila2[2]).ljust(3) + '            ' + '\n'
# print(d.reptres)