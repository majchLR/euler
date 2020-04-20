""" 
Find the sum of all the multiples of 3 or 5 below 1000.
"""

result = 0
for x in range(1000):
    if x % 3 == 0 or x % 5 == 0:
        result += x
        
print("Sum of all the multiples =", result)