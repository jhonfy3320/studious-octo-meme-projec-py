ARCHIVO_PEDIDOS = 'pedidos.txt'

def ver_historial():
    try:
        print('\n historial de pedidos' )
        with open(ARCHIVO_PEDIDOS, 'r', encoding='utf-8') as archivo:
            pedidos = archivo.readline()
            if pedidos:
                for i, pedido in enumerate(pedidos, start=1):
                    print(str(i) + '. ' + pedidos.strip())
            else:
                print('Aun no hay ningun pedido')
    except FileNotFoundError:
        print('\n Todavia no exixte un historial de pedidos')
