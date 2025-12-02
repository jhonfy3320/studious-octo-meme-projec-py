# Funciones lambda y fábrica de funciones en Python
# Una función lambda es una función pequeña y anónima que se define utilizando la palabra clave 'lambda'.
# Se utiliza para crear funciones simples y de una sola línea sin necesidad de definir una función completa
# con 'def'. Las funciones lambda son útiles cuando se necesitan funciones rápidas y temporales,
# especialmente como argumentos para otras funciones.
# Sintaxis básica de una función lambda:
# lambda argumentos: expresión
# Ejemplo 1: Función lambda que suma dos números
suma = lambda a, b: a + b
resultado = suma(5, 3)
print(f"La suma de 5 y 3 es: {resultado}")
print("-----"*10)
# Ejemplo 2: Función lambda que verifica si un número es par
es_par = lambda x: x % 2 == 0
numero = 3
if es_par(numero):
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")
print("-----"*10)
# Ejemplo 3: Función lambda para ordenar una lista de tuplas por el segundo elemento
lista_tuplas = [(1, 'b'), (2, 'a'), (3, 'c')]
lista_ordenada = sorted(lista_tuplas, key=lambda x: x[1])
print(f"Lista ordenada por el segundo elemento: {lista_ordenada}")
print("-----"*10)
# Fábrica de funciones: Función que devuelve otras funciones
def crear_operacion(operacion):
    match operacion:
        case 'sumar':
            return lambda a, b: a + b  
        case 'restar':
            return lambda a, b: a - b  
        case 'multiplicar':
            return lambda a, b: a * b  
        case 'dividir':     
            return lambda a, b: a / b  
        case _:
            return lambda a, b: "Operación no válida"   
# Uso de la fábrica de funciones
operacion_sumar = crear_operacion('sumar')
resultado = operacion_sumar(10, 5)
print(f"La suma de 10 y 5 es: {resultado}")
operacion_restar = crear_operacion('restar')
resultado = operacion_restar(10, 5)
print(f"La resta de 10 y 5 es: {resultado}")
operacion_multiplicar = crear_operacion('multiplicar')
resultado = operacion_multiplicar(10, 5)
print(f"La multiplicación de 10 y 5 es: {resultado}")
operacion_dividir = crear_operacion('dividir')
resultado = operacion_dividir(10, 5)
print(f"La división de 10 y 5 es: {resultado}")
operacion_invalida = crear_operacion('potenciar')
resultado = operacion_invalida(10, 5)
print(f"Resultado de operación no válida: {resultado}")
def calculadora(a, b, operacion):
    operacion_func = crear_operacion(operacion)
    return operacion_func(a, b)
resultado = calculadora(20, 10, 'sumar')
print(f"La suma de 20 y 10 es: {resultado}")
resultado = calculadora(20, 10, 'restar')
print(f"La resta de 20 y 10 es: {resultado}")
resultado = calculadora(20, 10, 'multiplicar')      
print(f"La multiplicación de 20 y 10 es: {resultado}")
resultado = calculadora(20, 10, 'dividir')
print(f"La división de 20 y 10 es: {resultado}")
resultado = calculadora(20, 10, 'potenciar')
print(f"Resultado de operación no válida: {resultado}")
print("-----"*10)

def mi_funtion(n):
    return lambda a: a * n

duplicar = mi_funtion(4)
triplicar = mi_funtion(6) 
cuatriplar = mi_funtion(8)
quintiplicar = mi_funtion(10)      

print(duplicar(10)) 
print(triplicar(15))  
print(cuatriplar(20))  
print(quintiplicar(25))  
print("-----"*10)