class television:
    def __init__(self,numserie,marca,modelo,anhoFabricacion,precioBase):
        self.numserie=numserie
        self.marca=marca
        self.modelo=modelo
        self.anhoFabricacion=anhoFabricacion
        self.precioBase=precioBase
    
    def precioconIVA(self):
        return self.precioBase*1.21
        
    def toString(self):
        print(self.numserie,self.marca,self.modelo,self.anhoFabricacion,self.precioBase,self.precioconIVA())
    
