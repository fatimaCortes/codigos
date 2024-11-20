#################################################################################
#Programa 15

# Juego Piedra Papel y Tijera
# Programa que lea las opciones de 2 jugadores, y muestra el resultado
# Empate, gana jugador 1 o gana jugador 2
# Si introducimos una opción que no coindica con piedra, papel o tijera
# Diga que opción Incorrecta
#################################################################################
# Juego Piedra, Papel y Tijera

def obtener_opcion_jugador(jugador):
    opcion = input(f"Jugador {jugador}, elige piedra, papel o tijera: ")
    while opcion not in ['piedra', 'papel', 'tijera']:
        print("Opción incorrecta. Intenta de nuevo.")
        opcion = input(f"Jugador {jugador}, elige piedra, papel o tijera: ")
    return opcion

opcion_jugador1 = obtener_opcion_jugador(1)
opcion_jugador2 = obtener_opcion_jugador(2)

if opcion_jugador1 == opcion_jugador2:
    resultado = "Empate"
elif opcion_jugador1 == 'piedra':
    if opcion_jugador2 == 'tijera':
        resultado = "Gana Jugador 1"
    else:
        resultado = "Gana Jugador 2"
elif opcion_jugador1 == 'papel':
    if opcion_jugador2 == 'piedra':
        resultado = "Gana Jugador 1"
    else:
        resultado = "Gana Jugador 2"
elif opcion_jugador1 == 'tijera':
    if opcion_jugador2 == 'papel':
        resultado = "Gana Jugador 1"
    else:
        resultado = "Gana Jugador 2"

print(resultado)
