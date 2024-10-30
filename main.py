#Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b
# de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c
# del triangulo, dado por el teorema de Pitágoras: c2=a2+b2
#.

#Ingrese cateto a: 7
#Ingrese cateto b: 5
#La hipotenusa es 8.6023252670426267

import math # call math fuction

catA =float (input("Enter side A :"))
catB =float (input("Enter side B :"))
hyp = math.sqrt((catA**2)+(catB**2)) # math.sqrt to calculate square root 

print(f""" 
    The hypotenuse is :{hyp}
""")