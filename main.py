#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:

#ingrese el radio: 5
#Perimetro: 31.4
#Área: 78.5

radio = float(input("Enter the radio of the circunference: "))
print (f"""
    Area of the circunference is:{(radio**2)*3.1416}
    Perimeter of the circunference is:{radio*2*3.1416}
""")
