# Product Number 10
#   The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#   Find the sum of all the primes below two million.
import math

def check_prime(integer):
    if integer < 3: return True
    for i in range(2, int(math.sqrt(integer)) + 1):
        if integer % i == 0:
            return False
    return True

sum_ = 2
for i in range(3, 2000001, 2):
    if check_prime(i):
        sum_ += i
        
print("Sum of Primes Below 2 Million Is: ", sum_)