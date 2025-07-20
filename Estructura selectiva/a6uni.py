#Nombre: Brandon de Jesus Garza Jasso            Matricula: 250218
#6
#En una Universidad Estatal, los cargos por colegiatura son de $50 
# (dólares) por materia, con un cargo máximo de $750 independientemente
# del número de asignaturas tomadas. Así un estudiante que cursa 12
# materias pagaría $600, mientras que toma 21 pagaría el cargo máximo de
# $750. Escriba un Algoritmo en el que la entrada es el número de materias
# y la colegiatura es la salida.

print("---Cada materia tiene un costo de $50 dolares---")
mate = float(input("Cuantas materias desea llevar este semestre? : "))

total = mate * 50

if total > 750:
    total = 750

print(f"Su total en colegiatura es de : {total}")