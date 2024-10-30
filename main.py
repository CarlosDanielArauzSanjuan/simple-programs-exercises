#Parte decimal
#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

#Ingrese un numero: 4.5
#0.5
#Ingrese un numero: -1.19
#0.19

def decimal(number): #followed by the function name and parentheses containing any parameters
    if number < 0: #cicle
        return abs(number) - int(abs(number)) #abs means absolute value
    return number - int(number)

numbers = float(input( "Enter the number: "))
decimals =  decimal(numbers)

print(f"""
    The decimal value of the number is: {decimals}
""")