def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


counter = 0
z = 2
while counter < 10001:
    if is_prime(z):
        counter += 1
        print(z, counter)
        z += 1
    else:
        z += 1


