# Manejo de comillas, múltiples líneas y búsqueda en strings de Python

# Strings con diferentes tipos de comillas
string_simples = 'Este es un string con comillas simples'
string_dobles = "Este es un string con comillas dobles"
string_triples_simples = '''Este es un string con comillas triples simples.
Puede abarcar múltiples líneas.'''
string_triples_dobles = """Este es un string con comillas triples dobles.
También puede abarcar múltiples líneas."""  
print(string_simples)
print(string_dobles)        
print(string_triples_simples)
print(string_triples_dobles)

# Salto de línea en strings
print("""Primera línea
Segunda línea
Tercera línea
y muchas
      otras lineas """    )

#Metodo de búsqueda en strings
texto = "En un lugar de La Mancha, de cuyo nombre no quiero acordarme..."
palabra_a_buscar = "Mancha" 
indice = texto.find(palabra_a_buscar)
if indice != -1:
    print(f'La palabra "{palabra_a_buscar}" fue encontrada en el índice {indice}.')
else:
    print(f'La palabra "{palabra_a_buscar}" no fue encontrada en el texto.')

# Búsqueda de una subcadena que no existe
palabra_a_buscar2 = "Python"
indice2 = texto.find(palabra_a_buscar2)
if indice2 != -1:
    print(f'La palabra "{palabra_a_buscar2}" fue encontrada en el índice {indice2}.')
else:
    print(f'La palabra "{palabra_a_buscar2}" no fue encontrada en el texto.')   

#Metodod len para obtener la longitud de un string
longitud_texto = len(texto)
print(f'La longitud del texto es de {longitud_texto} caracteres.')

# Uso de comillas dentro de strings
string_con_comillas = 'Ella dijo: "Hola, ¿cómo estás?" y él respondió:\'Estoy bien, gracias.\''
texto2 = 'Hola niños como se encuentra "el día" hoy?, dijo freddy a sus amigos, y ellos respondieron: \'muy bien, gracias por preguntar.\', sus mejores ' \
'amigos son: "emanuel", "nicolas", "sebastian", "martin", "alejandro", "kevin".'
print(len(texto2))
print(len(string_con_comillas))  

#Busque la palabra "freddy" en el texto2
indice3 = texto2.find("freddy")
if indice3 != -1:
    print(f'La palabra "freddy" fue encontrada en el índice {indice3}.')
else:
    print(f'La palabra "freddy" no fue encontrada en el texto.')

#Busque la palabra "emanuel" en el texto2
indice4 = texto2.find("emanuel")
if indice4 != -1:
    print(f'La palabra "emanuel" fue encontrada en el índice {indice4}.')
else:
    print(f'La palabra "emanuel" no fue encontrada en el texto.')   

#Busqueda de palabras que no existen en el texto2
indice5 = texto2.find("juan")
if indice5 != -1:
    print(f'La palabra "juan" fue encontrada en el índice {indice5}.')      
else:
    print(f'La palabra "juan" no fue encontrada en el texto.')  
indice6 = texto2.find("dia")
if indice6 != -1:
    print(f'La palabra "dia" fue encontrada en el índice {indice6}.')      
else:
    print(f'La palabra "dia" no fue encontrada en el texto.')
indice7 = texto2.find("amigos")
if indice7 != -1:
    print(f'La palabra "amigos" fue encontrada en el índice {indice7}.')      
else:
    print(f'La palabra "amigos" no fue encontrada en el texto.')

#Mayusculas y minusculas en la busqueda
indice8 = texto2.find("Freddy")
if indice8 != -1:
    print(f'La palabra "Freddy" fue encontrada en el índice {indice8}.')      
else:
    print(f'La palabra "Freddy" no fue encontrada en el texto.')    

#Pasar texto de minusculas a mayusculas y de mayusculas a minusculas
texto_mayusculas = texto2.upper()
print(texto_mayusculas)
texto_minusculas = texto2.lower()
print(texto_minusculas) 

#Buscar espacios en blanco al inicio y al final de un string
texto_con_espacios = "   Hola, este es un texto con espacios en blanco al inicio y al final.    "
print("Texto original:", repr(texto_con_espacios))
texto_sin_espacios = texto_con_espacios.strip()
print("Texto sin espacios:", repr(texto_sin_espacios))      