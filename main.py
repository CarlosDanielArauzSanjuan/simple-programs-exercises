import math
to = float(input("what is the temperature of the Egg\n")) 
tw = 100
ty = 70
m = 47
p = 1.038
c = 3.7
k = 5.4 * math.pow(10,-3)

div = math.pow(m,(2/3)) * (c * (math.pow(p, (1/3))))
div2 = (k * math.pow(math.pi, 2))* math.pow((4*math.pi) / 3, (2/3))
total = div/div2 
total2 = math.log(0.76 * ((to - tw) / (ty - tw)))
sec = total * total2
min = round(sec/60)

print(f"""
      The time to cook the egg is {round(sec)} seconds
      the time to cook the egg is {min} minutes
""")