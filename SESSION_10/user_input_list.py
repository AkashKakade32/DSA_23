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
    while N<len(L):
        insert_at_sorting_position(L,N)
        N = N+1

def main():
    L = []
    while True:
        ans = int(input("Do You Want to Add More Number? [1 = Yes, 0 = No] : "))
        if ans!=1:
            break
        data = int(input("Please Enter the Number : "))
        L.append(data)
    
    print("Before Sorting : ", L)
    insertion_sort(L)
    print("After Sort : ", L)

main()