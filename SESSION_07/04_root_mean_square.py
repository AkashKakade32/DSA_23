'''
@Goal:
    1) Accept list of positive integers from end user
    2) Print the list in index wise manner
    3) Calculate the arethematic mean of the list
    4) Print the root mean
          root_mean_square = square root of (sum of all the squares of numbers in the list/length of list)

LEVEL 1: CODING
LEVEL 2: Reason the Loop using reasoning method

'''

import sys

L = []
size = 0

while True:
    num = int(input("Do you want to enter the another number? [1 for Yes, 0 for No] : "))
    if (num != 1):
        break
    if(num < 0):
        print("Number Must be positive")
        sys.exit()

    num2 = int(input("Enter the Number : "))
    L.append(num2)

if(len(L) == 0):
    print("Length of list must not be zero")
    sys.exit()

i = 0

while(i < len(L)):
    print(L[i])
    i = i + 1

'''
@Reasoning
    1) We need loop variable k to iterate over all the values present in the List L
    2) We need variable square_sum to store the square sum of all the values present in the List L
    3) We need variable length to calculate the length
    4) Square the every element present in the list and add them
    5) Calculate root mean square
'''

square_sum = 0
k = 0

while(k<len(L)):
    square_sum = (L[k]**2) + square_sum
    k = k+1

root_square_mean = (square_sum/len(L))**0.5

print(f"Root Mean Square is : {root_square_mean}")