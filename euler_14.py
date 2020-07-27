# Problem Number 14
# The following iterative sequence is defined for the set of positive integers:
#    n → n/2 (n is even)
#    n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
#    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# note: Once the chain starts the terms are allowed to go above one million.
answer = 0
count_buffer = 0

print("Calculating....")
for i in range(1, 1000001):
    collatz = i
    count = 0
    while collatz != 1:
        if collatz % 2 == 0: 
            collatz = (collatz / 2)
        else: 
            collatz = (3 * collatz) + 1
        count += 1
        
    if count >= count_buffer: 
        answer = i
        count_buffer = count
    
print("Collatz Number under 1 million with the longest chain: ", answer)
    