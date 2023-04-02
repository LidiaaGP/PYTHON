from ejercicio01.Encuesta import Encuesta

encuesta=Encuesta("¿Lee libros habitualmente?(S/N)")
for i in range(10): 
    encuesta.incA()

for i in range(20): 
    encuesta.incB()

print(encuesta.get_pregunta())
print("Total Votos:",encuesta.total_votos())
print("Votos A:",encuesta.get_votos_a())
print("Votos B:",encuesta.get_votos_b())
print("Porcentaje A:",encuesta.porcentajeA())
print("Porcentaje B:",encuesta.porcentajeB())
