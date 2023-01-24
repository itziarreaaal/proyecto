import Conect as c
import Date as d
# import menu as m
import random
cursorr = c.mydb.cursor()

def agregarregBD(dni, nombre, riesgo, humano):
    sql = "INSERT INTO player (player_id, player_name, player_risk, human) VALUES (%s, %s, %s, %s)"
    val = (dni, nombre, riesgo, humano)
    cursorr.execute(sql, val)
    c.mydb.commit()
    return "Usuario agregado"

def eliminarregBD(dni):
    if dni in listadni():
        cursorr.execute(f"SELECT * FROM player where player_id = '{dni}'")
        resultadosh = cursorr.fetchall()
        for fila in resultadosh:
            print("ID: ", fila[0], "\n", "NAME: ", fila[1], "\n", "RISK: ", fila[2], "\n", "Type: ", fila[3])
            res= input(f'Are you sure you want to remove player with id {dni}? Y/N')
            res=res.upper()
        if res == "Y":
            cursorr.execute(f"DELETE FROM player where player_id = '{dni}'")
            resultadosh = cursorr.fetchall()
            c.mydb.commit()
            return "Usuario Eliminado"
        else:
            return
    else:
        return

def listadni():
    niflista = []
    cursorr.execute("SELECT player_id FROM player")
    for x in cursorr:
        for nif in x:
            niflista.append(nif)
    return niflista


def roundmax():
    next = False
    while not next:
        ma = input(" " * 58 + "MAX ROUNDS")
        ma.strip()
        if not ma.isdigit() or not ma or ma.isspace():
            print(" " * 58 +'Please enter only int')
        else:
            ma = int(ma)
            if 1 < ma < 20:
                d.contextgame['rounds'] = ma
                print(" " * 52, "Has escogido ",  ma, "rondas")
                return
            else:
                print(" " * 58 +'Only numbers between 5 and 20')



def escogermazoes():
    car = d.cartasES.copy()
    d.contextgame['mazo'] = 'ESP'
    print(" " * 50, "Escogiste la Baraja Española")
    return car

def escogermazopo():
    car = d.cartasEN.copy()
    d.contextgame['mazo'] = 'POK'
    print(" " * 50, "Escogiste la Baraja de Poker")
    return car

def insert_ranking():
  cursorr.execute(
    "select player_id, `Ganancias Obtenias`, `Partidas Jugadas`, `Minutos Jugados` from ranking")
  resultadosr = cursorr.fetchall()

  for fila2 in resultadosr:
    d.rak += "".ljust(5) + str(fila2[0]).ljust(9) + '               ' + str(fila2[1]).ljust(3) + '       ' + str(
      fila2[2]).ljust(3) + '            ' + str(fila2[3]).ljust(3) + '\n'
  return d.rak

def new_item_name():
  # creo una llista de noms per després comprobar si és un nom repetit
  name = input(" " * 58 + "Name:")
  try:
    # comprobo si es un string buit
    if not name or name.isspace():
      msj = "Cannot be an empty name!"
      raise ValueError
  except ValueError:
    print(" " * 58 +msj)
    return new_item_name()
  else:
    return name

def newDni(h):
    next = False
    dnlist = []
    cursorr.execute("SELECT player_id FROM player")
    for x in cursorr:
        for cf in x:
            dnlist.append(cf)
    while not next:
        if h:
            dni = input(" " * 58 + "DNI:")
            if len(dni) != 9 or not dni[0:8].isdigit():
                print(" " * 58 +'El formato de DNI no es valido')
            elif d.listadni[int(dni[0:8]) % 23].lower() != dni[8].lower():
                print(" " * 58 +f'El DNI {dni} no es valido')

            else:
                dni = dni.upper()
                if dni in dnlist:
                    print(" " * 58 +'DNI alredy exists')
                else:
                    return dni
        elif not h:
            dnin = random.randint(11111111, 99999999)
            letra = d.palabra[dnin % 23]
            dni = (str(dnin) + letra)
            if dni in dnlist:
                next = False
            else:
                return dni
def newName():
    next = False
    while not next:
        nn = input(" " * 58 + "Name:")
        nn = nn.strip()
        if not nn or nn.isspace() or nn.isdigit():
            print(" " * 58 + 'Incorrect name, please, enter a name not empty with only letters')
        else:
            return nn

def newProfile():
    next = False
    while not next:
        print(" " * 58 + "1)Cautious" + "\n" + " " * 58 + "2)Moderated" + "\n" + " " * 58 + "3)Bold")
        sel = input(" " * 58 + "Opcion:")
        if not sel.isdigit():
            print(" " * 58 +'Only numbers available')
        else:
            sel = int(sel)
            if sel not in range(1, 4):
                print(" " * 58 +'Not in range ')
            else:
                if sel == 1:
                    return 1
                elif sel == 2:
                    return 2
                elif sel == 3:
                    return 3


