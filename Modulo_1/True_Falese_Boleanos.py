#Booleanos en Python: True, False y casting a bool
# Definición de valores booleanos
valor_verdadero = True
valor_falso = False     
print("Valor Verdadero:", valor_verdadero)  # Imprime el valor True
print("Valor Falso:", valor_falso)          # Imprime el valor False
print(type(valor_verdadero))  # Muestra el tipo de dato: bool
print(type(valor_falso))      # Muestra el tipo de dato: bool   
print(bool('Hola atosdos Emanuel, Nicolas, Alejandro, Martin, Sebastian, Kevin'))  # Convierte una cadena no vacía a True
print(bool(''))  # Convierte una cadena vacía a False
print(bool(12345))  # Convierte un número distinto de cero a True
print(bool(0))      # Convierte el número cero a False
print(bool([1, 2, 3]))  # Convierte una lista no vacía a True
print(bool([]))         # Convierte una lista vacía a False
print(bool({'clave': 'valor'}))  # Convierte un diccionario no vacío a True
print(bool({}))                # Convierte un diccionario vacío a False 
print('#' * 50)

#Enteros y flotantes a booleanos
print(bool(1))      # Convierte el entero 1 a True
print(bool(0))      # Convierte el entero 0 a False
print(bool(-1))     # Convierte el entero -1 a True
print(bool(0.0))    # Convierte el flotante 0.0 a False
print(bool(0.1))    # Convierte el flotante 0.1 a True
print(bool(-0.1))   # Convierte el flotante -0.1 a True
print('#' * 50)     

#Listas, tuplas y conjuntos a booleanos
print(bool([1, 2, 3]))  # Convierte una lista no vacía a True
print(bool([]))         # Convierte una lista vacía a False
print(bool((1, 2)))    # Convierte una tupla no vacía a True
print(bool(()))        # Convierte una tupla vacía a False
print(bool({1, 2, 3}))  # Convierte un conjunto no vacío a True
print(bool(set()))     # Convierte un conjunto vacío a False
print('#' * 50) 

#Enteros 
x = 1234567890.3
print(isinstance(x, int))  # Verifica si x es un entero
y = 123456
print(isinstance(y, float))  # Verifica si y es un flotante
z = "Hola, mundo!"
print(isinstance(z, str))    # Verifica si z es una cadena de texto
print('#' * 50) 