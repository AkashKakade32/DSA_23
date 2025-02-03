def insert_at_sorting_position(L, N:int):
    k = L[N-1]
    i = N-2
    while i>=0:
        if L[i]>k:
            L[i+1] = L[i]
        else:
            break
        i = i-1
    L[i+1] = k

def insertion_sort(L):
    N = 2
    while N<=len(L):
        
