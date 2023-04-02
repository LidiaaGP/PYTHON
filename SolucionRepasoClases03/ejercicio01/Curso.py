from ejercicio01.Alumno import Alumno

class Curso:
    
    __MAX=40
    
    def __init__(self):
        self.__alumnos=[]
    
    
    def añadir(self,DNI,nombre,direccion,telefono):
        if len(self.__alumnos)==self.__MAX:
            print("ERROR. Maximo alcanzado")
        else:
            existe=False
            for alumno in self.__alumnos:
                if alumno.get_dni==DNI:
                    print("ERROR. Ya existe ese DNI")
                    existe=True
                    break
            if existe==False:
                self.__alumnos.append(Alumno(DNI,nombre,direccion,telefono))
                print("Alumno añadido")
    
    def buscar(self,DNI):
        existe=False
        for alumno in self.__alumnos:
            if alumno.get_dni()==DNI:
                existe=True
                print(alumno.toString())
                break
        if existe==False:
            print("NO ENCONTRADO")
    
    def ver_datos_curso(self):
        for alumno in self.__alumnos:
            print(alumno.toString())