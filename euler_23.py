# Problem Number 23
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# A number n is called deficient if the sum of its proper divisors is less than n 
# and it is called abundant if this sum exceeds n.
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
# the smallest number that can be written as the sum of two abundant numbers is 24. 
# By mathematical analysis, it can be shown that all integers greater than 
# 28123 can be written as the sum of two abundant numbers. However, 
# this upper limit cannot be reduced any further by analysis even though it is known that 
# the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.


def is_abundant(integer):
    sum_ = 0
    for i in range(1, int(integer / 2) + 1):
        if integer % i == 0: sum_ += i
    if sum_ > integer: return True
    else: return False


abundant_list = []
for num in range(0, 28124):
    if is_abundant(num) == True: abundant_list.append(num)

sumtwo_abundants = []
sumtwo_abundants = [False] * 28124

for i in range(0, len(abundant_list)):
    for j in range(i, len(abundant_list)):
        if (abundant_list[i] + abundant_list[j]) <= 28123:
            sumtwo_abundants[abundant_list[i] + abundant_list[j]] = True
        break

sum_ = 0
for number in range(0, 28124):
    if (sumtwo_abundants[number] == False): 
        sum_ += (number)
print("The Sum of all the numbers that cant be made by summing two abundant numbers is: ", sum_)
            