def menu_principal(figura,opciones,prompt):
    print("*"+" *"*38+" *")

    count = 0
    # iteramos sobre las skins
    for i in figura:
        count += 1
        if count == 5:
            print("*" + "  Zelda,Breath Of The Wild" + " " * 31 + i + "*")
            continue
        print("*" + " " * 57 + i + "*")
    print("*",end=" ")
    for i in opciones:
        if i!="Exit":
            print(i,end=", ")
        else:
            print(i,end="  ")
    if len(opciones) == 6:
        print("* " * 16)
    else:
        print("* " * 21)
    if len(prompt)!=0:
        for i in prompt:
            print(i)
    try:
        opc = input("What to do now ? ")
        assert opc.title() in opciones
        return opc
    except AssertionError:
        historialPrompt(prompt,"Invalid action")
        return "Invalid action"

def historialPrompt(prompt,NewLine,name=""):
    if "\n" in NewLine:
        NewLine.index("\n")
        NewLine += "\n"
        for i in range(NewLine.count("\n")):
            if i==0:
                inicio=0
                final = NewLine.index("\n")
            else:
                inicio=final+1
                final = NewLine.find("\n",inicio)
            if len(prompt) == 8:
                prompt[0], prompt[1], prompt[2], prompt[3], prompt[4], prompt[5], prompt[6], prompt[7] = \
                    prompt[1], prompt[2], prompt[3], prompt[4], prompt[5], prompt[6], prompt[7], NewLine[inicio:final].capitalize()
            else:
                prompt.append(NewLine.capitalize())
    elif NewLine.lower()=="new game":
        if len(prompt) == 8:
            prompt[0], prompt[1], prompt[2], prompt[3], prompt[4], prompt[5], prompt[6], prompt[7] = \
                prompt[1], prompt[2], prompt[3], prompt[4], prompt[5], prompt[6], prompt[7], NewLine.title()
        else:
            prompt.append(NewLine.title())
    elif name!="":
        if len(prompt) == 8:
            prompt[0], prompt[1], prompt[2], prompt[3], prompt[4], prompt[5], prompt[6], prompt[7] = \
                prompt[1], prompt[2], prompt[3], prompt[4], prompt[5], prompt[6], prompt[7], NewLine
        else:
            prompt.append(NewLine)

    elif len(prompt)==8:
        prompt[0],prompt[1],prompt[2],prompt[3],prompt[4],prompt[5],prompt[6],prompt[7]=\
        prompt[1],prompt[2],prompt[3],prompt[4],prompt[5],prompt[6],prompt[7],NewLine.capitalize()
    else:
        prompt.append(NewLine.capitalize())
    LimpiarPantalla()

def LimpiarPantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def Continue(titulo,contenido,opciones):
    print("*" +titulo+ " *" * 38 + " *")#saved games
    print("*" + " " * 77 + "*")#consultas 1 espacio arriba otro abajo ordenada de antigua a más nueva
    for i in opciones:
        if i!="Back":
            print(i,end=", ")
        else:
            print(i,end="  ")
    print("* " * 16)
def saveGames(lista):#esta funcion se encarga de pasarle la lista de las ultimas partidas guardadas +
    historial=[("")]  # a la funcion dialogos.generador_menus
    diccionari_jugadors={}
    for i in range(len(lista)):#agreagamos los resultados de la query anterior en un diccionario con el id de partida
        diccionari_jugadors[i] = {"data_partida":lista[i][1],"player":lista[i][2],"region":lista[i][3]}

    for i in range(len(diccionari_jugadors.keys())):
        for j in range(len(diccionari_jugadors.keys())-1):#ordenamos con bubble sort
            if diccionari_jugadors.get(j).get("data_partida")<diccionari_jugadors.get(j+1).get("data_partida"):
                diccionari_jugadors[j+1],diccionari_jugadors[j]=diccionari_jugadors[j],diccionari_jugadors[j+1]

    for i in range(len(diccionari_jugadors.keys())):#como sabemos que ya esta ordenador recorremos el diccionario por las claves
        if len(historial)==9: #quando vaya a introducir la novena fila sale del bucle porque solo son las ultimas 8 partidas
            diccionari_jugadors.pop(i)
        else:
            historial.append("{}: {} - {}, {}  ".format(i,diccionari_jugadors.get(i).get("data_partida"),diccionari_jugadors.get(i).get("player"),diccionari_jugadors.get(i).get("region")).ljust(66) + u"\u2665" + "3/4".rjust(5)),
    for i in range(10-len(historial)): #aqui terminamos de rellenar los espacios en blanco para mantener todas las lineas de la plantilla
        historial.append(("  "))

    return historial,diccionari_jugadors #devolvemos el historial para que aparezca por pantalla y
                                         # el diccionario para cuando queramos jugar o eliminar una partida


