'''
@Author: Akash Kakade
#Goal: To implement merge algorithm
'''


def merge(L:list, p:int, q:int, r:int) -> None:
    N1 = q-p+1
    N2 = r-q

    L1 = []
    i=0
    while i<N1:
        element = L[p+i]
        L1.append(element)
        i = i+1

    L2 = []
    i = 0
    while i<N2:
        element = L[q+1+i]
        L2.append(element)
        i = i+1
    
    print(f"L1 : {L1}, L2 : {L2}")

L = [10,15,3,63,78,79,80,81,82,11,12,13,14,15,1,2,5]

p = L.index(78)
q = L.index(82)
r = L.index(15)

merge(L,p,q,r)