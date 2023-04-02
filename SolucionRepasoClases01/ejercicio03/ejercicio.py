from ejercicio03.Pelicula import Pelicula
from ejercicio03.Productora import Productora

productora1=Productora("Dreamworks Pictures","http://www.dreamworksstudios.com/")
productora2=Productora("Warner Bros. Pictures","http://www.warnerbros.com/")
pelicula1=Pelicula("War Horse",productora1)
pelicula2=Pelicula("Gran Torino",productora2,"Clint Eastwood",119)
pelicula1.ver_datos()
pelicula2.ver_datos()
pelicula1.set_director("Steven Spielberg")
pelicula1.set_duracion(146)
pelicula1.ver_datos()