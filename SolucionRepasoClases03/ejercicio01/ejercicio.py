from ejercicio01.Curso import Curso


def menu():
    print("1.-Añadir alumno")
    print("2.-Buscar Alumno")
    print("3.-Mostrar Curso")
    print("4.-Fin")

def añadir():
    DNI=input("Dime DNI: ")
    nombre=input("Dime nombre: ")
    direccion=input("Dime direccion: ")
    telefono=input("Dime telefono: ")
    curso.añadir(DNI, nombre, direccion, telefono)

def buscar():
    DNI=input("Dime DNI: ")
    curso.buscar(DNI)

curso=Curso()
fin=False

while fin==False:
    menu()
    opcion=int(input("Escoge Opcion: "))
    if opcion==1:
        añadir()
    elif opcion==2:
        buscar()
    elif opcion==3:
        curso.ver_datos_curso()
    elif opcion==4:
        fin=True
        print("FIN")
    else:
        print("OPCION ERRONEA")
    


