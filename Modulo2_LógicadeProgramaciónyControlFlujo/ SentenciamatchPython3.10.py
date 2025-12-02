# Sentencia match en Python 3.10 para control de flujo
def evaluar_dia(dia):
    match dia:
        case "lunes":
            return "Inicio de la semana laboral."
        case "martes":
            return "Segundo día de la semana."
        case "miércoles":
            return "Mitad de la semana."
        case "jueves":
            return "Casi es viernes."
        case "viernes":
            return "Último día laboral de la semana."
        case "sábado" | "domingo":
            return "Es fin de semana, disfruta!"
        case _:
            return "Día no válido."
# Ejemplo de uso
dia = "miércoles"
resultado = evaluar_dia(dia)
print(f"El día {dia} indica: {resultado}")  

# Sentencia match en Python 3.10 para control de flujo
def evaluar_dia(martes):
    match martes:
        case "lunes":
            return "Inicio de la semana laboral."
        case "martes":
            return "Segundo día de la semana."
        case "miércoles":
            return "Mitad de la semana."
        case "jueves":
            return "Casi es viernes."
        case "viernes":
            return "Último día laboral de la semana."
        case "sábado" | "domingo":
            return "Es fin de semana, disfruta!"
        case _:
            return "Día no válido."
# Ejemplo de uso
dia = "miércoles"
resultado = evaluar_dia(dia)
print(f"El día {dia} indica: {resultado}")  

# Sentencia match en Python 3.10 para control de flujo
dia = 8 # 1 representa lunes, 2 martes, ..., 7 domingo

match dia:
    case 1:
        mensaje = "Hoy es lunes, inicio de la semana."
    case 2:
        mensaje = "Hoy es martes, segundo día de la semana."
    case 3:
        mensaje = "Hoy es miércoles, mitad de la semana."
    case 4:
        mensaje = "Hoy es jueves, casi es viernes."
    case 5:
        mensaje = "Hoy es viernes, último día laboral."
    case 6 | 7:
        mensaje = "Es fin de semana, disfruta!"
    case _:
        mensaje = "Número de día no válido."    
    
print(mensaje)


user = {"nombre": "Ana", "rol": "admin", "activo": True}

match user:
    case {"nombre": nombre, "rol": "admin"}:
        print(f"El administrador '{nombre}' ha iniciado sesión.")
    case {"nombre": nombre, "rol": "invitado"}:
        print(f"El invitado '{nombre}' tiene acceso limitado.")
    case {"nombre": nombre, "rol": rol}:
        print(f"El usuario '{nombre}' tiene el rol de '{rol}'.")
    case _:
        print("El diccionario de usuario no es válido.")