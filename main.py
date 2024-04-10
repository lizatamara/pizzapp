import masa
import salsa
import add
import remove
import show
import tiempo
import datos as d

ingredientes_orden = d.ingredientes

while True:

    opcion = input(d.menu)
    
    if opcion == '1':
        eleccion = input(d.T_MASA).upper()
        ingredientes_orden = masa.tipo_masa(ingredientes_orden, eleccion)
        

    elif opcion == '2':
        eleccion = input(d.T_SALSA).upper()
        ingredientes_orden = salsa.tipo_salsa(ingredientes_orden, eleccion)
        
    elif opcion == '3':
        eleccion = int(input(d.AG_INGREDIENTE))
        ingredientes_orden = add.agregar_ingrediente(ingredientes_orden, eleccion)
        
    elif opcion == '4':
        eleccion = int(input(d.QT_INGREDIENTE))
        ingredientes_orden = remove.quitar_ingredientes(ingredientes_orden, eleccion)
        

    elif opcion == '5':
        tiempo = tiempo.estimar_tiempo(ingredientes_orden)
        print(f'su pizza estará lista en {tiempo} minutos')
        
    elif opcion == '0':
        
        show.mostrar_ingredientes(ingredientes_orden)

    else:
        print('pedido cancelado')
        exit()
        


