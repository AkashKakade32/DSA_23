'''
Input: Non Empty list of integers
All elements exclusing the last element are sorted
Write code so that the entire list is sorted

'''

L = [10,20,30,40,50,60,25]

print("Before Algorithm : ",L)

k = L[len(L)-1]

i = len(L)-2

while i>=0:
    if L[i]>k:    
        L[i+1] = L[i]
    else:
        break
    i = i-1
L[i+1] = k

print("After Algorithm : ",L)