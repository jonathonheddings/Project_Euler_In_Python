# Problem Number 25
# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

fib_minor = 1
fib_major = 2
buffer = 0
digits = 0
index = 3

while(digits < 1000): 
    # Move Fibonacci Forward
    buffer = fib_major + fib_minor
    fib_minor = fib_major
    fib_major = buffer
    index += 1
    
    # Check Digits
    digits = len(str(fib_major))

print("The index of the first Fibonacci number to contain 1000 digits is:", index)