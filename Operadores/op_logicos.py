#And    compara dos datos y solo en el caso de que ambos sean true
#devolvera true en el resto de los casos solo dara falso (false)

r1 = True & True #devolvera true
r2 = True & False #devolvera false
r3 = False & True #devolvera false
r4 = False & False #devolvera false

print ("Operador And  | "," R1: ", r1, " -R2: ", r2, " -R3: ", r3," -R4: ", r4)




#Or solo devuelve falso si ninguna se cumple, en el resto de casos devuelve true

r5 = True | True #devolvera true
r6 = True | False #devolvera true
r7 = False | True #devolvera true
r8 = False | False #devolvera false

print("Operador Or   |", " -R5: ", r5," -R6: ", r6," -R7: ", r7," -R8: ",r8)

#Not devuelve  lo contrario de la condicion true = false ---- y false = true

r9 =  not True #devolvera false
r10 = not False #devolvera True

r11 = not 2==2
r12 = not 2>2

print("Operador Not  |", " -R9: ",r9," -R10: ",r10," -R11: ",r11," -R12: ",r12)
