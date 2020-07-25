# Problem Number 6
#  The sum of the squares of the first ten natural numbers is, 385.
#  The square of the sum of the first ten natural numbers is, 3025.
#  Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
#  3025 - 385 = 2640.
#  Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_squares = 0
for i in range(1, 100):
    sum_squares += i * i

square_sums = 0
for s in range(1,100):
    square_sums += s
square_sums = square_sums * square_sums

print("Difference between Square of Sums and Sum of Squares: ", square_sums - sum_squares)