#################################################################################
# Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba 
# el dí­a correspondiente. 
# Si introducimos otro número nos da un error.
#################################################################################

dia_sem = int(input("\nIntroduce un día de la semana (1-7): "))

dias = {1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 5: "Viernes", 6: "Sábado", 7: "Domingo"}

if 1 <= dia_sem <= 7:
    print(f"El día correspondiente es {dias[dia_sem]}.")
else:
    print("Error: Número incorrecto.")
    