def setgameplayer():
  cursorh = c.mydb.cursor()
  cursorh.execute(
    "select player_id as ID, player_name as Name, case when player_risk = 1 then 'Cautious' when player_risk = 2 then 'Moderated' when player_risk = 3 then 'Bold' end as Type from player where human = 1")
  resultadosh = cursorh.fetchall()
  cursorb = c.mydb.cursor()
  cursorb.execute(
    "select player_id as ID, player_name as Name, case when player_risk = 1 then 'Cautious' when player_risk = 2 then 'Moderated' when player_risk = 3 then 'Bold' end as Type from player where human = 0")
  resultadosb = cursorb.fetchall()
  print(d.sel)
  for fila2 in resultadosh:
    print(str(fila2[0]).ljust(9) + '           ' + str(fila2[1]).ljust(14) + '           ' + str(fila2[2]).ljust(
      9) + '                || ' + '\n')
  for fila in resultadosb:
    print('                                                                         ' + str(fila[0]).ljust(
    9) + '           ' + str(fila[1]).ljust(14) + '           ' + str(fila[2]).ljust(9) + '\n')
  print(
    '\n********************************************************************************************************************************************''\n')
#funciona
def pedirdatos1_3():
  opc=""
  while opc == "":
      opc = input("Option:id to remove player, -1 to go back:")
      if opc != "" and opc != "-1":
          if opc in listadni():
              return opc
          else:
              print(" " * 58 + "player removed")
              opc = ""
      elif opc == "-1":
        return
      else:
          print(" " * 58 + "OPCION INCORRECTA")
          opc=""

def pedirdatos2_1():
  opc=""
  while opc == "":
      opc = input("Option: id to add to game, sh to show actual players in game, -1 to go back:")
      if not opc.isspace() and opc != "-1" and opc != "sh":
          if opc in listadni():
              d.playcont.append(opc)
          else:
              print(" " * 58 + "Ingrese un valor correcto")
              opc = ""
      elif opc != "" and opc == "-1":
        return



def pedirdatos(dni):
  while dni == "":
      dni = input("Option: id to add to game, -id to remove player, sh to show actual players in game, -1 to go back:")
      if dni != "" and dni != "-id" and dni != "-1" and dni != "sh":
        return dni
      elif dni == "-1":
        return "-1"
      # elif dni ==

#hecha
def opcion2_1():
    opc=""
    while opc == "":
        input("Option: id to add to game, -id to remove player, sh to show actual players in game, -1 to go back:")
    if opc in listadni():
        return opc
    else:
        print(" " * 58 +"Ingrese un valor correcto")
        opc=""


  # falta la validacion si existe en la base de datos

def fillplayer(*dni):
  if dni != "" and dni != "-id" and dni != "-1" and dni != "sh":
    playerss=""
    codigo='select player_id as ID, player_name as Name, case when human = 1 then "Human" when human = 0 then "Bot" end as Human, case when player_risk = 1 then "Cautious" when player_risk = 2 then "Moderated" when player_risk = 3 then "Bold" end as Type from player where player_id = ' + '"' + dni + '"'
    cursorplayer = c.mydb.cursor()
    cursorplayer.execute(codigo)
    resultadosp = cursorplayer.fetchall()
    for fila in resultadosp:
    #     print(fila3[0], fila3[1], fila3[2], fila3[3] )
      print = d.apg + ''.ljust(35) + str(fila[0]).ljust(9) + '           ' + str(fila[1]).ljust(9) + '        ' + str(fila[2]).ljust(9) + '           ' + str(fila[3]).ljust(9) + '\n'
    if fila[3]=="Cautious":
        type  =30
    elif fila[3]=="Moderated":
        type = 40
    elif fila[3]=="Bold":
        type = 50

    # player1 = {fila[0]: {'name': fila[1], 'human': fila[2], 'bank': 0, 'initialCard': "", 'priority': 0, "type": type, "bet": 4, "points": 0, "cards": [], "roundPoints": 0}}
    # player1 = {fila[0]: {'name': fila[1], 'human': fila[2], 'bank': 0, 'initialCard': "", 'priority': 0, "type": type, "bet": 4, "points": 0, "cards": [], "roundPoints": 0}}
    # player2 = {fila[0]: {'name': fila[1], 'human': fila[2], 'bank': 0, 'initialCard': "", 'priority': 0, "type": type, "bet": 4, "points": 0, "cards": [], "roundPoints": 0}}
    # player1.update(player2)
    return playerss
    #print(players)
