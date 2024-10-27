# Problema 1. División de una lista de enteros.
# Escribe una función que reciba por parámetro una lista de enteros y devuelva
# dos listas: una con los valores negativos que tuviera y otra con los positivos.
# Ambas listas deben estar ordenadas ascendentemente

def dividir_lista_enteros(lista):
    lista_enteros_positivos=[]
    lista_enteros_negativos=[]
    for a in lista:
        if (a >= 0):
            lista_enteros_positivos.append(a)
        else:
            lista_enteros_negativos.append(a)
    lista_enteros_positivos.sort()
    lista_enteros_negativos.sort()
    return lista_enteros_positivos, lista_enteros_negativos
positivos, negativos=dividir_lista_enteros([1,2,3,5,9,-1,-2,7,-9,0,-8])
print(positivos)
print(negativos)


