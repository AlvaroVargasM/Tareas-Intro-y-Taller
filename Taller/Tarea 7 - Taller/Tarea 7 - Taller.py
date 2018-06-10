# Tarea 7

class conversion:
    def __init__( self, n):
        self.n = n

    def decAbi ( self, n):
        self.n = n
        if ( n > 1):
            self.decAbi ( self.n // 2)
        print ( n % 2)

    def biAdec ( self, n):
        self.n = n
        decimal = 0
        ind = 0
        while ( self.n != 0):
            ultimo_digi = self.n % 10
            decimal = decimal + ultimo_digi * ( 2 ** ind)
            self.n = self.n // 10
            ind += 1
        print ( decimal)
    
