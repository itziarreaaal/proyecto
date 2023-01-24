import Conect as c
import Date as d
import Funcions as f

def getOpt(textOpts="", inputOptText="", rangeList=[], dictionary={}, exceptions=[]):
  try:
    print(textOpts)
    opc = input(inputOptText)
    if not opc.isdigit():
      mensaje = "Incorrect option!"
      raise ValueError
    opc = int(opc)
    if opc not in rangeList and opc not in dictionary and opc not in exceptions:
      mensaje = "Incorrect option!"
      raise ValueError
  except ValueError:
    print(mensaje)
    return getOpt(d.menu00[0], d.menu00[1], d.menu00[2], d.menu00[3], d.menu00[4])
  else:
    if opc in rangeList:
      if opc == 1:
        return getOpt(d.menu01[0], d.menu01[1], d.menu01[2], d.menu01[3], d.menu01[4])
      elif opc == 2:
        return getOpt(d.menu02[0], d.menu02[1], d.menu02[2], d.menu02[3], d.menu02[4])
      elif opc == 3:
        return getOpt(d.menu03[0], d.menu03[1], d.menu03[2], d.menu03[3], d.menu03[4])
      elif opc == 4:
        return getOpt(d.menu04[0], d.menu04[1], d.menu04[2], d.menu04[3], d.menu04[4])
      elif opc == 5:
        return getOpt(d.menu05[0], d.menu05[1], d.menu05[2], d.menu05[3], d.menu05[4])
      elif opc == 6:
        print("Program closed!")
    if opc in dictionary:
      if opc == 1 and dictionary[1] == 1:
        print(d.HumanPlayer)
        human = True
        newdni = f.newDni(human)
        newname = f.newName()
        newtype = f.newProfile()
        print(f.agregarregBD(newdni, newname, newtype, human))
        input("Enter to continue")
        return getOpt(d.menu01[0], d.menu01[1], d.menu01[2], d.menu01[3], d.menu01[4])
      elif opc == 2 and dictionary[2] == 1:
        print(d.nbp)
        human = False
        newdni = f.newDni(human)
        newname = f.newName()
        newtype = f.newProfile()
        print(f.agregarregBD(newdni, newname, newtype, human))
        input("Enter to continue")
        return getOpt(d.menu01[0], d.menu01[1], d.menu01[2], d.menu01[3], d.menu01[4])
      elif opc == 3 and dictionary[3] == 1:
        f.setgameplayer()
        dni= f.pedirdatos1_3()
        print(f.eliminarregBD(dni))
        input("Press any key to continue:")
        return getOpt(d.menu01[0], d.menu01[1], d.menu01[2], d.menu01[3], d.menu01[4])
      elif opc == 4 and dictionary[4] == 1:
        return getOpt(d.menu00[0], d.menu00[1], d.menu00[2], d.menu00[3], d.menu00[4])
      elif opc == 1 and dictionary[2] == 2:
        jugadoresactales={}
        f.setgameplayer()
        f.pedirdatos2_1()
        input(" " * 58 + "Press any key to continue:")
        return getOpt(d.menu02[0], d.menu02[1], d.menu02[2], d.menu02[3], d.menu02[4])
      elif opc == 2 and dictionary[2] == 2:
        return getOpt(d.menu022[0], d.menu022[1], d.menu022[2], d.menu022[3], d.menu022[4])
      elif opc == 1 and dictionary[1] == 22:
        f.escogermazoes()
        input(" " * 58 + "Press any key to continue:")
        return getOpt(d.menu022[0], d.menu022[1], d.menu022[2], d.menu022[3], d.menu022[4])
      elif opc == 2 and dictionary[2] == 22:
        f.escogermazopo()
        input(" " * 58 + "Press any key to continue:")
        return getOpt(d.menu022[0], d.menu022[1], d.menu022[2], d.menu022[3], d.menu022[4])
      elif opc == 0 and dictionary[0] == 22:
        return getOpt(d.menu02[0], d.menu02[1], d.menu02[2], d.menu02[3], d.menu02[4])
      elif opc == 3 and dictionary[3] == 2:
        f.roundmax()
        return getOpt(d.menu02[0], d.menu02[1], d.menu02[2], d.menu02[3], d.menu02[4])
      elif opc == 4 and dictionary[4] == 2:
        print("go back")
        return getOpt(d.menu00[0], d.menu00[1], d.menu00[2], d.menu00[3], d.menu00[4])
      elif opc == 1 and dictionary[1] == 3:
        print("3.1")
        input("Press any key to continue:")
        return getOpt(d.menu03[0], d.menu03[1], d.menu03[2], d.menu03[3], d.menu03[4])
      elif opc == 2 and dictionary[2] == 3:
        print("3.2")
        return getOpt(d.menu03[0], d.menu03[1], d.menu03[2], d.menu03[3], d.menu03[4])
      elif opc == 3 and dictionary[3] == 3:
        print("3.3")
        return getOpt(d.menu03[0], d.menu03[1], d.menu03[2], d.menu03[3], d.menu03[4])
      elif opc == 4 and dictionary[4] == 3:
        print("lina3.4")
        return getOpt(d.menu03[0], d.menu03[1], d.menu03[2], d.menu03[3], d.menu03[4])
      elif opc == 5 and dictionary[5] == 3:
        print("lina3.5")
        return getOpt(d.menu03[0], d.menu03[1], d.menu03[2], d.menu03[3], d.menu03[4])
      elif opc == 6 and dictionary[6] == 3:
        print("lina3.6")
        return getOpt(d.menu03[0], d.menu03[1], d.menu03[2], d.menu03[3], d.menu03[4])
      elif opc == 1 and dictionary[1] == 4:
        print(f.insert_ranking())
        input("Enter to continue")
        return getOpt(d.menu04[0], d.menu04[1], d.menu04[2], d.menu04[3], d.menu04[4])
      elif opc == 2 and dictionary[2] == 4:
        print(f.insert_ranking())
        input("Enter to continue")
        return getOpt(d.menu04[0], d.menu04[1], d.menu04[2], d.menu04[3], d.menu04[4])
      elif opc == 3 and dictionary[3] == 4:
        print(f.insert_ranking())
        input("Enter to continue")
        return getOpt(d.menu04[0], d.menu04[1], d.menu04[2], d.menu04[3], d.menu04[4])
      elif opc == 4 and dictionary[4] == 4:
        return getOpt(d.menu00[0], d.menu00[1], d.menu00[2], d.menu00[3], d.menu00[4])
      elif opc == 1 and dictionary[1] == 5:
        print("En construcción 5.1")
        return getOpt(d.menu05[0], d.menu05[1], d.menu05[2], d.menu05[3], d.menu05[4])
      elif opc == 2 and dictionary[2] == 5:
        cursorr = c.mydb.cursor()
        cursorr.execute(
          "select distinct cardgame_id, player_id, bet_points from player_game_round pg where bet_points = (SELECT MAX(bet_points) FROM player_game_round pgr where pgr.cardgame_id = pg.cardgame_id)")
        resultadosr = cursorr.fetchall()
        for fila2 in resultadosr:
          d.rep += "\n" + "".ljust(45) + str(fila2[0]).ljust(3) + '         ' + str(fila2[1]).ljust(
            9) + '            ' + str(fila2[2]).ljust(3) + '            ' + '\n'
        print(d.rep)
        input(" " * 53 + "Press enter to continue" + " " * 59)
        return getOpt(d.menu05[0], d.menu05[1], d.menu05[2], d.menu05[3], d.menu05[4])
      elif opc == 3 and dictionary[3] == 5:
        cursorr = c.mydb.cursor()
        cursorr.execute(
          "select distinct cardgame_id, player_id, bet_points from player_game_round pg where bet_points = (SELECT min(bet_points) FROM player_game_round pgr where pgr.cardgame_id = pg.cardgame_id)");

        resultadosr = cursorr.fetchall()

        for fila2 in resultadosr:
          d.reptres += "\n" + "".ljust(45) + str(fila2[0]).ljust(3) + '         ' + str(fila2[1]).ljust(
            9) + '            ' + str(fila2[2]).ljust(3) + '            ' + '\n'
        print(d.reptres)
        input("Enter to continue")
        return getOpt(d.menu05[0], d.menu05[1], d.menu05[2], d.menu05[3], d.menu05[4])
      elif opc == 4 and dictionary[4] == 5:
        print("En construcción 5.4")
        return getOpt(d.menu05[0], d.menu05[1], d.menu05[2], d.menu05[3], d.menu05[4])
      elif opc == 5 and dictionary[5] == 5:
        print("En construcción 5.5")
        return getOpt(d.menu05[0], d.menu05[1], d.menu05[2], d.menu05[3], d.menu05[4])
      elif opc == 6 and dictionary[6] == 5:
        cursorr = c.mydb.cursor()
        cursorr.execute(
          "SELECT * FROM 6_alt")
        resultadosr = cursorr.fetchall()
        for fila2 in resultadosr:
          d.repseis += "\n" + "".ljust(63) + str(fila2[0]).ljust(3) + "".ljust(14) + str(fila2[1]).ljust(3) + '\n'
        print(d.repseis)
        input("Enter to continue")
        return getOpt(d.menu05[0], d.menu05[1], d.menu05[2], d.menu05[3], d.menu05[4])
      elif opc == 7 and dictionary[7] == 5:
        cursorr = c.mydb.cursor()
        cursorr.execute(
          "select cardgame_id, count(distinct player_id) from player_game_round where is_bank like 1 group by cardgame_id;")
        resultadosr = cursorr.fetchall()
        for fila2 in resultadosr:
          d.repsiete += "\n" + "".ljust(54) + str(fila2[0]).ljust(3) + "".ljust(27) + str(fila2[1]).ljust(9) + '\n'
        print(d.repsiete)
        input("Enter to continue")
        return getOpt(d.menu05[0], d.menu05[1], d.menu05[2], d.menu05[3], d.menu05[4])
      elif opc == 8 and dictionary[8] == 5:
        cursorr = c.mydb.cursor()
        cursorr.execute(
          "select cardgame_id as Id_Game, avg(bet_points) as Average_Bet from player_game_round group by cardgame_id")
        resultadosr = cursorr.fetchall()
        for fila2 in resultadosr:
          d.repocho += "\n" + "".ljust(64) + str(fila2[0]).ljust(3) + "".ljust(8) + str(fila2[1]).ljust(6) + '\n'
        print(d.repocho)
        input("Enter to continue")
        return getOpt(d.menu05[0], d.menu05[1], d.menu05[2], d.menu05[3], d.menu05[4])
      elif opc == 9 and dictionary[9] == 5:
        cursorr = c.mydb.cursor()
        cursorr.execute(
          "select cardgame_id as Id_Game, avg(bet_points) as Average_Bet from player_game_round where round_num like 1 group by cardgame_id")
        resultadosr = cursorr.fetchall()
        for fila2 in resultadosr:
          d.repnueve += "\n" + "".ljust(63) + str(fila2[0]).ljust(3) + "".ljust(8) + str(fila2[1]).ljust(6) + '\n'
        print(d.repnueve)
        input("Enter to continue")
        return getOpt(d.menu05[0], d.menu05[1], d.menu05[2], d.menu05[3], d.menu05[4])
      elif opc == 10 and dictionary[10] == 5:
        cursorr = c.mydb.cursor()
        cursorr.execute(
          "select  distinct cardgame_id, avg(bet_points), max(round_num) from player_game_round group by cardgame_id;")
        resultadosr = cursorr.fetchall()
        for fila2 in resultadosr:
          d.repnueve += "\n" + "".ljust(63) + str(fila2[0]).ljust(3) + "".ljust(8) + str(fila2[1]).ljust(6) + '\n'
        print(d.repnueve)
        input("Enter to continue")
        return getOpt(d.menu05[0], d.menu05[1], d.menu05[2], d.menu05[3], d.menu05[4])
      elif opc == 11 and dictionary[11] == 5:
        return getOpt(d.menu05[0], d.menu05[1], d.menu05[2], d.menu05[3], d.menu05[4])

getOpt(d.menu00[0], d.menu00[1], d.menu00[2], d.menu00[3], d.menu00[4])