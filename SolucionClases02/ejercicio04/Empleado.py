class Empleado:

    def __init__(self,dni,nombre=""):
        self.dni=dni
        self.nombre=nombre
        self.apellidos=""
        self.salario=0
    
    def salario_neto(self):
        return self.salario-self.salario*0.12
    