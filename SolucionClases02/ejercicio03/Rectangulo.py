class Rectangulo:
   

    def __init__(self):
        self.base=0
        self.altura=0


    def perimetro(self):
        return 2*self.altura+2*self.base
    
    def area(self):
        return self.altura*self.base