# Tarea 5

def busqueda ( lista, n):
    if isinstance ( lista, list) and lista != []:
        return busq_0 ( lista, 0), busq_n ( lista, -1, n, [])
    else:
        return " Error."

def busq_0 ( lista, ind):
    if ind < len ( lista) and lista[ind] == 0:
        return True
    elif ind < len ( lista):
        return busq_0 ( lista, ind + 1)
    else:
        return False

def busq_n ( lista, ind, n, lista_aux):
    if ind > - ( len ( lista) + 1) and lista[ind] == n:
        return busq_n ( lista, ind - 1, n, lista_aux)
    elif ind > - ( len ( lista) + 1):
        return busq_n ( lista, ind - 1, n, [lista[ind]] + lista_aux)
    else:
        return lista_aux
    
