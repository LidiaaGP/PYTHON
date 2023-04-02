canalactual=int(input("Dime canal actual: "))
canaldestino=int(input("Dime canal destino: "))

if canalactual<canaldestino:
    adelante=canaldestino-canalactual
    atras=canalactual+(99-canaldestino)
else:
    adelante=canaldestino+(99-canalactual)
    atras=canalactual-canaldestino

if adelante>atras:
    print("Numero de saltos: ",atras)
else:
    print("Numero de saltos: ",adelante)