class Articulo:
    
    def __init__(self,referencia,precio):
        self.__referencia=referencia
        self.set_precio(precio)
        self.__IVA=0.18

    def get_referencia(self):
        return self.__referencia

    def get_precio(self):
        return self.__precio

    def get_iva(self):
        return self.__IVA

    def set_referencia(self, value):
        self.__referencia = value

    def set_precio(self, value):
        if value>0:
            self.__precio = value
        else:
            print("ERROR. El precio debe de ser positivo")

    def set_iva(self, value):
        self.__IVA = value

    def precioFinal(self):
        return self.__precio*(1+self.__IVA)
    
    def precioFinaldescuento(self,descuento):
        if descuento>0 and descuento<1:
            return self.__precio*(1-descuento)*(1+self.__IVA)
        else:
            return self.__precio*(1+self.__IVA)