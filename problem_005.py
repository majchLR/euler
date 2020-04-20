def divide_all(num):
    for i in range(2, 21):
        if num % i != 0:
            return False
    return True

z = 20

while True:
    if divide_all(z):
        break
    else:
        z += 10

print(z)