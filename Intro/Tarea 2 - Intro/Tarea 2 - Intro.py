# Tarea 2 - Intro

def suma ( lista):
    if isinstance ( lista, list) and lista != []:
        return suma_aux ( lista, 0), suma_par ( lista, 0, [])
    else:
        print( " Error.")

def suma_aux( lista, ind):
    suma = 0
    while ind < ( len ( lista)):
        suma += lista[ind]
        ind += 1
    return ( suma)

def suma_par ( lista, ind, resultado):
    if ind < len ( lista) and lista[ind] % 2 == 0:
        return suma_par ( lista, ind + 1, resultado + [lista[ind]])
    elif ind < len ( lista):
        return suma_par ( lista, ind + 1, resultado)
    return ( resultado)
