# Operadores aritméticos en Python: suma, resta, módulo y precedencia

a = 15
b = 7           
# Suma
suma = a + b
print("Suma:", suma)  # Imprime el resultado de la suma
# Resta
resta = a - b
print("Resta:", resta)  # Imprime el resultado de la resta
# Módulo
modulo = a % b
print("Módulo:", modulo)  # Imprime el resultado del módulo
# Multiplicación
multiplicacion = a * b
print("Multiplicación:", multiplicacion)  # Imprime el resultado de la multiplicación
# División      
division = a / b    
print("División:", division)  # Imprime el resultado de la división
# División entera
division_entera = a // b
print("División entera:", division_entera)  # Imprime el resultado de la división entera
# Potenciación  
potenciacion = a ** b
print("Potenciación:", potenciacion)  # Imprime el resultado de la potenciación


# Precedencia de operadores
resultado_precedencia = a + b * 2 - 5 / (1 + 1)
print("Resultado con precedencia de operadores:", resultado_precedencia)  # Imprime el resultado considerando la precedencia
# Uso de paréntesis para cambiar la precedencia
resultado_con_parentesis = (a + b) * (2 - 5) / (1 + 1)
print("Resultado con paréntesis:", resultado_con_parentesis)  # Imprime el resultado con paréntesis que alteran la precedencia
print('#' * 50)
# Operadores combinados
a += 5  # Equivalente a a = a + 5
print("Valor de a después de += 5:", a)  # Imprime el nuevo

#Precedencia de operadores
#paréntesis
resultado1 = (3 + 5) * 2
print("Resultado con paréntesis:", resultado1)  # Imprime 16
#exponentes
resultado2 = 3 + 5 ** 2
print("Resultado con exponentes:", resultado2)  # Imprime 28
#multiplicación y división, enteras y flotantes
resultado3 = 10 / 2 * 3
print("Resultado con multiplicación y división:", resultado3)  # Imprime 15.0
#suma y resta
resultado4 = 10 - 3 + 2
print("Resultado con suma y resta:", resultado4)  # Imprime 9
#Comparación de identidad y pertenencia
x = 10
y = 10
print("x es y:", x is y)  # Imprime True porque ambos apuntan al mismo valor
lista1 = [1, 2, 3]
lista2 = lista1
print("lista1 es lista2:", lista1 is lista2)  # Imprime True
print("2 en lista1:", 2 in lista1)  # Imprime True
print("5 no en lista1:", 5 not in lista1)  # Imprime
print('#' * 50)
# Operadores lógicos: and, or, not
a = True
b = False
# Operador and
resultado_and = a and b
print("Resultado de a and b:", resultado_and)  # Imprime False
# Operador or
resultado_or = a or b
print("Resultado de a or b:", resultado_or)  # Imprime True         