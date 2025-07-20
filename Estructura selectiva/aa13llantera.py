#Nombre: Brandon de Jesus Garza Jasso              Matricula: 250218
#13
#Calcular el total que una persona debe pagar en un llantera, si el precio de
#cada llanta es de $800 si se compran menos de 5 llantas y de $700 si se
#compran 5 o mas.

compra = float(input("Cuantas llantas desea comprar hoy? : "))

if compra >= 5:
    llanta = 700
    total = compra * llanta
else:
    llanta = 800
    total =  llanta * compra

print(f"Su total es de {total}")
