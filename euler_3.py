# Problem Number 3
#
#  The prime factors of 13195 are 5, 7, 13 and 29.
#     What is the largest prime factor of the number 600851475143?
import math

def check_prime(integer):
    for i in range(2, int(math.sqrt(integer))):
        if(integer % i == 0):
            return False
    return True


number = 600851475143
largest_prime = 0

for integer in range(1, 775146):
    if number % integer == 0 and check_prime(integer):
        largest_prime = integer
        
print("Largest Prime Factor of 600851475143: ", largest_prime)