# Slicing, replace y split para manipular strings en Python
# INT = 1234567890

Texto = 'Los niños, mis mejores primos que tu sa ¿bes quienes son me hacen mucha fata '
#Posiscion de cada caracter
print(Texto[2:5])
print(Texto[5:])
print(Texto[:10])
print(Texto[:-2])  # Slicing completo: Devuelve todo el
print(Texto[::2])  # Slicing con paso: Devuelve cada segundo caracter
print(Texto[:])    # texto  
print('#' * 50)

#Renplazo de texto
print(Texto.replace('niños', 'amigos'))  # Reemplaza 'niños' por 'amigos' en el texto   
print(Texto.replace('mucha fata', 'mucha falta de ustedes'))  # Reemplaza 'mucha fata' por 'mucha falta de ustedes'
print(Texto.replace('primos', 'hermanos'))  # Reemplaza 'primos' por 'hermanos'
print(Texto.replace('niños', 'Emanuel, Nicolas, Alejandro, Martin, Sebastian, Kevin'))  # 
print(Texto[2:15])  # Slicing: Extrae una porción del texto desde el índice 2 hasta el 15
print(Texto.replace('niños', 'amigos').split())
print('#' * 50)

#Trabajandon con split
print(Texto.split())  # Divide el texto en una lista de palabras usando espacios como separador
print(Texto.split(','))  # Divide el texto en una lista usando la coma como
print(Texto.split('que'))  # Divide el texto en una lista usando 'que' como separador
print(Texto.split(' '))  # Divide el texto en una lista usando espacios como separador
print(Texto.replace('niños', 'amigos').split(' '))  #Reemplaza 'niños' por 'amigos' y luego divide el texto en una lista
print(Texto.replace('mucha fata', 'mucha falta de ustedes').split(' '))  # Reemplaza 'mucha fata' por 'mucha falta de ustedes' y
print('#' * 50)

# Normalizando texto
Texto2 = 'LOS NIÑOS son mis mejores primos QUE TU SABES QUIENES SON ME HACEN MUCHA FATA '
print(Texto2.lower())  # Convierte todo el texto a minúsculas
print(Texto2.upper())  # Convierte todo el texto a mayúsculas
print(Texto2.capitalize())  # Capitaliza la primera letra del texto
print(Texto2.title())  # Capitaliza la primera letra de cada palabra en el texto
print('#' * 50)

Texto_normalizado2 = Texto2.lower().replace('niños', 'amigos').replace('mucha fata', 'mucha falta de ustedes')
print(Texto_normalizado2.split(' '))  # Divide el texto normalizado en una lista usando espacios como separador 
Texto_normalizado = Texto.replace('niños', 'amigos').replace('mucha fata', 'mucha falta de ustedes')
print(Texto_normalizado.split(' '))  # Divide el texto normalizado en una lista usando espacios como separador  
