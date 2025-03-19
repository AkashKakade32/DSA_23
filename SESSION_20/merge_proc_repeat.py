def merge(L:list, p:int, q:int, r:int):
    N1 = q-p+1
    N2 = r-q

    L1 = []
    L2 = []

    i = 0
    while(i < N1):
        element = L[p+i]
        L1.append(element)
        i = i+1

    i = 0
    while(i < N2):
        element = L[q+1+i]
        L2.append(element)
        i = i+1

    print(f"L1 : {L1}, L2 : {L2}")

    i = 0
    j = 0
    k = 0

    while(True):
        if(L1[i] <= L2[j]):
            L[p+k] = L1[i]
            i = i+1
            k = k+1
            if(i == N1):
                while(j < N2):
                    L[p+k] = L2[j]
                    j = j+1
                    k = k+1
                break

        else:
            L[p+k] = L2[j]
            j = j+1
            k = k+1
            if(j == N2):
                while(i < N1):
                    L[p+k] = L1[i]
                    i = i+1
                    k = k+1
                break

def merge_sort(L:list, p:int, r:int):
    if(p<r):
        q = (p+r)//2
        merge_sort(L, p, q)
        merge_sort(L, q+1, r)
        merge(L, p, q, r)

L = [-3, -4, -5, 10, 20, 30, 40, 50, 17, 21, 23, 26, 29, 31, 34, -6, -10]

merge_sort(L, 0, len(L)-1)

print(L)
