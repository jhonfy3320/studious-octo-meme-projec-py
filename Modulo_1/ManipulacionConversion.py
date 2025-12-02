# Manipulación y conversión de tipos numéricos en Python
# Conversión entre tipos: int, float, complex

# Conversión de entero a flotante
entero = 10
flotante = float(entero)
print("Entero:", entero, "-> Flotante:", flotante, "Tipo:", type(flotante))

# Conversión de flotante a entero
flotante2 = 9.88
entero2 = int(flotante2)
print("Flotante:", flotante2, "-> Entero:", entero2,    "Tipo:", type(entero2))

# Conversión de entero a complejo
entero3 = 5
complejo = complex(entero3)
print("Entero:", entero3, "-> Complejo:", complejo, "Tipo:", type(complejo))    
# Conversión de flotante a complejo
flotante3 = 3.14
complejo2 = complex(flotante3)          
print("Flotante:", flotante3, "-> Complejo:", complejo2, "Tipo:", type(complejo2))

import cmath
import math
import random

print("Número aleatorio entre 1 y 100:", random.randint(1, 100))
