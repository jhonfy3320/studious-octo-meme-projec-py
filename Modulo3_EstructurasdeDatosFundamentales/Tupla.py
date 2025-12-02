# Tuplas en Python: ordenadas, inmutables y con duplicados permitidos
# Crear una tupla vacía
mi_tupla = ()
print("Tupla vacía:", mi_tupla) 
# Crear una tupla con elementos iniciales
frutas = ("manzana", "banana", "cereza", "manzana", "durazno", "banana", "frutilla", "kiwi", "mango", "naranja")
print("Tupla de frutas:", frutas) 
# Acceder a elementos por índice
primera_fruta = frutas[0]
print("Primera fruta:", primera_fruta) 
# Contar la cantidad de veces que aparece un elemento
cantidad_bananas = frutas.count("banana")
print("Cantidad de bananas en la tupla:", cantidad_bananas) 
# Encontrar el índice de la primera aparición de un elemento
indice_cereza = frutas.index("cereza")
print("Índice de la primera cereza en la tupla:", indice_cereza) 
# Tuplas pueden contener elementos de diferentes tipos de datos
tupla_mixta = (42, "Hola", 3.14, True, None, [1, 2, 3], {"clave": "valor"}, (4, 5),
                complex(2, 3),'Emanuel', 'Nicolas', 'Alejandro', 'Marin', 'Sebastian', 'Kevin', 'Luciana', 'Freddy')
print("Tupla mixta:", tupla_mixta)
# Porque agregar complex, lista y diccionario en una tupla  
#porque es inmutable no se pueden agregar o eliminar elementos de la tupla a que se debe esto, pero se pueden modificar los elementos mutables dentro de la tupla como la lista y el diccionario
print(type(tupla_mixta))
print(len(tupla_mixta))
print('---' * 20)

Carros = ('Lamborghini', 'Ferrari', 'Porsche', 'McLaren', 'Bugatti', 'Aston Martin', 'Maserati', 'Rolls-Royce', 'Bentley', 'Pagani', 'Koenigsegg')
print(Carros)
print(Carros[3])
print("Cantidad de carros en la tupla:", len(Carros))
print("Carros ordenados alfabéticamente:", sorted(Carros))
print(type(Carros))
print('---' * 20)

# Cuando solo tenemos un elemento en la tupla, debemos incluir una coma al final    
Crarro = ('Dogge Charger',)
print(type(Crarro))
print(Crarro)
print('---' * 20)

# Desempaquetado de tuplas
# Que es desempaquetado de tuplas, es asignar los valores de una tupla a variables individuales
tupla_colores = ("rojo", "verde", "azul")
color1, color2, color3 = tupla_colores
print("Color 1:", color1)
print("Color 2:", color2)
print("Color 3:", color3)
print('---' * 20)

#Desempaquetando tupla_mixta
(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q) = tupla_mixta  # noqa: E741
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)        
print(i)
print(j)        
print(k)
print(l)
print(m)
print(n)
print(o)
print(p)
print(q)    
print('---'* 20)

# Duplicando tuplas 
print('tupla_mixta original:', tupla_mixta)
tupla_duplicada = tupla_mixta * 2
print('tupla_mixta duplicada:', tupla_duplicada)    
print('---' * 20)

# Concatenando tuplas
super_tupla = tupla_mixta + Carros
print('Tupla concatenada:', super_tupla)
print('---' * 20)
# Convertir una lista en una tupla
tupla_mixta_desde_lista = tuple(['Emanuel', 'Nicolas', 'Alejandro', 'Marin', 'Sebastian', 'Kevin', 'Luciana', 'Freddy'])
print('Tupla desde lista:', tupla_mixta_desde_lista)
print('---' * 20)   
# Convertir una tupla en una lista
lista_desde_tupla = list(tupla_mixta_desde_lista)
print('Lista desde tupla:', lista_desde_tupla)
print('---' * 20)
# Iterar sobre una tupla e imprimir cada elemento
for tupla in tupla_mixta_desde_lista:
    print(tupla)    
print('---' * 20)

# Modificar tuplas 
# Aunque las tuplas son inmutables, podemos convertirlas en listas para modificarlas y luego volver a convertirlas en tuplas
Carros_lista = list(Carros)
Carros_lista.append('Tesla')
Carros_modificados = tuple(Carros_lista)
print('Tupla de carros modificada:', Carros_modificados)    
