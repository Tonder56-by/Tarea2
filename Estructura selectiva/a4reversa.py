#Nombre: Brandon de Jesus Garza Jasso            Matricula: 250218
#4
#Elaborar un Algoritmo para invertir una cifra almacenada en una variable
#A de tal manera si ingresa 834 debe darle como salida 438 , el dato
#ingresado debe estar en un rango de 1 y 999


n = float(input("Ingrese su numero a voltear: "))

if n <= 100:
    dec = n // 10
    uni = n % 10
    reversa= uni * 10 + dec
    print(f"Su numero invertido :  {reversa}")

else:

    cente = n // 100
    dec = (n % 100) // 10
    uni = n % 10
    reversa = uni * 100 + dec * 10 + cente
    print(f"Su numero invertido : {reversa}")


