# Listas en Python: creación, modificación y métodos esenciales
# Crear una lista vacía
mi_lista = []
print("Lista vacía:", mi_lista) 
# Crear una lista con elementos iniciales
frutas = ["manzana", "banana", "cereza"]
print("Lista de frutas:", frutas) 
# Acceder a elementos por índice
primera_fruta = frutas[0]
print("Primera fruta:", primera_fruta) 
# Modificar un elemento de la lista
frutas[1] = "naranja"
print("Lista de frutas después de la modificación:", frutas) 
# Agregar un elemento al final de la lista
frutas.append("durazno")
print("Lista de frutas después de agregar un elemento:", frutas) 
# Insertar un elemento en una posición específica
frutas.insert(1, "kiwi")
print("Lista de frutas después de insertar un elemento:", frutas)

Carros = ["Ford", "Chevrolet", "Toyota", "Honda," "BMW", "Audi", "Mercedes", "Volkswagen", "Nissan", "Hyundai", "Kia"]
print(Carros)
Carros[2] = "Tesla"
print(Carros)
print("Cantidad de carros en la lista:", len(Carros))
print("Carros ordenados alfabéticamente:", sorted(Carros))
print(Carros[2])
Carros.append("Hyundai")
print(Carros)
print(type(Carros))
print('---' * 20)

# Mezclado valores de diferentes tipos de datos en una lista
lista_mixta = [42, "Hola", 3.14, True, None, [1, 2, 3], {"clave": "valor"}, (4, 5),
                complex(2, 3),'Emanuel', 'Nicolas', 'Alejandro', 'Marin', 'Sebastian', 'Kevin', 'Luciana', 'Freddy']
print("Lista mixta:", lista_mixta)
print(type(lista_mixta))
#aacesar al elemento 'Marin' dentro de la lista_mixta
print(lista_mixta[11])
print(lista_mixta[14])
print(lista_mixta[3])
print(lista_mixta[8])
print(len(lista_mixta))
print(lista_mixta[2:14])
if 'Nicolas' in lista_mixta:
    print("Nicolas está en la lista mixta.")
if 'Emanuel' in lista_mixta:
    print("Emanuel está en la lista mixta.")
if 'Freddy' in lista_mixta:
    print("Freddy está en la lista mixta.")
if 'Carlos' not in lista_mixta:
    print("Carlos no está en la lista mixta.")
#Agreagar nuevos elementos a la lista_mixta
lista_mixta.append("Diversion")
lista_mixta.append('Juntos')
lista_mixta.append(2025)
lista_mixta.insert(8, '8-15')
print(lista_mixta)
#Eliminar un elemento de la lista_mixta
lista_mixta.remove(None)
lista_mixta.pop(0)  # Elimina el primer elemento
print(lista_mixta)
lista_mixta.sort(key=str)  # Ordena la lista convirtiendo todos los elementos a cadenas
#lista_mixta.sort()  # Ordena la lista (puede generar error si hay tipos no comparables)
lista_mixta.reverse()  # Invierte el orden de la lista
print('---' * 20)
#unir dos listas
Super_lista = frutas + Carros
print("Super lista:", Super_lista)
print("Cantidad de elementos en la super lista:", len(Super_lista))
print('---' * 20)
mega_lista3 = lista_mixta + Super_lista
print("Mega lista 3:", mega_lista3)
print("Cantidad de elementos en la mega lista 3:", len(mega_lista3))

