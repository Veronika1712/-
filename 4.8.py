import math
x = float(input())
k = float()
f = float()
if math.sin(x)>=0:
    k = x**2
    print(k)
else:
    k = abs(x)
    print(k)
if x < k:
    f = abs(x)
    print(f)
else:
    f = k*x
    print(f)
