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
        insert_at_sorting_position(L,N)
        N = N+1

def display(L):
    for i in range(len(L)):
        print(i, L[i])

def main():
    L = [63,45,78,85,96,11,15,17,68,55]
    print("Before Sort : ", L)
    insertion_sort(L)
    print("After Sort : ", L)
    display(L)

main()        
