
from random import randint
opciones = ["piedra", "papel", "tijera"]
rounds_jugador = 0
rounds_pc = 0
ronda = 1
alias = input("Ingresa tu nombre: ")
while (rounds_pc < 2 and rounds_jugador < 2):
    print(f"Round {ronda}: {alias} vs pc") # Bubles de turno con While
    pc = opciones[randint(0, 2)]
    turno_usuario = input("Piedra, Papel o Tijera!, elegi una opción: ")
    turno_usuario = turno_usuario.replace(" ", "").lower()
    if turno_usuario in opciones:
        if turno_usuario == pc:
            print("Es un empate!!!\n")
        else:        
            if turno_usuario == "piedra" and pc == "papel": # condicionales piedra
                print(f"{alias}: Piedra - pc: Papel")
                print("Ops!!! perdiste, papel le gana a piedra")
                rounds_pc += 1
            elif turno_usuario == "piedra" and pc == "tijera":
                print(f"{alias}: Piedra - pc: Tijera")
                print("Bien hecho!, la piedra rompe la tijera")
                rounds_jugador += 1        
            elif turno_usuario == "papel" and pc == "tijera": # condicionales papel
                print(f"{alias}: Papel - pc: tijera")
                print("Ops!!! perdiste, la tijera corta el papel")
                rounds_pc += 1
            elif turno_usuario == "papel" and pc == "piedra":
                print(f"{alias}: Papel - pc: Piedra")
                print("Bien hecho!, el papel envuelve a la piedra")
                rounds_jugador += 1        
            elif turno_usuario == "tijera" and pc == "piedra": # condicionales tijera
                print(f"{alias}: Tijera - pc: Piedra")
                print("Ops!!! perdiste, la piedra rompe la tijera")
                rounds_pc += 1
            elif turno_usuario == "tijera" and pc == "papel":
                print(f"{alias}: Tijera - pc: Papel")
                print("Bien hecho!, la tijera corta el papel")
                rounds_jugador += 1
                print(f"MARCADOR {alias} : {rounds_jugador} - pc: {rounds_pc} \n\n")
            ronda += 1
    else:
        print(f"{turno_usuario} no es una opción correcta!\n")
if rounds_pc > rounds_jugador:
    print("Derrota Total!!!")
elif rounds_jugador > rounds_pc:
    print("Victoria impecable 😎!")
