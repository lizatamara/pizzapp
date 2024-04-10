import masa
import salsa
import add
import remove
import show
import tiempo

ingredientes_orden = {'masa': 'Masa Tradicional',
                      'salsa': 'Salsa de Tomate',
                      'ingredientes': ['Queso']
                        }

while True:

    opcion = input('''¿Qué desea realizar?
                 1. Cambiar tipo de Masa
                 2. Cambiar tipo de Salsa
                 3. Agregar Ingredientes
                 4. Eliminar Ingredientes
                 5. Ordenar con los Ingredientes Actuales
                 0. Consultar ingredientes de la pizza
                 Otro Número cancelará el pedido.
                 > ''')
    
    if opcion == '1':
        eleccion = input("""Escoja el tipo de masa:
                         T) Tradicional
                         D) Delgada
                         B) Bordes de Queso
                        > """).upper()
        ingredientes_orden = masa.tipo_masa(ingredientes_orden, eleccion)
        

    elif opcion == '2':
        eleccion = input("""Escoja el tipo de salsa:
                         T) Salsa de Tomate
                         A) Salsa Alfredo
                         B) Salsa BBQ
                         P) Salsa Pesto
                        > """).upper()
        ingredientes_orden = salsa.tipo_salsa(ingredientes_orden, eleccion)
        
    elif opcion == '3':
        eleccion = int(input("""Desea agregar un ingrediente nuevo?:
                             1) Tomate
                             2) Champiñones
                             3) Aceituna
                             4) Cebolla
                             5) Pollo
                             6) Jamón
                             7) Carne
                             8) Tocino
                             9) Queso 
                             > """))
        ingredientes_orden = add.agregar_ingrediente(ingredientes_orden, eleccion)
        
    elif opcion == '4':
        eleccion = int(input("""Desea eliminar un ingrediente?:
                             1) Tomate
                             2) Champiñones
                             3) Aceituna
                             4) Cebolla
                             5) Pollo
                             6) Jamón
                             7) Carne
                             8) Tocino
                             9) Queso 
                             > """))
        ingredientes_orden = remove.quitar_ingredientes(ingredientes_orden, eleccion)
        

    elif opcion == '5':
        tiempo = tiempo.estimar_tiempo(ingredientes_orden)
        print(f'su pizza estará lista en {tiempo} minutos')
        
    elif opcion == '0':
        
        show.mostrar_ingredientes(ingredientes_orden)

    else:
        print('pedido cancelado')
        exit()

print('caca')
        


