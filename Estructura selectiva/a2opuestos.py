#Nombre: Brandon de Jesus Garza Jasso            Matricula: 250218
#2
#que lea 2 numeros enteros y verifique si son opuestos solo si uno es positivo y el otro negativo

num1= float(input("Ingrese el primer numero: "))
num2= float(input("Ingrese el segundor numero: "))

if num1 > 0 and num2 > 0 or num1 < 0 and num2 < 0:
    print("No son opestos")
else:
    print("SI SON")
