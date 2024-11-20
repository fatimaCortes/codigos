#################################################################################
# Escribe un programa que pida un número entero entre uno y doce e imprima el 
# número de días que tiene el mes correspondiente.
# Si introducimos otro número nos da un error.
#################################################################################


mes = int(input("\nIntroduce un número de mes (1-12): "))

dias_por_mes = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

if 1 <= mes <= 12:
    print(f"El mes {mes} tiene {dias_por_mes[mes]} días.")
else:
    print("Error: Número incorrecto.")
    