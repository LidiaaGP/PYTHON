class NIF:
    
    def __init__(self,DNI):
        self.set_dni(DNI)
        
    def get_letra(self):
        return self.__letra

    def get_dni(self):
        return self.__DNI

    def set_dni(self, value):
        letras=['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
        self.__DNI = value
        self.__letra=letras[self.__DNI%23]

    def mostrar(self):
        print(self.__DNI,"-",self.__letra) 
  