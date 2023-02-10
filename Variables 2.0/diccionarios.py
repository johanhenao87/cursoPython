#creando diccionarios con dict()

diccionario = dict(nombre="Johan",apellido="Rojas",)

#las listas no pueden ser claves usamos fronzenset para meter conjuntos diccionario ={frozenset(["DALTO", "RANCIO",])}

diccionario = {frozenset(["DALTO", "RANCIO",]):"JAJAJA"}




print(diccionario)

#CREANDO DICCIONARIOS CON fromkeys  dict.fromkeys

repor = dict.fromkeys(["nombre","apellido"],"Johan")
#                     funciona como lista iterable, y el siguiente valor es fijo o por defecto
print(repor)




print("Comienzo")
for i in [0, 1, 2]:
    print("Hola ", end="")
print()
print("Final")