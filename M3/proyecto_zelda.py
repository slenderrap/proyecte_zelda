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
    print("* " * 16)
    if len(prompt)!=0:
        for i in prompt:
            print(i)
    try:
        opc = input("What to do now?")
        assert opc.capitalize() in opciones
        return opc
    except AssertionError:
        historialPrompt(prompt,"Invalid Option")

def historialPrompt(prompt,NewLine):
    if len(prompt)==8:
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


# " "*76 seria todo el contenido
#56 seria la parte antes de la figura
#15 lo que ocupa la figura
#5 espacios derecha
import random
import os
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
("    \" || \"        "),
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
opciones = ("Continue", "New Game", "Help", "About", "Query", "Exit")

while flag_0:
    while flag_00:
        opcion = menu_principal(figuras[random.randint(1,len(figuras))],opciones,prompt)
        if opcion!=None:
            historialPrompt(prompt,opcion)
        # elif opcion == "Continue":
        #
        # elif opcion == "New Game":
        #
        # elif opcion == "Help":
        #
        # elif opcion == "About":
        #
        # elif opcion == "Query":
        # else:
        #     flag_00 = False
        #     flag_0 = False

