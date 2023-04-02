class Television:

    def __init__(self, numeroSerie,marca,modelo,anhoFabricacion,precioBase):
        self.numeroSerie=numeroSerie
        self.marca=marca
        self.modelo=modelo
        self.anhoFabricacion=anhoFabricacion
        self.precioBase=precioBase
    
    def precioconIVA(self):
        return self.precioBase*1.21
    
    def toString(self):
        return self.numeroSerie+" "+self.marca+" "+self.modelo+" "+str(self.anhoFabricacion)+" "+str(self.precioBase)+" Precio Final:"+str(self.precioconIVA())