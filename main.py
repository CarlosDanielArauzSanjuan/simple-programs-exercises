#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:

#Primera nota: 55
#Segunda nota: 71
#Tercera nota: 46
#Cuarta nota: 87
#El promedio es: 64.75

first =float(input("Enter your first score:"))
second =float(input("Enter your second score:"))
third = float(input("Enter your third score:"))
fourth = float(input("Enter your fourth score:"))

print(f"""
      the Average grade is :{(first+second+third+fourth)/4}
      """)
