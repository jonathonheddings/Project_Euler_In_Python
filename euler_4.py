# Project Number 4
#
# A palindromic number reads the same both ways. The largest palindrome made from the product
#    of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def convert_to_int(number):
    return int(''.join(str(i) for i in number))

palindrome = 0
for num1 in range(100, 999):
    for num2 in range(100, 999):
        num_string = [int(i) for i in str(num1 * num2)]
        if  num_string == num_string[::-1]:
            if convert_to_int(num_string) > palindrome:
                palindrome = convert_to_int(num_string)
                
print("The Largest Palindrome From Two 3 Digit Numbers Is: ", palindrome)
                
