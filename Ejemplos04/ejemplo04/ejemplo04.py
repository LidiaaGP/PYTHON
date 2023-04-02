class Conversiones:
    
    #variable de clase
    cambioDolar=1.1
      
    #Metodo de clase
    @classmethod
    def euros_a_dolares(cls,euros):
        return euros*cls.cambioDolar

print(Conversiones.euros_a_dolares(10))