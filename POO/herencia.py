class Rectangulo:

#Inicializamos las instancias de la varíable para crear atributos generales
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

#Metodo general

    def are(self):
        return self.base * self.altura

#Sublase a la cual se le heredan los 
class Cuadrado(Rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado)




if __name__ == "__main__":
    rectangulo = Rectangulo(base = 3, altura= 4)
    print(rectangulo.are())

    cuadrado = Cuadrado(lado=5)
    print(cuadrado.are())