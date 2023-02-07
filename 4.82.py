n=int(input())
if 0<n<100:
    g='лет'
    if (n // 10) % 10 != 1:
        if n % 10 == 1:
            g = "год"
        elif n % 10 in (2, 3, 4) and not (n in [12, 13, 14]):
            g = "года"
            print("Мне", n, g)
else:
    print("Возраст вне указанного диапазона")
