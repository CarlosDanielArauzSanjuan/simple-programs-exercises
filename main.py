#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, 
# que indique qué hora marcará el reloj dentro de h horas:

#Hora actual: 3
#Cantidad de horas: 5
#En 5 horas, el reloj marcara las 8
#Hora actual: 11
#Cantidad de horas: 43
#En 43 horas, el reloj marcara las 6

actual = float(input("Enter actual time: "))
hours = float(input("Enter the number of hours to pronosticate the future time: "))
future = float(actual + hours) % 12

#cicle
if future == 0:
    future = 12
    
print(f"""
    in {hours} hours, the time will be {future}
""")