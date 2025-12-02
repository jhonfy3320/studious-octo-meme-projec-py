# Conjuntos en Python: creación, métodos y operaciones básicas
# Crear un conjunto vacío
from tkinter import N


conjunto_vacio = set()
print("Conjunto vacío:", conjunto_vacio)
# Crear un conjunto con elementos iniciales
frutas = {"manzana", "banana", "cereza", "durazno", "frutilla", "kiwi", "mango", "naranja"}
print("Conjunto de frutas:", frutas)
# Agregar un elemento al conjunto
frutas.add("piña")
print("Conjunto de frutas después de agregar piña:", frutas)
# Elementos duplicados no se permiten en conjuntos
frutas.add("manzana")
print("Conjunto de frutas después de intentar agregar manzana nuevamente:", frutas)
# Eliminar un elemento del conjunto
frutas.remove("kiwi")
print("Conjunto de frutas después de eliminar kiwi:", frutas)
print(len(frutas))
print('---' * 20)

# Diferentes tipos de datos en un conjunto
conjunto_mixto = {42, "Hola", 3.14, True, None, (1, 2, 3), frozenset({"clave": "valor"}),
                   complex(2, 3),'Emanuel', 'Nicolas', 'Alejandro', 'Marin', 'Sebastian', 'Kevin', 'Luciana', 'Freddy'}
print("Conjunto mixto:", conjunto_mixto)
print(type(conjunto_mixto))
print(len(conjunto_mixto))
print('---' * 20)
# Iterando sobre un conjunto
for elemento in conjunto_mixto:
    print(elemento)
# Cuando iteramos sobre un conjunto, el orden de los elementos no está garantizado
# Por lo tanto, el orden de impresión puede variar en cada ejecución
# Otro datos a tener en cuemnta es que los conjuntos no son indexados, por lo que no podemos acceder a elementos por índice
print('---' * 20)
# Un elemento esta o no en el conjunto
print("¿Está 'Emanuel' en el conjunto mixto?", 'Emanuel' in conjunto_mixto)
print("¿Está 'Carlos' en el conjunto mixto?", 'Carlos' in conjunto_mixto)
if "Nicolas" in conjunto_mixto:
    print("Nicolas está en el conjunto mixto.")
if "Carlos" not in conjunto_mixto:
    print("Carlos no está en el conjunto mixto.")
print('---' * 20)
#Agregar varios elementos a un conjunto usando update
tupla_nombres = ('Emanuel', 'Nicolas', 'Alejandro', 'Marin', 'Sebastian', 'Kevin', 'Luciana', 'Freddy')
conjunto_nombres = set()
conjunto_nombres.update(tupla_nombres)
print("Conjunto de nombres después de update:", conjunto_nombres)
print('---' * 20)   
#Agregar un nuevo elemento al conjunto de nombres
conjunto_nombres.add('Camilo')
print("Conjunto de nombres después de agregar Carlos:", conjunto_nombres)
print('---' * 20)
#Eliminar un elemento del conjunto de nombres
conjunto_nombres.remove('Camilo')
print("Conjunto de nombres después de eliminar Camilo:", conjunto_nombres)
conjunto_nombres.discard('Carlos')  # Usar discard para evitar error si el elemento no existe
print("Conjunto de nombres después de descartar Camilo nuevamente:", conjunto_nombres)
conjunto_mixto.pop()  # Elimina un elemento arbitrario
print("Conjunto mixto después de pop:", conjunto_mixto) 
Nuvo_conjunto = conjunto_nombres.copy()
print("Copia del conjunto de nombres:", Nuvo_conjunto)  
Nuvo_conjunto.clear()
print("Copia del conjunto de nombres después de clear:", Nuvo_conjunto) 
print('---' * 20)
# Operaciones con conjuntos
A = {1, 2, 3, 4, 5, 'a', 'b', 'c', 'Emanuel', 'Nicolas', 'Alejandro','Freddy'}
B = {4, 5, 6, 7, 8, 'c', 'd', 'e', 'Marin', 'Sebastian', 'Kevin', 'Luciana','Freddy'}
# Unión
union = A.union(B)
print("Unión de A y B:", union)
# Intersección
interseccion = A.intersection(B)
print("Intersección de A y B:", interseccion)
# Diferencia
diferencia = A.difference(B)
print("Diferencia de A y B (A - B):", diferencia)
# Diferencia simétrica
diferencia_simetrica = A.symmetric_difference(B)
print("Diferencia simétrica de A y B:", diferencia_simetrica)
# Verificar subconjunto
subconjunto = {1, 2, 'a'}
es_subconjunto = subconjunto.issubset(A)
print("¿El conjunto {1, 2, 'a'} es subconjunto de A?", es_subconjunto)
# Verificar superconjunto
es_superconjunto = A.issuperset(subconjunto)
print("¿El conjunto A es superconjunto de {1, 2, 'a'}?", es_superconjunto)
# Verificar disjuntos
conjunto_disjunto = {10, 11, 12}
son_disjuntos = A.isdisjoint(conjunto_disjunto)
print("¿A y {10, 11, 12} son disjuntos?", son_disjuntos)    