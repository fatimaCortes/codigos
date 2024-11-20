#################################################################################
#Realiza un programa que pida por teclado el resultado (dato entero) obtenido 
#al lanzar un dado de seis caras y muestre por pantalla el número en letras 
#(dato cadena) de la cara opuesta al resultado obtenido.
#* Nota 1: En las caras opuestas de un dado de seis caras están los números: 
#1-6, 2-5 y 3-4.
#* Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, 
#se mostrará el mensaje: "ERROR: número incorrecto.".
#################################################################################


numero_dado = int(input("\nIntroduce el resultado del dado (1-6): "))


caras_opuestas = {1: "seis", 2: "cinco", 3: "cuatro", 4: "tres", 5: "dos", 6: "uno"}


if 1 <= numero_dado <= 6:
    print(f"La cara opuesta al {numero_dado} es {caras_opuestas[numero_dado]}.")
else:
    print("ERROR: número incorrecto.")