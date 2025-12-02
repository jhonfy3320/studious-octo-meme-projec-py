try:
    with open('historia_primos2.txt', 'r', encoding='utf-8') as f:
        print(f.readline())
        print(f.readline())
except FileNotFoundError:
    open('historia_primos2.txt', 'x')
    print('No se a encontrado el archivo')
    
print('-----'* 20)
try:
    with open('historia_primos.txt', 'a') as f:
        f.write('\n')
        f.write('Emanuel como es el lider, hace lo que quiera con freddy, freddy es su esclsvo')
    with open('historia_primos.txt', 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print('No se a encontrado el archivo ')