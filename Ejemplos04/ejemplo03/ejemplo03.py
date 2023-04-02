class Factura:

    #variable de clase
    IVA=0.21
    
    def __init__(self,base):
        self.base=base
    
    def total(self):
        return self.base+self.base*self.IVA
    
    def datos(self):
        return "Base: "+str(self.base)+" Total: "+str(self.total())

factura1=Factura(100)
print(factura1.datos())
print("Porcentaje IVA:",Factura.IVA)