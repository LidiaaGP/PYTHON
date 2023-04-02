class Coche:
    def __init__(self,modelo,pasajeros,deposito,kpl):
        self.modelo=modelo
        self.pasajeros=pasajeros
        self.deposito=deposito
        self.kpl=kpl
    
    def calcularAutonomia(self):
        return self.deposito*self.kpl
    
    def mayorAutonomia(self,autonomia):
        resultado=False
        if self.calcularAutonomia()>autonomia:
            resultado= True
        return resultado
    
coche1=Coche("Renault x", 5, 60, 20)
coche2=Coche("Mercedes v", 7, 90, 30)
if coche1.mayorAutonomia(coche2.calcularAutonomia()):
    print (coche1.modelo," tiene mas autonomia que ",coche2.modelo)
else:
    print (coche2.modelo," tiene mas autonomia que ",coche1.modelo)