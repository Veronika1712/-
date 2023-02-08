m = int(input())
x = 1
z = float(1)
if x >= 1 and x <= 100:
   while z >= 0.52 and z <= 33.7:
      z = z + (x*x + 100)/(x + 200)
      print(z, sep ="_")
      x += 1
