import random

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:
        if elemento == objetivo:
            match = True
    
    return match

if __name__ == '__main__':

    tamño_de_objetos = int(input('De que tamaño es la lista: '))
    objetivo = int(input('¿Que numero quieres encontrar?: '))
    lista = [random.randint(0,100) for i in range (tamño_de_objetos)]

    encontrado = busqueda_lineal(lista, objetivo)

    print(lista)
    print(f'El objetivo: {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    

