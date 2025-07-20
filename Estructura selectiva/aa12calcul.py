#Nombre: Brandon de Jesus Garza Jasso            Matricula: 250218
#12
#Elabore un Algoritmo que lea dos variables enteras a y b. El programa debe
#leer un carácter y tomar una de las siguientes determinacione
#Si es '+' debe sumar las dos variables
#Si es '­ ' debe restar las dos variables
#Si es '* ' debe multiplicar las dos variables
#Si es '/ ' debe dividir las dos variables
#Si es '% ' debe obtener el residuo de la división.

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
op = input("Ingrese la operación (+, -, *, /, %): ")

if op == '+':
    resultado = a + b
elif op == '-':
    resultado = a - b
elif op == '*':
    resultado = a * b
elif op == '/':
    if b != 0:
        resultado = a / b
    else:
        print("Error: División por cero")
        exit()
elif op == '%':
    if b != 0:
        resultado = a % b
    else:
        print("Error: División por cero")
        exit()
else:
    print("Operador no válido")
    exit()

print(f"Resultado: {resultado}")
