'''
@Goal:
    1) Accept list of positive integers from end user
    2) Print the list in index wise manner
    3) Calculate the arethematic mean of the list
    4) Print the arithematic mena

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
    2) We need variable sum to store the sum of all the values present in the List L
    3) We need variable length to calculate the length
    4) To calculate arethematic mean we need to use mean = sum/length
'''

sum = 0
k = 0

while(k<len(L)):
    sum = L[k] + sum
    k = k+1

mean = sum/len(L)

print(f"Arithematic Mean is : {mean}")
