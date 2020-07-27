# Problem Number 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#      a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#      There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math

c = 0
product = 0
for a in range(1,996):
    if product == 0: 
        for b in range(a, 997):
            c = math.sqrt((a * a) + (b * b))
            if (a + b + c) == 1000:
                product = int(a * b * c)
                break
                
    else: break
               
print("Product of the Pythagorean Triplet for which a + b + c = 1000: ", product)    