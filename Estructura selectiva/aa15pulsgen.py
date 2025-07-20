#Nombre: Brandon de Jesus Garza Jasso            Matricula: 250218
#15
#Calcule las pulsaciones totales por cada 10 segundos (220 - edad) / 10 si es mujer (210 - edad) / 10

Edad = int(input("Ingrese su edad porfavor : "))
sexo = input("Ingrese su genero: H/M").lower()

if sexo == 'h': 
        puls = 220

elif sexo == "m":
        puls =210

else:
    print("Ingrese un sexo valido H o M")
    
tp= (puls - Edad) / 10
print("Su total de pulsaciones por cada 10 segundos es: ",tp)