#Nombre: Brandon de Jesus Garza Jasso            Matricula: 250218
#7
#Calcular la edad

from datetime import datetime as da

nacimiento =da.strptime(
    input("Ingrese su fecha de nacimiento: (dd-mm-aaaa)"),
    "%d-%m-%Y" )
edad = da.now().year - nacimiento.year

cumplio = (da.now().month, da.now().day) >= (nacimiento.month, nacimiento.day)
if not cumplio: edad -= 1
print(f"Tienes {edad} años")

