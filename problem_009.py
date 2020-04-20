licznik = 0

x = 1000

for a in range(1, x+1):
    for b in range(1, x+1):
        if a + b + (a**2 + b**2)**0.5 == x and a < b:
            c = x - a - b
            print(a, b, c)
            print(a * b * c)
            print((a**2 + b**2), c**2)
