import math
 
def f(x):
    return 1.0 + 1.0 / (x + 1.0)
 
a = float(input())
 
x = math.ceil(1.0 / (a - 1.0) - 1.0)
while f(x) >= a:
    x += 1.0
 
print(f"f({x:.0f}) = {f(x)}")
