import random

def busque_lineal(lista, objetivo):
    match = False

    for elemento in lista: # O(n)
        if elemento == object:
            match = True
            break
    
    return match


if __name__ == "__main__":
    tamaño_de_lista = int(input('De que tamaño es la lista?: '))
    objetivo = int(input('Que numero quieres encontrar?: '))

    lista = [random.randint(0, 100) for i in range(tamaño_de_lista)]
    
    encontrado = busque_lineal(lista, objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta en la ista" if encontrado else "no esta en la lista"}')
