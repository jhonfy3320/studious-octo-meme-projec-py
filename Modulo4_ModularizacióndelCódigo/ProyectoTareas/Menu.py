def mostrar_menu():
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")


def pedir_opcion():
    try:
        opcion = int(input("Elige una opción: "))
        return opcion
    except ValueError:
        print("Debes ingresar un número.")
        return 0