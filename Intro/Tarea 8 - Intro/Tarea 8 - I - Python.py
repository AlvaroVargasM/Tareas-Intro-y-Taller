# Tarea 8 - Intro
""" Construye un rectangulo de asteriscos en base al input del usuario."""

def principal():
    altura = int ( input ( "Cual sera la altura del triangulo? "))
    t1 = Triangulo( altura)
    t1.tri()
    
class Triangulo:
    def __init__ ( self, altura):
        self.__n = 1
        self.__altura = altura
        self.__lista = list ( range ( altura))

    def tri (self):      
        for i in self.__lista:
            ast = "*" * self.__n
            self.__n += 1
            print ( ast)

principal()
