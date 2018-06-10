# Sumatoria
""" Toma los valores dados por el usuario y los sumas, la suma aparece cuando el usuario introduce 0."""

def sumatoria ():
    suma = 0
    x = int ( input ( "Numero a sumar: "))
    while x != 0:
        suma += x
        x = int ( input ( "Numero a sumar: "))
    print ( "La suma de los numeros es: " + str(suma))

sumatoria()
