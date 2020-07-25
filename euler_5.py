# Problem Number 5
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#         What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

num = 20
loop = True
while loop == True:
    for i in [19, 17, 13, 15, 11, 12, 14, 16, 18]:
        if num % i == 0:
            if i == 18:
                print("Smallest Positive Number Divisible By All Numbers From 1 to 20: ", num)
                loop = False
        else:
            break
        
    num += 20
    