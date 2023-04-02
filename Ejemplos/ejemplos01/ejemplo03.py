# En Python existe un tipo propio para trabajar con funciones
# Hay que importat fractions

import fractions

fraccion1=fractions.Fraction(1,3)
fraccion2=fractions.Fraction(2,7)

print("Fraccion 1:",fraccion1,"es de tipo",type(fraccion1))
print("Fraccion 2:",fraccion2,"es de tipo",type(fraccion2))

suma=fraccion1+fraccion2
print("La suma es:",suma)