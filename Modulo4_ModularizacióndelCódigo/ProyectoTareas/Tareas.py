# Tareas.py
def crear_tarea(id_tarea, descripcion):
    return{
        'id': id_tarea,
        'descrippcion': descripcion,
        'completada': False
    }

def  agregar_tarea(lista_tareas, descripcion):
    nuevo_id = len(lista_tareas) +1
    tarea = crear_tarea(nuevo_id, descripcion)
    lista_tareas.append(tarea)

def listar_tareas(lista_tareas):
    if not lista_tareas:
        print('No hay tareas aun')
        return
    
    for tarea in lista_tareas:
        estado = 'Super' if tarea['Completada'] else 'Tiempo'
        print(f'{tarea[id]}. {tarea['descripcion']}')

def  maracar_completada(lista_tareas, id_tarea):
    for tarea in lista_tareas:
        if tarea['id'] == id_tarea:
            tarea['completada'] = True
            print(f'Tarea"{tarea["descrippcion"]}"marcada como completada')
            return
        print('No se encontro una tarea con ese ID')

def eliminar_tarea(lista_tareas, id_tarea):
    for tarea in lista_tareas:
        if tarea['id'] == id_tarea:
            print(f'Tarea "{tarea["descripcion"]}" eliminada.')
            return
        print('No se encontro una tarea con ese ID')