def opcionesPlantilla(opciones,prompt,dicc):
    for i in prompt:
        print(i)
    opc = input("What to do now ? ").capitalize()
    opc_texto = ""
    opc_numero = ""
    for i in range(len(opc)):
        if opc[i].isalpha():
            opc_texto += opc[i]
        elif opc[i].isdigit():
            opc_numero += opc[i]
    if opc_numero != "":
        opc = opc.replace(opc_numero,"X")


    if opc in opciones:
        if (opc_texto == "Play" or opc_texto == "Erase") and opc_numero.isdigit() and int(opc_numero) in dicc.keys():
            historialPrompt(prompt,opc_texto.capitalize()+ " "+opc_numero)
            if opc_texto == "Play":
                pass
            else:
                cursor.execute("set FOREIGN_KEY_CHECKS=0")
                cursor.execute("delete from game where user_name='{}'".format(dicc.get(int(opc_numero)).get("player")))
                mi_conexion.commit()
                cursor.execute("set FOREIGN_KEY_CHECKS=1")
        elif opc_texto=="Help":
            historialPrompt(prompt, opc_texto)
            soloBack(dialogos.help_saved_games_top,dialogos.help_saved_games_end,dialogos.help_saved_games_content)
        else:
            historialPrompt(prompt, opc_texto)
    else:
        historialPrompt(prompt,"Invalid action")


    return opc_texto, prompt

def soloBack(top,end,content):
    opt = ""
    while opt!="Back":
        dialogos.generador_menus(top, end, content)
        for i in prompt:
            print(i)
        opt=input("What to do now ?").capitalize()
        if opt!="Back":
            historialPrompt(prompt, "Invalid action")
        else:
            historialPrompt(prompt, "Back")

def queries(consulta):
    if consulta==1:
        cursor.execute("select * from show_players")
        rows = cursor.fetchall()
        for i in rows:
            print(i)
    elif consulta==2:
        cursor.execute("select * from games_played")
        rows = cursor.fetchall()
        for i in rows:
            print(i)

    elif consulta==3:
        cursor.execute("select * from acquired_weapons")
        rows = cursor.fetchall()
        for i in rows:
            print(i)
    elif consulta==4:

        print(cursor.execute("select * from food_eaten"))
    else:
        cursor.execute("select * from max_bloodmoons")
        rows = cursor.fetchall()
        for i in rows:
            print(i)
    input("Press 'Enter' to continue")

# " "*76 seria todo el contenido
#56 seria la parte antes de la figura
#15 lo que ocupa la figura
#5 espacios derecha

import random
import os
import mysql.connector
from funciones import dialogos
mi_conexion = mysql.connector.connect(
    host="4.231.10.226",
    user="zelda",
    port="3306",
    password="link",
    database="zelda_pre"


    #la base de datos real es zelda, esta es de pruebas


)

cursor = mi_conexion.cursor()



flag_0=True
flag_00=True

prompt=[]
skin_1=(
("         ##         "), #15 de ancho
("         ##         "),
("      ##~~~         "),
("     ###~~~O        "),
("     ###~~~ \       "),
("       |@@@| \      "),
("       |   |  \     "),
("       =   ==       "),
("   %%%%%%%%%%%%     "),
("%%%%%%%%%%%%%%%     "),
)


skin_2=(
("          &&        "), #16 de ancho
("         oo &       "),
("$        -- &##     "),
("$$      <<OO####    "),
(" $$   //OOO####     "),
("  $$// OO#####      "),
("    **   OOO###     "),
("     &   @@@@\      "),
("         Q  Q       "),
("         Q  Q       "),
)

skin_3=(
("      &&            "), #15 de ancho
("     ####           "),
("    \" || \"          "),
(" @@@@@@@@@@@@@      "),
("@     ||@@@         "),
("      |@@@          "),
("     @@@            "),
("   @@@||      @     "),
("@@@@@@@@@@@@@@      "),
("      ||            "),
)

