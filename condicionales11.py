#####################################################################################
#La política de cobro de una compañía telefónica es:
#cuando se realiza una llamada el cobro es por el tiempo que ésta dura
#de tal forma que los primeros cinco minutos cuestan 1 euro
#los siguientes tres 80 céntimos,
#los siguientes dos minutos, 70 céntimos
#y a partir del décimo minuto, 50 céntimos.

#Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
#de mañana 15%, y en turno de tarde 10%. 
#Realice un programa para determinar cuánto debe pagar por cada concepto 
#una persona que realiza una llamada.
#####################################################################################

duracion = int(input("\nIntroduce la duración de la llamada en minutos: "))

dia = input("Introduce el día de la semana: ").strip().lower()
if dia != "domingo":
    turno = input("Introduce el turno (mañana o tarde): ").strip().lower()
else:
    turno = None  

if duracion <= 5:
    costo_llamada = duracion * 1
elif duracion <= 8:
    costo_llamada = 5 * 1 + (duracion - 5) * 0.80
elif duracion <= 10:
    costo_llamada = 5 * 1 + 3 * 0.80 + (duracion - 8) * 0.70
else:
    costo_llamada = 5 * 1 + 3 * 0.80 + 2 * 0.70 + (duracion - 10) * 0.50

if dia == "domingo":
    impuesto = costo_llamada * 0.03
elif turno == "mañana":
    impuesto = costo_llamada * 0.15
else:
    impuesto = costo_llamada * 0.10

total_a_pagar = costo_llamada + impuesto
print("\n")
print("Costo de la llamada antes de impuestos:", round(costo_llamada, 2), "euros")
print("Impuesto aplicado:", round(impuesto, 2), "euros")
print("Total a pagar:", round(total_a_pagar, 2), "euros")