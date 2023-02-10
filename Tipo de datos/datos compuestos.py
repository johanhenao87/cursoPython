print("################################################################################");
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











