# Condicionales en Python: if, else, and, or y pass
from calendar import c


x = 23
y = 25
# Condicional if
if x > y:
    print(f"{x} es mayor que {y}")  # Imprime si x es mayor que y

if y > x:
    print(f"{y} es mayor que {x}")  # No se imprime porque la condición es falsa    

# Condicional if-else
if x < y:
    print(f"{x} es menor que {y}")
else:
    print(f"{x} no es menor que {y}")  # Imprime esta línea porque la condición es falsa        
print('#' * 50)

# Condicional if-elif-else
if x < y:
    print(f"{x} es menor que {y}")
elif x == y:
    print(f"{x} es igual a {y}")        
else:
    print(f"{x} es mayor que {y}")  # Imprime esta línea porque ambas condiciones anteriores son falsas
print('#' * 50)

z = 15
# Uso de operadores lógicos and y or en condicionales
if x < y and z < y:
    print(f"{x} es menor que {y} y {z} es menor que {y}")  # Imprime esta línea porque ambas condiciones son verdaderas 
if x > y or z < y:
    print(f"{x} es mayor que {y} o {z} es menor que {y}")  # Imprime esta línea porque una de las condiciones es verdadera

#Comparacion de str
a = "hola"
b = "mundo"
c = "hola"

if a == c:
    print(f'"{a}" es igual a "{c}"')  # Imprime esta línea porque ambas cadenas son iguales
else:
    print(f'"{a}" no es igual a "{c}"') 
if a != b:
    print(f'"{a}" es diferente de "{b}"')  # Imprime esta línea porque las cadenas son diferentes
else:
    print(f'"{a}" no es diferente de "{b}"')
print('#' * 50)

# Trabajando con if anidados
if a == c:
    if b != c:
        print(f'"{a}" es igual a "{c}" y "{b}" es diferente de "{c}"')  # Imprime esta línea porque ambas condiciones son verdaderas
    else:
        print(f'"{b}" no es diferente de "{c}"')
else:
    print(f'"{a}" no es igual a "{c}"') 
print('#' * 50)
# Uso de pass en condicionales
if x > y:
    pass  # No hace nada si la condición es verdadera
else:
    print(f"{x} no es mayor que {y}, se ejecuta el else")  # Imprime esta línea porque la condición es falsa
print('#' * 50)

#Activida d práctica: Determinar si un número es par o impar
numero = 15
if numero % 2 == 0:
    print(f"{numero} es un número par")  # Imprime si el número es par
else:
    print(f"{numero} es un número impar")  # Imprime si el número es impar 
print('#' * 50)
#Actividad práctica: Validar acceso basado en edad y membresía
# Supongamos que un club permite la entrada solo a personas mayores de 18 años que sean miembros.
# Definimos las variables
edad = 20
es_miembro = True   
if edad >= 18 and es_miembro:
    print("Acceso concedido al club")  # Imprime si la persona cumple ambas condiciones
else:
    print("Acceso denegado al club")  # Imprime si alguna de las condiciones no se cumple   
     