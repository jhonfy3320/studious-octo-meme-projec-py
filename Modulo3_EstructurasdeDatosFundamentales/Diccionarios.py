#Diccionarios en Python: pares clave-valor ordenados y anidados
# Crear un diccionario vacío
diccionario_vacio = {}
print("Diccionario vacío:", diccionario_vacio)
# Crear un diccionario con pares clave-valor iniciales
persona = {"nombre": "Emanuel",
           "edad": 15,
           "ciudad": "cartago",
           "ocupacion": "estudiante",
           "hobbies": ["leer", "viajar", "correr"]}

persona2 = {"nombre": "Nicolas",
           "edad": 14,
           "ciudad": "rozo",
           "ocupacion": "estudiante",
           "hobbies": ["dibujo", "música", "fútbol"]}

persona3 = {"nombre": "Alejandro",
           "edad": 13,
           "ciudad": "buga",
           "ocupacion": "estudiante",
           "hobbies": ["videojuegos", "natación", "cine"]} 

persona4 = {"nombre": "Marin",
           "edad": 10,
           "ciudad": "palmira",
           "ocupacion": "estudiante",
           "hobbies": ["fotografía", "ciclismo", "tecnología"]}

persona5 = {"nombre": "Sebastian",
           "edad": 12,
           "ciudad": "tuluá",
           "ocupacion": "estudiante",
           "hobbies": ["ajedrez", "senderismo", "arte"]}

persona6 = {"nombre": "Kevin",
            "edad": 11,
            "ciudad": "buga",
            "ocupacion": "estudiante",
            "hobbies": ["programación", "robótica", "astronomía"]}

persona7 = {"nombre": "Luciana",
            "edad": 14,
            "ciudad": "cartago",
            "ocupacion": "estudiante",
            "hobbies": ["danza", "moda", "cocina"]}

persona8 = {"nombre": "Freddy",
            "edad": 15,
            "ciudad": "rozo",
            "ocupacion": "estudiante, Universitario",
            "hobbies": ["mecánica", "automovilismo", "deportes"]}     

print("Diccionario de persona:", persona) 
print("Diccionario de persona2:", persona2)
print("Diccionario de persona3:", persona3)
print("Diccionario de persona4:", persona4)
print("Diccionario de persona5:", persona5)         
print("Diccionario de persona6:", persona6)
print("Diccionario de persona7:", persona7)
print("Diccionario de persona8:", persona8)
# Acceder a valores mediante claves
print("Nombre de la persona:", persona["nombre"])
print("Edad de la persona:", persona["edad"])
print("Ciudad de la persona:", persona["ciudad"])
print("Ocupación de la persona:", persona["ocupacion"])
print("Hobbies de la persona:", persona["hobbies"])
print(persona2.get("nombre"))
print(persona3.keys())
print(persona4.values())
print('---' * 20)
if "nombre" in persona:
    print("La clave 'nombre' existe en el diccionario persona.")
else:
    print("La clave 'nombre' no existe en el diccionario persona.")
print('---' * 20)
# Verificar la existencia de una clave
if "nombre" in persona8:
    print("La clave 'nombre' existe en el diccionario persona.")
else:
    print("La clave 'nombre' no existe en el diccionario persona.")
print('---' * 20)
# Modificar valores en el diccionario
# Modificar la edad de la persona
persona["edad"] = 14
print("Edad modificada de la persona:", persona["edad"])
# Agregar una nueva clave-valor
persona["email"] = "emanuel15@gmail.com"
print("Diccionario de persona después de agregar email:", persona)
persona5update = {"telefono": "123-456-7890"}
persona5.update(persona5update)
print("Diccionario de persona5 después de agregar teléfono:", persona5)
print('---' * 20)
# Eliminar una clave-valor
persona5.pop('telefono', None)  # Usar pop con default para evitar error si la clave no existe
print("Diccionario de persona5 después de eliminar teléfono:", persona5)
del persona7["ciudad"]
print("Diccionario de persona después de eliminar ciudad:", persona7)
print('---' * 20)
# Iterar sobre un diccionario
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
print('---' * 20)
for clave in persona2.keys():
    print(f"Clave: {clave}")
print('---' * 20)
for valor in persona3.values():
    print(f"Valor: {valor}")
print('---' * 20)
# Longitud del diccionario
print("Número de pares clave-valor en el diccionario persona4:", len(persona4))
print("Número de pares clave-valor en el diccionario persona6:", len(persona6))
print('---' * 20)
# Diccionarios anidados
estudiantes = {
    "estudiante1": persona,
    "estudiante2": persona2,
    "estudiante3": persona3,
    "estudiante4": persona4,        
    "estudiante5": persona5,
    "estudiante6": persona6,
    "estudiante7": persona7,
    "estudiante8": persona8
}
print("Diccionario de estudiantes:", estudiantes)
print("Información del estudiante1:", estudiantes["estudiante1"])
print("Hobbies del estudiante2:", estudiantes["estudiante2"]["hobbies"])
print("Ciudad del estudiante3:", estudiantes["estudiante3"]["ciudad"])
print('---' * 20)   

'''for key, value in estudiantes.items():
    print(f"{key}: {value['nombre']}, Edad: {value['edad']}, Ciudad: {value['ciudad']}")
print('---' * 20)'''

# Nuevo dieccionarios anidados
Carros = {
    "Carro1": {"marca": "Toyota", "modelo": "Corolla", "año": 2020},
    "Carro2": {"marca": "Honda", "modelo": "Civic", "año": 2019},
    "Carro3": {"marca": "Ford", "modelo": "Focus", "año": 2018},
    "Carro4": {"marca": "Chevrolet", "modelo": "Malibu", "año": 2021},
    "Carro5": {"marca": "Nissan", "modelo": "Sentra", "año": 2017},
    "Carro6": {"marca": "Hyundai", "modelo": "Elantra", "año": 2022},
    "Carro7": {"marca": "Kia", "modelo": "Forte", "año": 2016},
    "Carro8": {"marca": "Volkswagen", "modelo": "Jetta", "año": 2023}
}
print("Diccionario de Carros:", Carros)
print("Información del Carro1:", Carros["Carro1"])
print("Modelo del Carro2:", Carros["Carro2"]["modelo"])
print("Año del Carro3:", Carros["Carro3"]["año"])
print('---' * 20)
for key, value in Carros.items():
    print(f"{key}: {value['marca']}, Modelo: {value['modelo']}, Año: {value['año']}")
print('---' * 20)
# Los diccionarios tambien son conocidos como objectos directos 
# 
