# Problem Number 49
# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
# is unusual in two ways: (i) each of the three terms are prime, and, 
# (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
# exhibiting this property, 
# but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?

def sieve(maximum): 
    prime_list = [True] * (maximum + 1)
    prime_list[0] = False
    prime_list[1] = False
    
    for num in range(2, maximum + 1):
        if prime_list[num]:
            for q in range(2 * num, maximum + 1, num):
                prime_list[q] = False 
    list_of_primes = []
    for prime in range(165, len(prime_list)):
        if prime_list[prime]: list_of_primes.append(prime)
    return list_of_primes

prime_list = sieve(9999)
a = []
b = []
c = []
count = 0
print("Calculating.... this will take a while..")
for number in range(1000, 10000):
    for prime in prime_list:
        if (prime + number) in prime_list:
            if (prime + number + number) in prime_list:
                a.append(prime)
                b.append(prime + number)
                c.append(prime + number + number)
                a_s = "".join(sorted(str(a[count])))
                b_s = "".join(sorted(str(b[count])))
                c_s = "".join(sorted(str(c[count])))
                count += 1
                if (c_s == a_s) and (a_s == b_s): print("4 Digit Prime Arithmetic Sequence: ", prime, "", (prime + number), "", (prime + number + number), "Term of Addition:", number)

