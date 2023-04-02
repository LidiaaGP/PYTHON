class SocioClub:
    
    def __init__(self,dni,nombre=None,apellidos=None,cuotaMensual=0):
        self.set_dni(dni)
        self.__nombre=nombre
        self.__apellidos=apellidos
        self.set_cuota_mensual(cuotaMensual)

    def get_dni(self):
        return self.__dni

    def get_nombre(self):
        return self.__nombre

    def get_apellidos(self):
        return self.__apellidos

    def get_cuota_mensual(self):
        return self.__cuotaMensual

    def set_dni(self, value):
        if len(value)==9:
            self.__dni = value
        else:
            print("ERROR. El DNI debe de tener 9 caracteres")

    def set_nombre(self, value):
        self.__nombre = value

    def set_apellidos(self, value):
        self.__apellidos = value

    def set_cuota_mensual(self, value):
        if value>=0:
            self.__cuotaMensual = value
        else:
            print("ERROR. La cuota mensual no puede ser negativa")

    def ver_socio(self):
        print("SOCIO:")
        print("DNI:",self.__dni)
        print("Nombre:",self.__nombre)
        print("Apellidos:",self.__apellidos)
        print("Cuota Mensual:",self.__cuotaMensual)