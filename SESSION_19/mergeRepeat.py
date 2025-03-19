'''
@Author : Akash Kakade
@Goal : To implement merge algorithm and Practice
'''

def merge(L:list, p:int, q:int, r:int):
    N1 = q-p+1
    N2 = r-q

    L1 = []
    i = 0;
    while(i < N1):
        element = L[p+i]
        L1.append(element)
        i = i+1

    L2=[]
    i = 0
    while(i<N2):
        element = L[q+1+i]
        L2.append(element)
        i = i+1

    print(f"L1:{L1}, L2:{L2}")

L = [34,12,45,10,20,30,40,13,17,25,27,32,35,45,50,29,91,89]

p = L.index(10)
q = L.index(40)
r = L.index(50)

merge(L, p, q, r)
