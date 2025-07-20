#Nombre: Brandon de Jesus Garza Jasso              Matricula: 250218
#16
#En una escuela la colegiatura de los alumnos se determina según el numero
#de materias que cursan. El costo de todas las materias es el mismo.
#si es mas de 9 un descuento del 30% sino se le agrega el 10% de iva

materias = int(input("Ingrese el número de materias: "))
costo = float(input("Ingrese el costo por materia: "))
prom = float(input("Ingrese el promedio del alumno: "))

colegiatura = materias * costo

if prom >= 9:
    pago = colegiatura * 0.70
else:
    pago = colegiatura * 1.10

print(f"El total a pagar es: ${pago:.2f}")
