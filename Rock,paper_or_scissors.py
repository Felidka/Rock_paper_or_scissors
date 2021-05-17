import random
game_list = ["Roca", "Papel", "Tijera"]
computer = c = 0
command = p = 0
print("Puntaje : Computador " + str(c) + " Jugador "  + str(p))
#Bucle 
run = True
while run:
    computer_choice = random.choice(game_list)
    command = input("Roca, Papel o Tijera?: ")
    if command == computer_choice :
        print("Empate")
    elif command == "Roca":
        if computer_choice == "Tijera":
            print(" El jugador gano ")
            p += 1
        else:
            print(" La computadora gano ")
            c += 1
    elif command == "Papel":
        if computer_choice == "Roca":
            print("El jugador gano")
            p += 1
        else:
            print("La computadora gano")
            c += 1
    elif command == "Tijera":
        if computer_choice == "Papel":
            print("El jugador gano")
            p += 1
        else:
            print("La computadora gano")
            c += 1
    elif command == "Salir":
        break
    else:
        print("Comando erroneo")
    print("Jugador: " + command)
    print("Computador: " + computer_choice)
    print("")
    print("Puntaje: Computador " + str(c) + " Jugador " + str(p))
    print("")