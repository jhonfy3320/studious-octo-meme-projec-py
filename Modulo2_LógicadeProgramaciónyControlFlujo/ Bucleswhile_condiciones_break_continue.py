# Bucles while en Python: condiciones, break y continue
contador = 100
while contador > 0:
    print(f"Contador actual: {contador}")
    
    # Si el contador es múltiplo de 15, salimos del bucle
    if contador % 15 == 0:
        print("Contador es múltiplo de 15, saliendo del bucle.")
        break
    
    # Si el contador es múltiplo de 10, saltamos esta iteración
    if contador % 10 == 0:
        print("Contador es múltiplo de 10, saltando esta iteración.")
        contador -= 1
        continue
    
    contador -= 1   

E = 2
while E <= 100:
    print(f"E actual: {E}")
    E += 2  
    if E == 50:
        print("E ha alcanzado 50, saliendo del bucle.")
        break

i = 0
while i < 20:
    i += 1
    if i % 3 == 0:
        print(f"{i} es múltiplo de 3, saltando esta iteración.")
        continue
    print(f"Valor de i: {i}")
print('---' * 20)
i = 0
while i < 20:
    i += 1
    if i == 11:
        continue
    print(f"Valor de i: {i}")
else:
    print("i ha alcanzado el valor de 20, finalizando el bucle.")