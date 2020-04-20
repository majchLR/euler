x = [i for i in range(1, 101)]
sq_x = []

for i in x:
    sq = i**2
    sq_x.append(sq)

print(sq_x)
ss = sum(sq_x)
print(ss)

sum_x = sum(x)
sum_sq = sum_x**2
print(sum_sq)

print(sum_sq - ss)