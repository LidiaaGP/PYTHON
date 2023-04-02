from ejercicio03.MarcaMaraton import MarcaMaraton

marca1=MarcaMaraton(1,59,59)
marca2=MarcaMaraton(2,0,1)
marca1.verMarca()
marca2.verMarca()
print("Iguales:",marca1.igualQue(marca2))
print("Menor:",marca1.menorQue(marca2))
print("Mayor:",marca1.mayorQue(marca2))

marca1.siguiente()
marca2.anterior()

marca1.verMarca()
marca2.verMarca()
print("Iguales:",marca1.igualQue(marca2))
print("Menor:",marca1.menorQue(marca2))
print("Mayor:",marca1.mayorQue(marca2))
