from ejemplo02.Barco import Barco

class Velero(Barco):
    
    def __init__(self,matricula,largo,ancho,numMastiles):
        super().__init__(matricula,largo,ancho)
        self.__numMastiles=numMastiles

    def get_num_mastiles(self):
        return self.__numMastiles


    def set_num_mastiles(self, value):
        self.__numMastiles = value

    def precio_dia_alquiler(self):
         return super().precio_dia_alquiler()+self.__numMastiles*10
    
    def toString(self):
        return super().toString()+" Mastiles: "+str(self.__numMastiles)