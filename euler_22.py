# Problem Number 22
#      Using names.txt , a 46K text file containing over five-thousand first names, 
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, 
# multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, 
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
# COLIN would obtain a score of 938 × 53 = 49714. 
# What is the total of all the name scores in the file?
import pandas as pd
import numpy as np

alphabet = {'A':1,  'B':2,  'C':3,  'D':4,  'E':5,  'F':6,  'G':7,  'H':8,  'I':9,  'J':10, 
            'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 
            'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

# Pull data from the file
data = pd.DataFrame()
data = pd.read_csv('Python_Practice/Project_Euler/p022_names.csv')

# Create and sort list of names from data
name_list = []
for value in data:
    name_list.append(value)
name_list.sort()

# Calculate the word scores and store them
alph_value = 0
for name in range(0, len(name_list)): 
    for letter in str(name_list[name]):
        alph_value += alphabet[letter]
        
    name_list[name] = alph_value * (name + 1)
    alph_value = 0

# Sum the word scores and print the answer
sum_ = 0  
for i in range(0, len(name_list)):
    sum_ += int(name_list[i])
print("The Sum of all the alphebtized word scores in the text file is:", sum_)

