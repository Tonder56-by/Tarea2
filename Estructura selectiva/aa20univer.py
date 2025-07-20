#Nombre: Brandon de Jesus Garza Jasso              Matricula: 250218
#20 y 21
#Una institución educativa estableció un programa para estimular a los alumnos con buen rendimiento académico y que consiste en lo siguiente: Si el promedio es de 9.5 o mas y el alumno es de preparatoria,
#entonces este podrá cursar 55 unidades y se le hará un 25% de descuento. Si el promedio es mayor o igual a 9 pero menor que 9.5 y el
#alumno es de preparatoria, entonces este podrá cursar 50 unidades  y se le hará un 10% de descuento. Si el promedio es mayor que 7 y menor que 9 y el alumno es de
#preparatoria, este podrá cursar 50 unidades y no tendrá ningún descuento. Si el promedio es de 7 o menor, el numero de materias reprobadas
#es de 0 a 3 y el alumno es de preparatoria, entonces podrá cursar 45 unidades y no tendrá descuento.
#Si el promedio es de 7 o menor, el numero de materias reprobadas es de 4 o mas y el alumno es de preparatoria, entonces podrá
#cursar 40 unidades y no tendrá ningún descuento. ß Si el promedio es mayor o igual a 9.5 y el alumno es de profesional, entonces podrá cursar 55 unidades y se le hará un
#20% de descuento. ß Si el promedio es menor de 9.5 y el alumno es de profesional, entonces podra cursar 55 y no tendra descuento
#
#Obtener el total que tendrá que pagar un alumno si la colegiatura para alumnos
#de profesional es de $300 por cada cinco unidades y para alumnos de
#preparatoria es de $180 por cada cinco unidades.

nivel = input("Ingrese el nivel del alumno (preparatoria/profesional): ").lower()
prom = float(input("Ingrese el promedio del alumno: del 1-10 "))
reprobadas = int(input("Ingrese el número de materias reprobadas: "))

unidades = 0
descuento = 0


if nivel == "preparatoria":
    if prom >= 9.5:
        unidades = 55
        descuento = 0.25
        costo_uni = 36
    elif 9 <= prom < 9.5:
        unidades = 50
        descuento = 0.10
        costo_uni = 36
    elif 7 < prom < 9:
        unidades = 50
        descuento = 0
        costo_uni = 36
    elif prom <= 7 and reprobadas <= 3:
        unidades = 45
        descuento = 0
        costo_uni = 36
    elif prom <= 7 and reprobadas >= 4:
        unidades = 40
        descuento = 0
        costo_uni = 36


elif nivel == "profesional":
    if prom >= 9.5:
        unidades = 55
        descuento = 0.20
        costo_uni = 60
    else:
        unidades = 55
        descuento = 0
        costo_uni = 36

else:
    print("Nivel no válido.")
    exit()

total_bruto = unidades * costo_uni
monto_descuento = total_bruto * descuento
total_pagar = total_bruto - monto_descuento

print("\n--- Resultado ---")
print(f"Unidades que puede cursar: {unidades}")
print(f"Descuento aplicado: {descuento * 100:.0f}%")
print(f"Total antes del descuento: ${total_bruto:.2f}")
print(f"Descuento: ${monto_descuento:.2f}")
print(f"Total a pagar: ${total_pagar:.2f}")
