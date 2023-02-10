sep = "---------------------------------------------------------------------------------------------------------"
espace = "  "

frase = input("Dime una frase y calculare cuanto tardas en decirla: ")


palabras_separadas = frase.split(" ")
cantidad_palabras = len(palabras_separadas)

if cantidad_palabras*2 < 60 :
    print(f"dijiste {cantidad_palabras} palabras y tardarias {cantidad_palabras*2} segundos en decirlas")
elif cantidad_palabras*2> 60:
    print("calmate un poco por favor")
else: 
    print ("lo siento pero debes digitar una frase")


#palabras_seg_promedio = 2
#palabras_seg_max = 
#palabras_seg_min =




#
#







#
#

