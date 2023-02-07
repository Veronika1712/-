x = float(input())
y = float(input())
if x < 4 and y > 0:
    print("I")
elif x > 4 and y > 0:
    print("II")
elif x > 4 and y < 0:
    print("III")
elif x == 4 and y < 0:
    print("false")
elif x == 4 and y > 0:
    print("false")
elif x > 4 and y == 0:
    print("false")
elif x < 4 and y == 0:
    print("false")
else:
    print("IV")
