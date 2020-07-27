# Problem Number 35
# The number, 197, is called a circular prime because all rotations of the digits: 
# 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?
import math
import timeit

def sieve(maximum): 
    prime_list = [True] * (maximum + 1)
    prime_list[0] = False
    prime_list[1] = False
    
    for num in range(2, maximum + 1):
        if prime_list[num]:
            for q in range(2 * num, maximum + 1, num):
                prime_list[q] = False 
                     
    list_of_primes = []
    for prime in range(0,len(prime_list)):
        if prime_list[prime]: list_of_primes.append(prime)
    return list_of_primes

def convert_to_int(number):
    return int(''.join(str(i) for i in number))

def move_right(iteration):
    length = int(len(str(iteration)))
    num_string = [int(i) for i in str(iteration)]
    last_number = num_string[len(num_string) - 1]
    for i in range(0, length):
        if i < length - 1: num_string[length - i - 1] = num_string[length - i - 2]
        else: num_string[0] = last_number
    return int(''.join(str(i) for i in num_string))


prime_list = sieve(1000000)
        
count = 0   
for prime in prime_list:   
    if len(str(prime)) == 1:
        count +=1
        continue
    iteration = prime
    all_iterations = 1
    for i in range(1, len(str(prime))):
        iteration = move_right(iteration)
        if iteration in prime_list:
            all_iterations += 1
            if all_iterations >= len(str(prime)): 
                count += 1    
        else: break
    
print("There are", count, "Circular Primes from 0 to 1 Million.")