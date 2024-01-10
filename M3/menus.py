
parte1 = ("* " * 40)

parte2 = ("*" + " Continue, New Game, Help, About, Exit " + "* "*20)



skin_1=(
("         ##         "), #14 de ancho
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
("          &&        "), #15 de ancho
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
("      &&            "), #14 de ancho
("     ####           "),
("     \"||\"           "),
(" @@@@@@@@@@@@@      "),
("@     ||@@@         "),
("      |@@@          "),
("     @@@            "),
("   @@@||      @     "),
("@@@@@@@@@@@@@@      "),
("      ||            "),
)

#Imprimimos parte 1(Linea de arriba)
print(parte1)

##--EJEMPLO DE USO--

#variable para contar lineas impresas
count = 0
#iteramos sobre las skins
for i in skin_1:#<-Modificamos skin_1 con cualquier skin
    count += 1
    if count == 5:
        print("*" +"  Zelda,Breath Of The Wild"+ " " * 31 + i + "*")
        continue

    print("*"+" " * 57 + i + "*")

#Imprimimos parte 2(Linea de abajo)
print (parte2)
