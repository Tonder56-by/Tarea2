#Nombre: Brandon de Jesus Garza Jasso              Matricula: 250218
#14
#En un supermercado se hace una promoción, mediante la cual el cliente
#obtiene un descuento dependiendo de un numero que se escoge al azar. 
#menor a 74 es 15% y mayor a 74 es 20

import random as ran

totalc = float(input("Ingrese el total de la compra: "))
numero = ran.randint(0,100)
print("Número generado al azar:", numero)

if numero < 74:
    desc = totalc * 0.15
else:
    desc = totalc * 0.20
totdesc = totalc - desc

print(f"Descuento aplicado: ${desc}")
print(f"Total a pagar: ${totdesc}")


