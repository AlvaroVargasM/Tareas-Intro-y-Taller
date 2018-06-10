# Tarea 4 - Intro

def busq_prim( lista):
    if isinstance ( lista, list) and lista != []:
        return bp ( lista, 0, [])
    else:
        return " Error."

def bp ( lista, ind, lista_aux):
    if ind < len ( lista):
        if lista[ind] % 2 == 0 or lista[ind] % 3 == 0 or lista[ind] % 5 == 0 or lista[ind] % 7 == 0 or lista[ind] == 1:
            return bp ( lista, ind + 1, lista_aux)
        else:
            return bp ( lista, ind + 1, lista_aux + [lista[ind]])
    else:
        return lista_primo (lista_aux)

def lista_primo ( lista):
    print ( lista)
