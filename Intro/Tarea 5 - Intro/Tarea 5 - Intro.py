# Tarea 5

def busq_bi(lista, n):
    return bb_aux ( lista, n, 0, len ( lista) - 1)

def bb_aux ( lista, n, inicio, ultimo):
    if inicio <= ultimo:
        mitad = ( inicio + ultimo) // 2
        if lista[mitad] == n:
            print ( " Encontrado")
        else:
            if n < lista[mitad]:
                bb_aux ( lista, n, inicio, 0 + (mitad - 1)) 
            else:
                bb_aux ( lista, n, 0 + ( mitad + 1), ultimo)
    else:
        print ( " No encontrado")
    
   
    
