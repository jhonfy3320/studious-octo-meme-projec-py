# Definición y uso de funciones en Python con argumentos y return
def saludar():
    """Función que imprime un saludo genérico."""
    print("¡Hola! Bienvenido a la programación en Python. Estamos aprendiendo python juntos." \
    " Es un lenguaje de programación muy versátil y poderoso.")
saludar()
# Lo grandiosos de las funciones es que nos ayudan a reutilizar código
# Podemos llamar a la función tantas veces como queramos
saludar()
saludar() 
print("-----"*10)   
# Función con argumentos
def saludar_personalizado(nombre):
    """Función que imprime un saludo personalizado."""
    print(f"¡Hola, {nombre}! Bienvenido a la programación en Python.")
saludar_personalizado("Emanuel")
saludar_personalizado("Nicolas")
saludar_personalizado("Alejandro")
# Los argumantos nos permiten pasar información a las funciones, que los llamamos parámetros
print("-----"*10)
# Función con múltiples argumentos
def saludar_completo(nombre, apellido, edad=''):
    """Función que imprime un saludo completo con nombre, apellido y edad."""
    print(f"¡Hola, {nombre} {apellido}! Tienes {edad} años. Bienvenido a la programación en Python.")
saludar_completo("Emanuel", "Ocoro", 15)
saludar_completo("Nicolas", "Ososrio", 14)
saludar_completo("Alejandro", "Vivas", 13)   
saludar_completo('Martin', 'Ocoro')
saludar_completo('Freddy', 'Tavera', 12)
print("-----"*10)
# Función con return
def sumar(a, b):
    """Función que retorna la suma de dos números."""
    return a + b    
resultado = sumar(24, 13)
print(f"La suma de 5 y 3 es: {resultado}")
resultado = sumar(10, 20)
print(f"La suma de 10 y 20 es: {resultado}")
resultado = sumar(-2, 8)
print(f"La suma de -2 y 8 es: {resultado}")

def funtion():
    pass
print("-----"*10)    

# Generar una calculadora básica usando funciones
def sumar(a, b):
    return a + b    
def restar(a, b):
    return a - b    
def multiplicar(a, b):
    return a * b    
def dividir(a, b):
    return a / b

resultado = sumar(10, 5)
print(f"La suma de 10 y 5 es: {resultado}")
resultado = restar(10, 5)
print(f"La resta de 10 y 5 es: {resultado}")
resultado = multiplicar(10, 5)
print(f"La multiplicación de 10 y 5 es: {resultado}")
resultado = dividir(10, 5)
print(f"La división de 10 y 5 es: {resultado}") 
print("-----"*10)
# Calculadora con el metodo Cases
def calculadora(a, b, operacion):
    if operacion == 'sumar':
        return a + b
    elif operacion == 'restar':
        return a - b
    elif operacion == 'multiplicar':
        return a * b
    elif operacion == 'dividir':
        return a / b
    else:
        return "Operación no válida"
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

# Calculadora con el metodo case (match-case)
def calculadora_case(a, b, operacion):
    match operacion:
        case 'sumar':
            return a + b
        case 'restar':
            return a - b
        case 'multiplicar':
            return a * b
        case 'dividir':
            return a / b
        case _:
            return "Operación no válida"
resultado = calculadora_case(30, 15, 'sumar')
print(f"La suma de 30 y 15 es: {resultado}")
resultado = calculadora_case(30, 15, 'restar')
print(f"La resta de 30 y 15 es: {resultado}")
resultado = calculadora_case(30, 15, 'multiplicar')         
print(f"La multiplicación de 30 y 15 es: {resultado}")
resultado = calculadora_case(30, 15, 'dividir')
print(f"La división de 30 y 15 es: {resultado}")
resultado = calculadora_case(30, 15, 'modulo')
print(f"Resultado de operación no válida: {resultado}") 
print("-----"*10)
# Función para calcular el factorial de un número
def factorial(n):   
    """Función que retorna el factorial de un número."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")
numero = 7
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")          
