#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

#Ingrese numero: 345
#543
#Ingrese numero: 241
#142#

num = input("Enter a 3 digits number:")
invnum = num[::-1] #
print (f""" 
       the inverted number is {invnum}
       """)