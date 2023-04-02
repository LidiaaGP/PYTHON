from ejemplo01.Persona import Persona

class Cliente(Persona):
    
    def __init__(self,DNI,nombre,edad,descuento):
        super().__init__(DNI,nombre,edad)
        self.__descuento=descuento

    def get_descuento(self):
        return self.__descuento


    def set_descuento(self, value):
        self.__descuento = value
    
    def toString(self):
        return super().toString()+" Descuento: "+str(self.__descuento)