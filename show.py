

def mostrar_ingredientes(ingredientes):
    print(f'la masa es {ingredientes["masa"]}')
    print(f'la salsa es {ingredientes["salsa"]}')
    print(f'los ingredientes son:')
    for ing in ingredientes['ingredientes']:
        print(f'- {ing}')

if __name__ == '__main__':
    ingredientes_prueba = {'masa' : 'tradicional',
                        'salsa' : 'tomate',
                        'ingredientes' : ['queso', 'brocoli']}

    mostrar_ingredientes(ingredientes_prueba)
