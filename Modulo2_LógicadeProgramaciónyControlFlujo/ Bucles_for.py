# Bucles for en Python: recorrido de secuencias y listas
# Recorrer una lista de números e imprimir su cuadrados
numeros = [1, 2, 3, 4, 5,6,7,8,9,10]
for numero in numeros:
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es {cuadrado}") 
# Recorrer una cadena de texto e imprimir cada carácter en mayúsculas
texto = "hola a todos mis queridos amigos, bienvenidos a la programación en Python, Emanuel, Nicolas, Alejandro, Marin, Sebastian, Kevin, luciana" 
for caracter in texto:
    print(caracter.upper())
# Recorrer un rango de números e imprimir solo los pares
for i in range(1, 21):
    if i % 2 == 0:
        print(f"{i} es un número par.")

# Recorrer una lista de frutas e imprimir un mensaje personalizado
frutas = ["manzana", "banana", "cereza", "durazno", "frutilla", "kiwi", "mango", "naranja"]
for fruta in frutas:
    print(f"Me gusta comer {fruta}s frescas.")      

# Recorrer una lista de nombres e imprimir un saludo personalizado
nombres = ['Emanuel', 'Nicolas', 'Alejandro', 'Marin', 'Sebastian', 'Kevin', 'Luciana', 'Freddy']
for nombre in nombres:
    print(f"Hola, {nombre}! ¿Cómo estás hoy?")  

# Recorrer una lista de ciudades e imprimir su longitud
ciudades = ["Buenos Aires", "Córdoba", "Rosario", "Mendoza", "La Plata", "Mar del Plata"]
for ciudad in ciudades:
    print(f"La ciudad de {ciudad} tiene {len(ciudad)} caracteres.") 
print('---' * 20)

Frutas = ["manzana", "banana", "cereza", "durazno", "frutilla", "kiwi", "mango", "naranja"]
for fruta in Frutas:
    if Frutas == "kiwi":
        continue
    print(Frutas)
else:
    print("He terminado de recorrer la lista de frutas.")
print('---' * 20)
for i in range(1, 100):
    if i == 50:
        print("He llegado a 50, saliendo del bucle.")
        break
    print(i)

print('---' * 20)
for i in range(0,111,2):
    print(i)
print('---' * 20)

Adjectivos = ['Rica', 'Saludable', 'Dulce_sabor']
Frutas = ["manzana", "banana", "cereza", "durazno", "frutilla", "kiwi", "mango", "naranja"]
for Adjectivo in Adjectivos:
    for Fruta in Frutas:
        print(f"La {Fruta} es muy {Adjectivo}.")
print('---' * 20)

#obtener una inateracion deon de salga manzana rica, manzana saludable, manzana dulce_sabor y luego pase a la siguiente fruta
Adjectivos = ['Rica', 'Saludable', 'Dulce_sabor']
Frutas = ["manzana", "banana", "cereza", "durazno", "frutilla", "kiwi", "mango", "naranja"]
for Fruta in Frutas:
    for Adjectivo in Adjectivos:
        print(f"La {Fruta} es muy {Adjectivo}.")
print('---' * 20)