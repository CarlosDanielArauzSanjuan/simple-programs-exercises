#Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo. El promedio del ramo se calcula con la siguiente formula.

#Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, 
# y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

#Ingrese nota certamen 1: 45
#Ingrese nota certamen 2: 55
#Ingrese nota laboratorio: 65
#Necesita nota 72 en el certamen 3

def scoreNece(c1, c2, lab): #function calculates a score based on some criteria, such as points
    nfinal = 60
    NC = (c1 + c2 + 0) / 3  
    C3 = ((nfinal- lab * 0.3) / 0.7) * 3 - c1 - c2
    return C3

sc1 = float(input("Enter score 1: "))
sc2 = float(input("Enter score 2: "))
sclab = float(input("Enter score LAB: "))

scorefinal = scoreNece(sc1, sc2, sclab)

print(f"You need {scorefinal:.2f} score on the final exam ")