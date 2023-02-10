diccionario = dict(nombre="Johan",apellido="Rojas",subs=1000000,)

for valor in diccionario.items():
    key = valor[0]
    value = valor[1]
    print(f"la clave es {key} y el valor es {value}")





frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]

for fruta in frutas:
    if fruta == "granada":
        continue
    print(f"Me voy a comer una {fruta}")


print("\n================================")
print("fin de codigo")



