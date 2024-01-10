
def generador_menus(top,end,content):

    #Main menu
    print("* " + top + ("* " * ((77 - len(top)) // 2)) + "*")  # Anchura: 79
    for i in content:
        print("*" + " " * 4 + i + (" " * (73 - len(i))) + "*")

    print("* " + end + ("* " * ((77 - len(end)) // 2)) + "*")




#Los parentesis indican salto de linea
#Top y end añadir 1 y 2 espacios dependiendo de Longitud.
#EJEMPLO:
# top = "Help, main menu "
# end = "Back  "
# content = ((""),(""),("Type 'continue' to continue a saved game"),
#              ("Type 'new game' to start a new game"),
#              ("Type 'about' to see information about the game"),
#              ("Type 'exit' to exit the game"),(""),(""),
#              ("Type 'back' now to go back to 'Saved games'"),(""))
#
#
# generador_menus(top,end,content)

