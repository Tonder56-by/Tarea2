#Nombre: Brandon de Jesus Garza Jasso            Matricula: 250218
#3
#Escriba un Algoritmo que reciba como entrada dos enteros positivos
#distintos y escriba la diferencia entre el número mayor y el menor, asegúrese de que su programa escriba 6 tanto cuando la entrada es 9 15
#como cuando la entrada es 15 9

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))


resta = num1 - num2

if resta <= 0:
    resta = resta * -1
    #resta *=-1
print(f"La diferencia es {resta}")

    

