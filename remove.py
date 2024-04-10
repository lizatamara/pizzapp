def quitar_ingredientes(ingredientes, eleccion):
    disponibles = ['Tomate','Champiñones','Aceituna','Cebolla','Pollo',
                    'Jamón','Carne','Tocino','Queso']

    quitar = disponibles[eleccion -1]

    if quitar in ingredientes['ingredientes']:
        ingredientes['ingredientes'].remove(quitar)
        print(f'se ha quitado {quitar}')
    elif len(ingredientes['ingredientes']) == 0:
        print('no hay nada para quitar')
    else:
        print('no está en la lista')

    return ingredientes

if __name__ == '__main__':
    ingredientes_prueba = {'masa' : 'tradicional',
                           'salsa' : 'tomate',
                           'ingredientes' : ['queso','brocoli']
                        }
    eleccion = int(input("""seleccione el ingrediente a quitar:
                         1) piña
                         2) brocoli
                         3) pepperoni
                         4) aceituna
                         5) queso
                        """))
    
    ingredientes = quitar_ingredientes(ingredientes_prueba, eleccion)
    
    print(ingredientes)
    