# Manejo de errores con try, except y finally en Python 
try:
    numero = 10/0
except ZeroDivisionError:
    print('No se puede dividir por cero')


#x = 'Emanuel, Nicolas, Alejandro, Freddy'
try:
    print(x)
except NameError:
    print('esta variable no ha sido definida')
finally:
    print('Esta sera ejecutado siendo exitoso o no el bleque')

try:
    archivo = open('datos.csv', 'r')
    contenido = archivo.read()
except FileNotFoundError:
    print('El archivo no exixste. Verifica el nombre o la ruta')
finally:
    print('Intento de lectura finalizado')

try:
    edad = int(input('Ingresa tu edad: '))
except ValueError:
    print('Debe infresar un numero entero. ')
finally:
    print('Entrada Prosesada. ')

import pandas as pd

try:
    df = pd.read_csv("https://example.com/datos.csv")
except pd.errors.EmptyDataError:
    print("❌ El archivo está vacío.")
except pd.errors.ParserError:
    print("❌ El archivo no tiene formato CSV válido.")
except Exception as e:
    print(f"❌ Error inesperado: {e}")
finally:
    print("Intento de carga completado.")