#Nombre: Brandon de Jesus Garza Jasso            Matricula: 250218
#8
#vocales

vocal = input("Ingresa una vocal: ").lower()

if vocal in ["a", "e", "o"]:
    print("La vocal es abierta")
elif vocal in ["i", "u"]:
    print("La vocal es cerrada")
else:
    print("No es una vocal válida")
