#creando un conjunto con set()

conjunto = set(["dato1"])

#metiendo un conjunto dentro de otro conjunto

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}



#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado1 = conjunto2 <= conjunto1

print(resultado)
print(resultado1)


#verificando si es un superconjunto (superset)
resultado2 = conjunto2.issuperset(conjunto1)
resultado3 = conjunto1 > conjunto2

print(resultado2)
print(resultado3)


#verificando si hay algun numero en comun
resultado4 = conjunto2.isdisjoint(conjunto1)


print(resultado4)



