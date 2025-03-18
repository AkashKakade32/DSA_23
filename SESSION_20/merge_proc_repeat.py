def merge(L:list, p:int, q:int, r:int)->None:
    N1 = q-p+1
    N2 = r-q
    L1 = []
    L2 = []

    i = 0
    while i<N1:
        val = L[p+i]
        L1.append(val)
        i = i+1

    i = 0
    while i<N2:
        val = L[q+1+i]
        L2.append(val)
        i = i+1

    i = 0
    j = 0
    k = 0

    while True:
        if L1[i] <= L2[j]:
            L[p+k] = L1[i]
            k = k+1
            i = i+1
            if i == N1:
                while j<N2:
                    L[p+k] = L2[j]
                    k = k+1
                    j = j+1
                break
        else:
            L[p+k] = L2[j]
            k = k+1
            j = j+1
            if j==N2:
                while i<N1:
                    L[p+k] = L[i]
                    k = k+1
                    i = i+1
                break

L = [-2, 4, 3, 10, 20, 30, 40, 50, 60, 15, 17, 25, 35, 45, 50, 55, 60, -200, -100, 345]

p = 3
q = 8
r = 16

merge(L, p, q, r)

print(L)
