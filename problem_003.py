prime_nums = []


def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            break
        elif x == num-1:
            return num


for y in range(2, 10000):
    if is_prime(y) is not None:
        prime_nums.append(y)

for number in prime_nums:
    if 600851475143 % number == 0:
        print(number, "jest dzielnikiem 600851475143")
