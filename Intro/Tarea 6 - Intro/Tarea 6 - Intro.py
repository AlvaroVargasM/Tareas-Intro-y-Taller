# Tarea 6 - Intro

def lista5x5 (n):
    lista = []
    lista1 = []
    while len ( lista) != 6:
        lista += [n]
    lista1 = ([lista] * 5) 
    return operaciones ( lista1, 0, 0, [], [])

def operaciones ( lista, i, ii, lista_aux, resultado):
    while ii < len ( lista [0]) and i < len ( lista):
        operacion = 0
        operacion = lista[i][ii] * -5 + 8
        lista_aux = [operacion]
        ii += 1
    if i < len ( lista):
        return operaciones ( lista, i + 1, 0, [], [lista_aux] + resultado)
    else:
        return resultado
    
        
    
