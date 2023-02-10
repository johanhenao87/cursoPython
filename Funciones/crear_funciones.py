#creando una funcion simple

nombre = input("Ingresa el nombre: ")
apellido = input("Ingresa el apellido: ")
sexo = input("Ingrese su genero: ")


def saludar(nombre,apellido,sexo):
    sexo = sexo.lower()
#    if (nombre = "" or apellido == "" or sexo == ""):
#         print("Hola,  como estas?")
    if  (sexo == "mujer"):
        genero = "Señora"
    elif (sexo == "hombre"):
        genero = "Señor"
    else: 
        genero = "corazon"
         
    print(f"Hola {nombre}  {apellido},  como estas mi {genero}?")


saludar(nombre,apellido,sexo)
