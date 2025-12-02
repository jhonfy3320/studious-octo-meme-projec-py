# app.py

from Tareas import (
    agregar_tarea,
    listar_tareas,
    maracar_completada,
    eliminar_tarea,
)
from Menu import mostrar_menu, pedir_opcion


def main():
    lista_tareas = []
    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == 1:
            listar_tareas(lista_tareas)

        elif opcion == 2:
            descripcion = input("Descripción de la nueva tarea: ")
            agregar_tarea(lista_tareas, descripcion)

        elif opcion == 3:
            try:
                id_tarea = int(input("ID de la tarea a marcar como completada: "))
                maracar_completada(lista_tareas, id_tarea)
            except ValueError:
                print("Debes ingresar un número entero.")

        elif opcion == 4:
            try:
                id_tarea = int(input("ID de la tarea a eliminar: "))
                eliminar_tarea(lista_tareas, id_tarea)
            except ValueError:
                print("Debes ingresar un número entero.")

        elif opcion == 5:
            print("Saliendo del gestor de tareas. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
