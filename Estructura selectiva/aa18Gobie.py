#Nombre: Brandon de Jesus Garza Jasso            Matricula: 250218
#18
#Una fábrica ha sido sometida a un programa de control de contaminación para lo cual se efectúa una revisión de los puntos IMECA generados por la
#fábrica. El programa de control de contaminación consiste en medir lospuntos IMECA que emite la fabrica en cinco días de una semana y si el promedio es superior a los 170 puntos entonces tendrá la sanción de parar
#su producción por una semana y una multa del 50% de las ganancias diariascuando no se detiene la producción. Si el promedio obtenido de puntosIMECA es de 170 o menor entonces no tendrá ni sanción ni multa. El
#dueño de la fábrica desea saber cuanto dinero perderá después de se sometido a la revisión.


ganancia_diaria = float (input("Ingrese la ganancia diaria de la fábrica: ")) 

imeca = [float(input(f"Ingrese los puntos IMECA del día {i+1}: ")) for i in range (5)] 
promedio = sum(imeca) / 5

if promedio > 170:
    multa = ganancia_diaria * 0.5
    perdida_t = (ganancia_diaria * 7) + multa

    print(f"La multa y penalizacion se basa en su ganancia diaria que es de {ganancia_diaria}")
    print(f"La multa: {multa}")
    print(f"Dinero que perderá la fábrica: ${perdida_t:.2f}")
else:
    print("Todo Okay buen trabajo :).")
