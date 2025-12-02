from menu import mostrar_menu
from pedidos import pedir_cafe
from ver_historial import ver_historial 

def main():
    while True:
        #Mostrar menu
        mostrar_menu()
        opcion = input('Selecciona una opcion: ')
        if opcion == '1':
            # Pedir un cafe 
            pedir_cafe()
        elif opcion == '2':
            # Ver historial
            ver_historial()
        elif opcion == '3':
            print('\n Muchas gracias por elejir nuestro riquicimo cafe')
            break
        else:
             print('Opcion invalida, por favor elija una opcion valida ')

if __name__ == '__main__':
    main()