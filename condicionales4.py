##################################################################################
# Crea un programa que pida al usuario dos números y muestre su división 
# si el segundo no es cero, o un mensaje de aviso en caso contrario.
#################################################################################

numerador = int(input("\nIntroduce el primer número: "))
denominador = int(input("Introduce el segundo número: "))


if denominador != 0:
    division = numerador / denominador
    print("\nLa división es: ",division)
else:
    print("\nNo se puede dividir entre cero.")
    
    