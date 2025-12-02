# Operadores lógicos OR y NOT con booleanos en Python
a = True
b = False   
# Operador OR
resultado_or = a or b
print("Resultado de a or b:", resultado_or)  # Imprime True
# Otro ejemplo con OR
x = 5
y = 10      
resultado_or_numeros = (x > 3) or (y < 5)
print("Resultado de (x > 3) or (y < 5):", resultado_or_numeros)  # Imprime True
# Operador NOT
resultado_not_a = not a
print("Resultado de not a:", resultado_not_a)  # Imprime False
resultado_not_b = not b
print("Resultado de not b:", resultado_not_b)  # Imprime True
# Otro ejemplo con NOT
z = 0
resultado_not_z = not (z > 0)
print("Resultado de not (z > 0):", resultado_not_z)  # Imprime True 
print('#' * 50)
# Combinación de operadores lógicos
resultado_combinado = (a and b) or (not b)
print("Resultado de (a and b) or (not b):", resultado_combinado)  # Imprime True
resultado_combinado2 = not (a or (x < 3))
print("Resultado de not (a or (x < 3)):", resultado_combinado2)  # Imprime False
print('#' * 50)
# Uso de operadores lógicos en condiciones
edad = 20
tiene_identificacion = True
puede_entrar = (edad >= 18) and tiene_identificacion
print("¿Puede entrar?", puede_entrar)  # Imprime True   
edad2 = 16
tiene_identificacion2 = False
puede_entrar2 = (edad2 >= 18) and tiene_identificacion2
print("¿Puede entrar?", puede_entrar2)  # Imprime False 
print('#' * 50)
# Ejemplo práctico: Validación de acceso
usuario_autenticado = True
tiene_permiso = False
acceso_concedido = usuario_autenticado and (tiene_permiso or not tiene_permiso)
print("¿Acceso concedido?", acceso_concedido)  # Imprime True
print('#' * 50)

# Operadores de comparacion 
x= 10
y= 6
z= 10
print("x == y:", x == y)  # Imprime False
print("x != y:", x != y)  # Imprime True
print("x > y:", x > y)    # Imprime True
print("x < y:", x < y)    # Imprime False
print("x >= z:", x >= z)  # Imprime True
print("y <= z:", y <= z)  # Imprime True

#Operadores logicos AND 
print(x > 5 and y < 10)  # Imprime True
print(x > 5 and y > 10)  # Imprime False    

print('#' * 50)
#Operadores logicos OR
print(x > 5 or y > 10)   # Imprime True
print(x < 5 or y > 10)   # Imprime False    
print('#' * 50)
#Operadores logicos NOT
print(not(x > 5))        # Imprime False
print(not(y > 10))       # Imprime True     

print('#' * 50)
#Ejemplos combinados
print((x > 5 and y < 10) or (x < 5))  # Imprime True
print(not(x > 5 and y < 10))  # Imprime False       

print('#' * 50)
#Operadores de negación
a = True
b = False
print("not a:", not a)  # Imprime False
print("not b:", not b)  # Imprime True