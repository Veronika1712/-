import math
r=int(input())
b=int(input())
Sr= math.pi*r**2
Sb=b**2
if Sr>Sb:
    print("Площадь" ,Sr,"больше площади",Sb)
else:
    print("Площадь" ,Sr,"меньше площади",Sb)
