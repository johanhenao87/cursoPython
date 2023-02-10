#Creando una lista list([])

#eje1
lista = list([1, 2, 3, 4])

#eje2
listado = (["hola", "johan", 20,50,30,True])


print("################################")
print("  ")

#devuelves la cantidad de elementos de la lista len()
#ejemplo 
lista1 =len(lista)
print (lista1)

print("################################")
print("  ")
#agregando un elemento a la lista con variable.append()
lista.append("sonar")
print(lista)

print("################################")
print("  ")

#agregando un elemento a la lista en un indice especifico insert lista.insert(key,"value")

lista.insert(3,"ma ")
print(lista)
print("################################")
print("  ")

#agregando varios elmentos a una lista con extend  lista.extend([1,2,3,4,5])

lista.extend([1,2,3,4,5])
print(lista)



print("********************************")
#eleminando elementos de la lista
print(".pop sacacmos un elemento de la lista indicando su indice")
#ejemplo
print(len(lista))

lista.pop(0)
print(lista)
print(len(lista))


lista.remove("sonar")
lista.remove("ma ")
print(lista)

lista.sort()

print(lista)

lista.reverse()
print(lista)

print("********************************")


#index verificando si un elemento se encuentra en la lista
elemento_encontrado



lista.clear()
print(lista)




print(" fin del programa  ")
