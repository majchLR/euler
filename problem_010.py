suma = 0

def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False

    return True


for y in range(2, 10):
    if is_prime(y):
        suma += y

print(suma)
