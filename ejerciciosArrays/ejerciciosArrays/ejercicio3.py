dias_semana=["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]
print(dias_semana)
dia=str(input("Dime día a buscar: "))
if dia in dias_semana:
    print(dia,"esta en la lista en la posicion",dias_semana.index(dia))
else:
    print(dia,"no esta en la lista")