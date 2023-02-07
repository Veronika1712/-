A=int(input())
B=int(input())
def func(A,B):
    sum = 0
    for C in range(A, B + 1):
      if C % 4 == 0:
         sum  += C
    return sum
 
print( func(A,B))
