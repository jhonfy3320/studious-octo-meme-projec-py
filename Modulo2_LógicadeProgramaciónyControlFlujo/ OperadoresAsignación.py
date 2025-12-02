# Operadores de asignación y walrus en Python
# Operadores de asignación combinados
x = 10
print("Valor inicial de x:", x)  # Imprime el valor inicial de x
x += 5  # Equivalente a x = x + 5
print("Valor de x después de += 5:", x)  # Imprime el nuevo valor de x
x -= 3  # Equivalente a x = x - 3
print("Valor de x después de -= 3:", x)  # Imprime el nuevo valor de x
x *= 2  # Equivalente a x = x * 2
print("Valor de x después de *= 2:", x)  # Imprime el nuevo valor de x
x /= 4  # Equivalente a x = x / 4
print("Valor de x después de /= 4:", x)  # Imprime el nuevo valor de x
x %= 3  # Equivalente a x = x % 3
print("Valor de x después de %= 3:", x)  # Imprime el nuevo valor de x
x **= 2  # Equivalente a x = x ** 2
print("Valor de x después de **= 2:", x)  # Imprime el nuevo valor de x
x //= 2  # Equivalente a x = x // 2
print("Valor de x después de //= 2:", x)  # Imprime el nuevo valor de x 
print('#' * 50)

y = 20

y //= 4  # Equivalente a y = y // 4
print("Valor de y después de //= 4:", y)  # Imprime el nuevo valor de y
y **= 3  # Equivalente a y = y ** 3
print("Valor de y después de **= 3:", y)  # Imprime el nuevo valor de y
print('#' * 50)



print('Operador walrus (Morasa, en expresiones)')
# Ejemplo 1: Usando el operador walrus en una condición if
if (n := 10) > 5:
    print("n es mayor que 5:", n)  # Imprime el valor de n  
print('#' * 50)
# Ejemplo 2: Usando el operador walrus en un bucle while
count = 0
while (count := count + 1) < 5:
    print("Count es:", count)  # Imprime el valor de count en cada iteración
print('#' * 50)
# Ejemplo 3: Usando el operador walrus en una comprensión de listas
numeros = [1, 2, 3, 4, 5]
cuadrados = [ (cuadrado := x ** 2) for x in numeros if cuadrado > 10]  # noqa: F821
print("Cuadrados mayores que 10:", cuadrados)  # Imprime los cuadrados mayores que 10
print('#' * 50)



