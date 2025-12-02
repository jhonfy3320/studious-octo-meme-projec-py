ARCHIVO_PEDIDOS = 'pedidos.txt'

def pedir_cafe():
    print('\n Elija el cafe que deseas llevar: ')
    print('1. Espresso')
    print('2. Cappuchino')
    print('3. Mocka')
    print('4. Americano')
    print('5. Latte')
    print('6. Latte Caramelo')

    opcion = input('Que cafe deseas tomar en este hermosos dia: ')

    cafes = {
        '1': 'Espresso',
        '2': 'cappuchino',
        '3': 'Mocka',
        '4': 'Americano',
        '5': 'Latte',
        '6': 'Latte Caramelo'
        }


    if opcion in cafes:
        cafe_elegido = cafes[opcion]
        print('Haz pedido un ' + cafe_elegido + '. ¡preparando tu cafe!')

        with open(ARCHIVO_PEDIDOS, 'a', encoding='utf-8') as archivo:
            archivo.write(cafe_elegido + ('\n'))

    else:
        print('Opcion no es valida intente de nuevo porfavo')