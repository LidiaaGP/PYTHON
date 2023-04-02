from ejercicio05.NotasAlumno import NotasAlumno

alumno1=NotasAlumno()
alumno1.set_asignatura("Lenguajes de Marcas")
alumno1.set_nombre("Andres")
alumno1.set_apellidos("Vieites Rodriguez")
alumno1.set_nota_eval_1(6)
alumno1.set_nota_eval_2(7.5)
alumno1.set_nota_eval_3(8.6)

print(alumno1.get_asignatura(),alumno1.get_nombre(),alumno1.get_apellidos(),alumno1.get_nota_eval_1(),alumno1.get_nota_eval_2(),alumno1.get_nota_eval_3(),alumno1.media())