figuras={1:skin_1,
         2:skin_2,
         3:skin_3}

cursor.execute("select * from save_games")
rows = cursor.fetchall()
if len(rows)==0:
    opciones = ("New Game", "Help", "About", "Query", "Exit")

else:
    opciones = ("Continue", "New Game", "Help", "About", "Query", "Exit")
    opciones_guardadas = ("Play X","Erase X","Help","Back")
    contenido="X"




while flag_0:
    while flag_00:
        opcion = menu_principal(figuras[random.randint(1,len(figuras))],opciones,prompt).title()

        if opcion == "Continue":

            if len(rows) == 1:
                input("Empezaria el juego")
            else:
                opc=""
                historialPrompt(prompt,opcion)
                while opc != "Back":

                    contenido,diccionarioPartidas=saveGames(rows)
                    dialogos.generador_menus(dialogos.saved_games_top, dialogos.saved_games_end,contenido)
                    opc,prompt = opcionesPlantilla(opciones_guardadas,prompt,diccionarioPartidas)
                    if "Erase" in opc:
                        cursor.execute("select * from save_games")
                        rows = cursor.fetchall()
                        opciones = ("Continue", "New Game", "Help", "About", "Query", "Exit")
                        opciones_guardadas = ("Play X", "Erase X", "Help", "Back")
                        contenido = "X"

        elif opcion == "New Game":
            opc = ""
            historialPrompt(prompt, opcion)
            while opc != "Back":
                dialogos.generador_menus(dialogos.new_game_top, dialogos.new_game_end, dialogos.new_game_content)
                for i in prompt:
                    print(i)
                opc = input("What's your name (Link)?").title()

                if opc == "Back":
                    historialPrompt(prompt, opc)
                elif opc== "Help":
                    historialPrompt(prompt, opc)
                    soloBack(dialogos.help_new_game_top, dialogos.help_new_game_end, dialogos.help_new_game_content)
                else:
                    if opc=="":

                        historialPrompt(prompt,"Welcome to the game, Link","Link")
                        name=opc
                        break
                    elif opc.replace(" ","").isalnum() and 3<=len(opc)<=10:

                        historialPrompt(prompt,"Welcome to the game, {}".format(opc),opc)
                        name=opc
                        break
                    else:

                        historialPrompt(prompt, "'{}' is not a valid name".format(opc))

            if opc !="Back":
                opt=""
                while opt!="Continue":
                    #mostrar legend
                    dialogos.generador_menus(dialogos.legend_top,dialogos.legend_end,dialogos.legend_content)
                    for i in prompt:
                        print(i)
                    opt = input("Type 'Continue' to continue: ").capitalize()
                    if opt != "Continue":
                        historialPrompt(prompt,"Invalid action")
                    else:
                        historialPrompt(prompt,opt)
                opt = ""
                while opt != "Continue":
                    dialogos.generador_menus(dialogos.plot_top, dialogos.plot_end, dialogos.plot_content)
                    for i in prompt:
                        print(i)
                    opt = input("Type 'Continue' to continue: ").capitalize()
                    if opt != "Continue":
                        historialPrompt(prompt, "Invalid action")
                    else:
                        historialPrompt(prompt, opt)

        elif opcion == "Help":
            historialPrompt(prompt, opcion)
            soloBack(dialogos.help_main_menu_top, dialogos.help_main_menu_end, dialogos.help_main_menu_content)

        elif opcion == "About":
            historialPrompt(prompt, opcion)
            soloBack(dialogos.about_top,  dialogos.about_end, dialogos.about_content)

        elif opcion == "Query":
            opc = ""
            historialPrompt(prompt, opcion)
            while opc != "Back":
                dialogos.generador_menus(dialogos.queries_top, dialogos.queries_end, dialogos.queries_content)
                for i in prompt:
                    print(i)
                opc = input("What to do now ? ").title()
                if opc=="Back":
                    historialPrompt(prompt, opc)
                else:
                    try:
                        assert opc.startswith("Select ") and opc[7:].isdigit() and 1 <= int(opc[7:]) <= 5
                        historialPrompt(prompt,opc)
                        queries(int(opc[-1]))
                    except AssertionError:
                        historialPrompt(prompt, "Invalid action")



        elif opcion == "Exit":
            flag_00 = False
            flag_0 = False


