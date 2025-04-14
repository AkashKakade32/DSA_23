def partition(L,p,r):
    pivot = L[r]
    i = p-1
    for j in range(p,r):
        if L[j] <= pivot:
            i = i + 1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[r] = L[r], L[i+1]
    return(i+1)

def quick_sort(L,p,r):
    if p < r:
        q = partition(L,p,r)
        quick_sort(L, p, q-1)
        quick_sort(L, q+1, r)

N = 10
L = []

from random import randint

for i in range(N):
    L.append(randint(1,100))

print("Before sort : ", L)
quick_sort(L, 0, len(L)-1)
print("After Sort : ", L)

