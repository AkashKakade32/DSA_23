def get_sublist(L, p, q):
    '''
    Return a sublist containing all elemets in L
    from index p to q, both included
    '''
    subL = []
    N = q-p+1
    i = 0
    while i<N:
        print(f"i = {i}, p = {p}, p+i = {p+i}")
        element = L[p+i]
        subL.append(element)
        i = i+1
    return subL


L = [10,20,30,40,50,60,70,80,90,100,120,130,140,150]

p = 2
q = 6

L1 = get_sublist(L, p, q)

print(f"Sublist from indices {p} to {q} including both indices", L1)