Este código muestra ejemplos de diferentes tipos de estructuras de datos en Python: listas, tuplas, conjuntos y diccionarios.

Las listas son estructuras de datos modificables que se definen utilizando corchetes y cuyos elementos están separados por comas. Por ejemplo, en la línea 5 se define una lista llamada "especs_subject" que contiene varios elementos de diferentes tipos (cadena, entero, etc.).

Las tuplas son similares a las listas, pero su contenido es inmodificable. En la línea 14 se define una tupla llamada "tupla" que también contiene varios elementos.

Los conjuntos son estructuras de datos que no permiten valores duplicados y no se pueden acceder mediante índices. En la línea 21 se define un conjunto llamado "conjunto" que contiene varios elementos.

Los diccionarios son estructuras de datos que almacenan pares clave-valor. En la línea 30 se define un diccionario llamado "trabajo" que contiene varios pares clave-valor relacionados con una persona (nombre, apellido, edad, etc.).

En general, este código muestra cómo se definen y utilizan estas estructuras de datos en Python. Sin embargo, se podría mejorar la legibilidad y la claridad agregando comentarios más detallados y explicando mejor el propósito de cada línea de código.


puedes comentar de una mejor manera este codigo py para que los aprendices lo entiendan mas facil     print("################################################################################");
print("Listas");
#las listas conocidas tambien conocidas como array o matriz.
# las listas son modifcables
#las listas se hacen nombrando unavariable pero guardando los diferentes datos dentro de un corchete
#dentro del cual sus definiciones van separadas por coma ejemplo:

especs_subject = ["Johan", "Henao", "Dj", True,1.85]

#el orden de inicio para llamar el primer elemento
# debes invocarlo con el numero 0 ejemplo: lista[0]

print (especs_subject[0]);

print(especs_subject);

especs_subject[2] = "Profesional"

print (especs_subject);


#las tuplas son arrays o matrices son iguales a las listas con la diferencia de que su contenido es inmodificable
print("las tuplas")




tupla = ("Johan", "Henao", "Dj", True,1.85)

print(tupla);

#tupla[1]="esto es una tupla"

#print (tupla);



print("  ");
print("  ");
print("################################################################################");


# Los conjuntos 
# no se puede acceder por medio de indice
#no permite valores duplicados
print("Conjuntos");

conjunto = {"Johan", "Henao", "Dj", True,1.85}





print("  ");
print("  ");
print("################################################################################");

#Diccionario 
#los valores internos se define por clave (Key) : valor(value),
#se encierra entre corchetes

print("Diccionarios  ");
print("  ");


trabajo = {
    'nombre': "Johan",
    'apellido': "Rojas",
    'edad' : 20 ,
    'ocupacion': "Operario"
}
print(trabajo);

print(trabajo['nombre']+" "+trabajo['apellido']+" ");



print("  ");
print("  ");
print("################################################################################");