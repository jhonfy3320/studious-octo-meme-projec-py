# Lectura y escritura de archivos de texto en Python
# open(Nombre, Modo)
# R (READ) Lectura
# W (WRITE) Escribir 
# X (Crear archivo nuevo)

try:    
    f = open('Archivo.txt', 'r')
    print(f.readline())
    f.close()
except FileNotFoundError:
    print('No se ha encontrado el archivo')

try:
    with open('historia_primos.txt', 'r', encoding='utf-8') as f:
        print(f.readline())
        print(f.readline())
        print(f.readline())
        print(f.readline())
        print(f.readline())
except FileNotFoundError:
    print('No se a encontrado el archivo ')

print('-----'* 20)
try:
    with open('resumen_curso.txt', 'r', encoding='utf-8') as f:
        print(f.readline())
        print(f.readline())
        print(f.readline())
        print(f.readline())
        print(f.readline())
except FileNotFoundError:
    print('No se a encontrado el archivo ')

print('-----'* 20)
try:
    with open('historia_primos.txt', 'a') as f:
        f.write('\n')
        f.write('Emanuel como es el lider, hace lo que quiera con freddy, freddy es su esclsvo')
    with open('historia_primos.txt', 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print('No se a encontrado el archivo ')