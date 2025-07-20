###Nombre: Brandon de Jesus Garza Jasso            Matricula: 250218
#19
#Fruteria con descuento por el numero de kilos 10 = 20%, mas de  5 = 15% y mas de 2  a 5 = 10% 

precio_k = float(input("Ingrese el precio por kilo de manzana: "))
kilos = float(input("Ingrese cuántos kilos compró: "))

tot = precio_k * kilos

if kilos > 10:
    descuento = tot * 0.20
elif kilos > 5:
    descuento = tot * 0.15
elif kilos > 2:
    descuento = tot * 0.10
else:
    descuento = 0

tot_pagar = tot - descuento
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Total a pagar: ${tot_pagar:.2f}")
