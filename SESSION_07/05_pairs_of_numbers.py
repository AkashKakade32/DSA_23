'''
@Goal:
   1) Accept the llst of numbers between 1 to 30 from end user in list L
   2) Accept the number between 40 and 60 from end user number N
   3) Find out and print all pairs in list whose sum is greater than N

'''

import sys

L = []

while True:
    num = int(input("Do you want to add another number? [1 for Yes and 0 for No] : "))
    if(num != 1):
        break

    num2 = int(input("Enter the Numbers between 1 to 30 : "))
    if((num2 < 1) or (num2 > 30)):
        print("Invalid Input.")
        sys.exit()
    L.append(num2)

N = int(input("Please enter the number between 40 and 60 : "))
if((N < 40) or (N > 60)):
        print("Invalid Input.")
        sys.exit()

i = 0
k = 0

pairs = []

while(i < len(L)):
    k = i+1
    while(k < len(L)):
        sum = 0
        sum = L[i] + L[k]
        if(sum > N):
            T = (L[i], L[k])
            pairs.append(T)
        k = k+1
    i = i + 1

print(f"Pairs are : {pairs}")