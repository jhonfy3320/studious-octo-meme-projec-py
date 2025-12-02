#Tipo de dato None en Python
# Definición de una variable con valor None 
# que es None es la ausencia de valor o un valor nulo
variable_none = None
print("Valor de la variable:", variable_none)  # Imprime el valor None
print("Tipo de dato:", type(variable_none))     # Muestra el tipo de dato: NoneType
print('#' * 50) 
# Uso de None en funciones
def funcion_sin_retorno():
    print("Esta función no retorna ningún valor")   
resultado = funcion_sin_retorno()  # Llamada a la función
print("Resultado de la función:", resultado)  # Imprime None ya que la función no retorna nada
print("Tipo de dato del resultado:", type(resultado))  # Muestra el tipo de dato: NoneType
print('#' * 50)
# Comparación con None      
otra_variable = 10
if otra_variable is None:   
    print("La variable es None")
else:
    print("La variable no es None, su valor es:", otra_variable)
print('#' * 50)
# Uso de None como valor predeterminado en funciones
def funcion_con_valor_predeterminado(parametro=None):
    if parametro is None:
        print("No se proporcionó ningún valor, usando valor predeterminado")
    else:
        print("El valor proporcionado es:", parametro)      