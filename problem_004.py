"""Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers."""


num_list = []
palin_list = []

for i in range(100, 1000):
    for j in range(100, 1000):
        z = i * j
        num_list.append(z)

for s in num_list:
    str_s = str(s)
    rev = str_s[::-1]
    if rev == str_s:
        print(str_s)
        palin_list.append(int(str_s))
palin_list.sort()
print(palin_list)