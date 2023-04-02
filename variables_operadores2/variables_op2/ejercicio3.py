A=float(input("Dime altura en cm: "))
E=float(input("Dime edad: "))
k=float(input("Dime k: "))

PesoIdeal=A-100-((A-150)/4)+((E-20)/k)
print("Formula de Lorentz",PesoIdeal)
PesoIdeal=A-100+(E/10*9/10)
print("Formula de Perroult", PesoIdeal)
PesoIdeal=A-100
print("Formula de Brocca", PesoIdeal)
PesoIdeal=50+0.75*(A-150)
print("Fórmula de Metropolitan Life Insurance Company",PesoIdeal)