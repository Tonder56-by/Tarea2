#Nombre: Brandon de Jesus Garza Jasso              Matricula: 250218
#10 y 11
#Elaborar un programa utilizando un menú
#Que pueda funcionar con MAYUSCULAS Y minusculas

def menu():
    while True: 
        print("Seleccione una ocpion ")
        print("N. Numero de cliente: ")
        print("D. Direccion:  ")
        print("T. Telefono: ")
        print("C. Ciudad: ")
        print("F. Fin del programa: ")

        opcion1 = input("Sleccion: ")
        opcion = opcion1.lower()

        if opcion == "n" :
            print("Numero de cliente: \nFulanito Maguaino")

        elif opcion == "d" :
            print("Direccion \nSiempre viva 123")

        elif opcion == "t" :
            print("Telefono \n6864839 ")

        elif opcion == "c" :
            print("Ciudad \nMexicali")

        elif opcion == "f" :
            print("Fin del programa")
            break
    
        else:
                print("Opcion no valida")

menu()

