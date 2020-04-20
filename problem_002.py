"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

fibo = [1, 2, 3, 5, 8]
x = 0

while True:
    k = fibo[-1] + fibo[-2]
    if k < 4000000:
        fibo.append(k)
        print(k)
    else:
        break

print(fibo)

for y in fibo:
    if y % 2 == 0:
        x = x + y
        print("y = ", y)
        print("x = ", x)