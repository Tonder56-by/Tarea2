#Nombre: Brandon de Jesus Garza Jasso              Matricula: 250218
#Titulo: numero maximo
#1
num1= float(input("Ingrese el primer numero: "))
num2= float(input("Ingrese el segundor numero: "))
num3= float(input("Ingrese el terceer numero: "))

if num1>num2:
    if num1>num3:
        max=num1
    else:
        max=num3
else:
    if num2>num3:
        max=num2
    else:
        max=num3

print(f"El numero mayo es: {max}")

#COMPUERTA LOGICA
if num1 >= num2 and num1 >= num3:
    mayor = num1
#
elif num2 >= num1 and num2 >= num3:
    mayor = num2
#
else: 
    mayor = num3
print(f"El numero mayor es: {mayor}")
    



