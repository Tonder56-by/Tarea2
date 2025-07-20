#Nombre: Brandon de Jesus Garza Jasso              Matricula: 250218
#17
#Calcular El gobierno desea saber el numero de pinos, oyameles y cedros que tendrá
#que sembrar en el bosque, si se sabe que en 10 metros cuadrados caben 8
#pinos, en 15 metros cuadrados caben 15 oyameles y en 18 metros
#cuadrados caben 10 cedros. También se sabe que una hectárea equivale a
#10 mil metros cuadrados.

metros = 10000  # 1 hectárea es 10,000 metros cuadrados

pinos = (metros / 10) * 8 #10m2 caben 8
oyameles = (metros / 15) * 15 #15m2 caben 15
cedros = (metros / 18) * 10 #18m2 caben 10

print(f"Número de pinos por hectárea: {pinos}")
print(f"Número de oyameles por hectárea: {oyameles}")
print(f"Número de cedros por hectárea: {int(cedros)}")
