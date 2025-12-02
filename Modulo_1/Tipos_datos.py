# Tipos de datos en Python: strings, números y colecciones
# Strings
cadeconcomillassimples = 'Hola, Mundo!'
cadenaconcomillasdosbles = "Hola, Mundo!"
cadenaconcomillastriples = '''Hola, Mundo!'''
cadenaconcomillastriplesdobles = """Hola, Mundo!"""

print(cadeconcomillassimples)
print(cadenaconcomillasdosbles)
print(cadenaconcomillastriples)
print(cadenaconcomillastriplesdobles)
print(type(cadeconcomillassimples))

# Números
entero = 42
flotante = 3.14159
complejo = 2 + 3j   

print(entero)
print(flotante)
print(complejo)
print(type(entero))
print(type(flotante))
print(type(complejo))

# Colecciones
# Listas
mi_lista = [1, 2, 3, 'cuatro', 'cinco']
print(mi_lista)
print(type(mi_lista))

# Tuplas
mi_tupla = (1, 2, 3, 'cuatro', 'cinco')
print(mi_tupla)
print(type(mi_tupla))   

# Conjuntos
mi_conjunto = {1, 2, 3, 'cuatro', 'cinco'}
print(mi_conjunto)
print(type(mi_conjunto))        

# Diccionarios
mi_diccionario = {'uno': 1, 'dos': 2, 'tres': 3}
print(mi_diccionario)
print(type(mi_diccionario)) 

# Booleanos
verdadero = True
falso = False       
print(verdadero)
print(falso)
print(type(verdadero))
print(type(falso))
