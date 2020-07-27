# Problem Number 15
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
#     there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?


#  Use a Pascals triangle to find the Binomial Coefficient 
#      that goes with the lattice square combination maximum
pascal = 0
n = 41
for line in range(1, n + 1):  
    number = 1;
    for i in range(1, line + 1):
        
        # Get the middle of the 40th line
        if(line == n) and (i >= (line + 1)/2) and (i <= (line + 1)/2): pascal = number        
        number = int(number * (line - i) / i)
        
print("There are ", pascal, " paths on a 20x20 grid.")
  
