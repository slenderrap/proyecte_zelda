# Funcion encargada de generar las pantallas de dialogo que suceden antes de iniciar y durante la partida.
#nos conectamos a la base de datos

# Los parentesis indican salto de linea
# top y end añadir 1 y 2 espacios dependiendo de Longitud.

# EJEMPLO:
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

def generador_menus(top,end,content):

    #Main menu
    print("* " + top + ("* " * ((77 - len(top)) // 2)) + "*")  # Anchura: 79
    for i in content:
        print("*" + " " * 2 + i + (" " * (75 - len(i))) + "*")

    print("* " + end + ("* " * ((77 - len(end)) // 2)) + "*")



# MAIN MENU
help_main_menu_top = "Help, main menu "
help_main_menu_end = "Back  "
help_main_menu_content = (("  "),("  "),("  Type 'continue' to continue a saved game"),
                    ("  Type 'new game' to start a new game"),
                    ("  Type 'about' to see information about the game"),
                    ("  Type 'exit' to exit the game"),("  "),("  "),
                    ("  Type 'back' now to go back to 'Saved games'"),("  "))

# SAVED GAMES
saved_games_top = "Saved games "
saved_games_end = "Play X, Erase X, Help, Back "
saved_games_content = (("  "),("  "),("  "),("  "),("  "),("  "),("  "),("  "),("  "),("  "))







# HELP, SAVED GAMES
help_saved_games_top = "Help, saved games "
help_saved_games_end = "Back  "
help_saved_games_content =  (("  "),("  "),("  Type 'play X' to continue playing the game 'X'"),
                            ("  Type 'erase X' to erase the game 'X"),
                            ("  Type 'back' now to back to the main menu"),
                            ("  "),("  "),("  "),
                            ("  Type 'back' now to go back to 'Saved games'"),(""))

# NEW GAME
new_game_top = "New game  "
new_game_end = "Back, Help  "
new_game_content =  (("  "),("  "),("  "),("  "),("  Set your name ?"),
                    ("  "),("  "),("  "),
                    ("  Type 'back' now to go back to 'Main Menu'"),("  "))

# HELP, NEW GAME
help_new_game_top = "Help, new game  "
help_new_game_end = "Back  "
help_new_game_content = (("  "),("  "),("  When asked, type your name and press enter"),
                        ("  if 'Link' is fine to you, just press enter"),
                        ("  "),
                        ("  Name must be between 3 and 10 characters long and only"),
                        ("  letters, numbers and spaces are allowed"),
                        ("  "),
                        ("  Type 'back' now to go back to 'Set your name'"),("  "))

# ABOUT
about_top = "About "
about_end = "Back  "
about_content = (("  "), ("  Game developed by 'Nombre del equipo' :"),
                ("  "),
                ("        Oriol Arribas"),
                ("        Erik Pinto"),
                ("        Sergio Fernández"),
                ("  "),
                ("  "),
                ("  Type 'back' now to go back to 'Main Menu'"),
                ("  "))

# LEGEND
legend_top = "Legend  "
legend_end = "Continue  "
legend_content = (("  "), ("  10,000 years ago, Hyrule was a land of prosperity thanks to the Sheikah"),
                ("  tribe. The Sheikah were a tribe of warriors who protected the Triforce,"),
                ("  "),
                ("  But one day, Ganondorf, an evil sorcerer, stole the Triforce and began"),
                ("  to rule Hyrule with an iron fist."),
                ("  "),
                ("  The princess, with the help of a heroic young man, managed to defeat"),
                ("  Ganondorf and recover the Triforce."),
                ("  "))

# PLOT
plot_top = "Plot  "
plot_end = "Continue  "
plot_content = (("  "), ("  "), ("  Now history is repeating itself, and Princess Zelda has been captured by"),
                ("  Ganon. He has taken over the Guardians and filled Hyrule with monsters."),
                ("  "),
                ("  "),
                ("  But a young man named 'Link' has just awakened and"),
                ("  must reclaim the Guardians to defeat Ganon and save Hyrule."),
                ("  "),
                ("  "))




#QUERIES
queries_top = "Queries "
queries_end = "Select X, Back  "
queries_content = (("  "),("  "),
                   ("  1: User has played"),
                   ("  2: Quantity of games played per user"),
                   ("  3: Weapons used per user and game where he spend more this weapon"),
                   ("  4: Meal eat per user and game where he eat more this meal"),
                   ("  5: Stadistic of 'Blood moons'"),
                   ("  "),
                   ("  "),
                   ("  ")
                   )


# HELP, INVENTORY
# plot_top = "Help, inventory  "
# plot_end = "Back  "
# plot_content = (("  "),("  Type 'show inventory main' to show the main inventory"),
#                 ("        (main, weapons, Food)"),
#                 ("  Type 'eatX' to eat X,where X is a Food item"),
#                 ("  Type 'Cook X' to Cook X, where X is a Food item"),
#                 ("  Type 'equip X' to equip X, where X is a weapon"),
#                 ("  Type 'unequip X' to unequip X, where X is a weapon"),
#                 ("  "),
#                 ("  Type 'back' now to go back to the 'Game'"),
#                 ("  "))
#
# # LINK DEATH
# plot_top = "Link Death  "
# plot_end = "Continue  "
# plot_content = (("  "),("  "),("  "),("  "),("  Game Over."),
#                 ("  "),
#                 ("  "),
#                 ("  "),
#                 ("  "),
#                 ("  "))
#
# # ZELDA SAVED
# plot_top = "Zelda saved "
# plot_end = "Continue  "
# plot_content = (("  "),("  "),("  "),("  "),("  Congratulations, Link has saved Princess Zelda."),
#                 ("  Thanks for playing!"),
#                 ("  "),
#                 ("  "),
#                 ("  "),
#                 ("  "))

# # MAIN MENU
# generador_menus(help_main_menu_top, help_main_menu_end, help_main_menu_content)
# # SAVED GAMES
# generador_menus(saved_games_top, saved_games_end, saved_games_content)
# # HELP, SAVED GAMES
# generador_menus(help_saved_games_top, help_saved_games_end, help_saved_games_content)
# # NEW GAME
# generador_menus(new_game_top, new_game_end, new_game_content)
# # HELP, NEW GAME
# generador_menus(help_new_game_top, help_new_game_end, help_new_game_content)
# # ABOUT
# generador_menus(about_top, about_end, about_content)
# # LEGEND
# generador_menus(legend_top, legend_end, legend_content)
# # PLOT
# generador_menus(legend_top, legend_end, legend_content)
# # PLOT
# generador_menus(plot_top, plot_end, plot_content)

