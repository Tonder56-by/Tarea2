##Nombre: Brandon de Jesus Garza Jasso            Matricula: 250218
#9
# Se desea ingresar un número por teclado correspóndiente a una calificación 
#se desea saber su equivalencia:
#19 – 20 : Sobresaliente
#16 ­ 18 : Muy Buena
#14 – 15 : Buena
#12 – 13 : Regular
#11 ó menos : Insuficiente


calificacion = int(input("Ingrese la calificación (de 0 a 20): "))

if calificacion >= 19 and calificacion <= 20:
    print("------Sobresaliente------")

elif calificacion >= 16 and calificacion <= 18:
    print("--Muy Buena--")

elif calificacion >= 14 and calificacion <= 15:
    print("Buena")

elif calificacion >= 12 and calificacion <= 13:
    print("Regular")

elif calificacion <= 11:
    print("Insuficiente")
else:
    print("Calificación fuera de rango")
