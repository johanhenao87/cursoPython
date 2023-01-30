
c1 = "Hola, soy, Johan"
c2 = "Bienvenido "
separador = "###################################################################################################### "
#dir - Devuelve todos los atributos de un objeto

#print(dir(c1))
print(separador)
#upper Pasa todo a MAYUSCULA - forma de usarlo  variable.upper()
print("Funcion Upper: Convierte cadenas de texto en Mayusculas...")
print(c1.upper())

print(separador)
#lower pasa todo a minuscula - forma de usarlo variable.lower()
print("Funcion Lower: Convierte cadenas de texto en minusculas...")
print(c1.lower())

print(separador)
#capitalize pasa la primera letra a Mayuscula -forma de usarlo variable.capitalize()
print("Funcion Capitalize: Convierte cadenas de texto en minusculas...")
print(c1.lower())

print(separador)
#buscamos una cadena en otra cadena si no hay resultados devuelve -1

busqueda_find = c1.find("h")

print(busqueda_find)


print(separador)
#buscamos una cadena en otra cadena si no hay concidencias devuelve un error o exepcion

busqueda_index = c1.index("H")

print(busqueda_index)



print(separador)
#si es numerico : devuelce true en caso contrario false

es_numerico = c1.isnumeric()
print(es_numerico)


print(separador)
#si es numerico : devuelce true en caso contrario false
print("es Numerico? ")
es_alfanumerico = c1.isalpha()
print(es_alfanumerico)


print(separador)
#Contador (count) contamos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencias

contar_coincidencias = c1.count("o")
print("Count: ")
print(contar_coincidencias)


print(separador)


#contamos cuantos caracteres tiene una cadena

cant_caract = len(c1)
print("Len: ")
print(cant_caract)



print(separador)
#Verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = c1.startswith("Hola")
print("Empieza con - Funcion o metodo de verificacion")

print(empieza_con)

print(separador)
#Verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = c1.endswith("n")
print("termina con - Funcion o metodo de verificacion")

print(termina_con)


#remplaza un pedazo de la cadena dada,

cadena_nueva = c1.replace("ohan", "ulian")
print("termina con - Funcion o metodo de verificacion")

print(cadena_nueva)


print(separador)
#separar cadenas Split

separadas = c1.split(",")

print(separadas)
print(separador)