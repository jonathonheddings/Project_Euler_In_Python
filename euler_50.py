# Problem Number 50
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

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

prime_list = sieve(1000000)

j_end = len(prime_list)
length = largest_prime_sum = 0

for i in range(0, len(prime_list)):
    for j in range(i + length, j_end):
        sum_ = sum(prime_list[i:j])
        if sum_ < 1000000: 
            if sum_ in prime_list:
                length = j - i
                largest_prime_sum = sum_
        else:
            j_end = j + 1
            break
    

print("The Largest Prime Sum Of Consecutive Primes is:", largest_prime_sum)