from ejercicio02_03.Multimedia import Multimedia
from ejercicio02_03.ListaMultimedia import ListaMutimedia

def menu():
    print("1.-Añadir multimedia")
    print("2.-Devolver multimedia por posicion")
    print("3.-Ver multimedias")
    print("4.-Fin")

def añadir():
    titulo=input("Dime titulo: ")
    autor=input("Dime autor: ")
    formato=input("Dime formato: ")
    duracion=float(input("Dime duracion: "))
    multimedia=Multimedia(titulo,autor,formato,duracion)
    if lista.add(multimedia)==True:
        print("Multimedia añadido")
    else:
        print("ERROR. Lista completa")
    

def buscarposicion():
    posicion=int(input("Dime posicion: "))
    if posicion<lista.size():
        print(lista.get(posicion).toString())
    else:
        print("POSICION ERRONEA")

lista=ListaMutimedia()
fin=False

while fin==False:
    menu()
    opcion=int(input("Escoge Opcion: "))
    if opcion==1:
        añadir()
    elif opcion==2:
        buscarposicion()
    elif opcion==3:
        print(lista.toString())
    elif opcion==4:
        fin=True
        print("FIN")
    else:
        print("OPCION ERRONEA")
    