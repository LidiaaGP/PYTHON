class Vehiculo:
   

    def __init__(self):
        self.marca=""
        self.modelo=""
        self.color=""
        self.num_ruedas=0
        self.precio=0


    def precio_IVA(self):
        return self.precio*1.21