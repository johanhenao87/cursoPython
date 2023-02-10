sep = "----------------------------------------------------------------------------------"
espace = "  "
absoluto = 100.0

#Tiempo de Cursos

#tiempo minimo para ver los conceptos de Python es de una duracion de 2.5horas(2 horas y media)
# 7 horas como maximo y 4 horas en promedio
#Cusro de Python de Dalto en 1.5horas (hora y media)


mas_rapido_otros_cursos = 2.5
promedio_otros_cursos = 4
maximo_otros_cursos = 7
curso_dalto = 1.5

# A) Diferencia en porcentaje entre el curso actual y:
# - 1 el mas rapido de otros cursos
# - 2 el mas lento de otros cursos
# - 3 el promedio de los cursos


print("Solucion de los ejercicios")
print(espace)

r1 = absoluto - curso_dalto / mas_rapido_otros_cursos * absoluto
r1 = round(r1, 1)
print(f'el curso de dalto dura un {r1}% menos que el mas rapido de otros cursos')
print(espace)
print(sep)

r2 =  absoluto - curso_dalto / maximo_otros_cursos * absoluto
r2 = round(r2, 1)
print(f'el curso de dalto dura {r2}% menos que el mas lento de otros cursos ')
print(espace)
print(sep)

r3 = absoluto - curso_dalto / promedio_otros_cursos * absoluto
r3 = round(r3, 1)
print(f'el curso de dalto que dura {r3}%  menos que el promedio de otros cursos')
print(espace)
print(sep)


print(espace)
# B) Porcentaje de material inservible que se reduce en: 
# - 1 el promedio de los cursos
# - 2 el curso actual
print(sep)

crudo_dalto = 3.5
crudo_promedio = 5


r4 = absoluto - promedio_otros_cursos / crudo_promedio * absoluto
r4 = round(r4, 1)
print(f"Porcentaje de Material inservible reducido en el promedio de los cursos es del {r4}%")
print(espace)
print(sep)

r5 = absoluto - curso_dalto / crudo_dalto * absoluto
r5 = round(r5, 1)
print(f"Porcentaje de Material inservible reducido en el curso dalto es del {r5}%")

# Mostrando diferencias si los cursos duraran 10 horas


print(f"ver 10 horas de curso de dalto equivale a ver{round(promedio_otros_cursos / curso_dalto *10, 1)}Hrs de un curso promedio")
print(sep)
print(f"ver 10 horas de otros cursos   equivale a ver {round(curso_dalto / promedio_otros_cursos  *10, 1)}Hrs del curso de dalto")
print(sep)