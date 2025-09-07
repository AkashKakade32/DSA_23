p = [30, 35, 15, 5, 10, 20, 25]
print(f'len(p):{len(p)}')
print(f'n = len(p)-1:{len(p)-1}')
N = len(p)
n = len(p)-1 

for l in range(2, n+1): 
    print(f"l:{l}")
    for i in range(1, n-l+2): 
        print(f'l:{l}:\ti:{i}')
        j = i + l - 1 
        print(f'\tFOR i = {i}, j={j}')
        for k in range(i, j): 
            print('\t\tk:', k)
        print(f'\tm[{i}:{j}] is SET')
#----------------------------------------
from math import inf as INFINITY 
N = len(p)
n = len(p)-1
m = [[0 for j in range(N)] for i in range(N)]
s = [[0 for j in range(N)] for i in range(N)]

for l in range(2, n+1): 
    for i in range(1, n-l+2): 
        j = i + l - 1
        m[i][j] = INFINITY 
        for k in range(i, j): 
            q = m[i][k] + m[k+1][j] + p[i-1] * p[k] * p[j]
            if q < m[i][j]: 
                m[i][j] = q 
                s[i][j] = k
print(f'OPTIMAL NUMBER OF STEPS:m[1][6]:{m[1][6]}')


def print_optimal_parens(s, i, j): 
    if i == j: 
        print(f'A{i}', end='')
    else: 
        print('(', end='')
        k = s[i][j]
        print_optimal_parens(s, i, k)
        print_optimal_parens(s, k+1, j)
        print(')', end='')

print('PARENTHIZED EXPRESSION:')
print_optimal_parens(s, 1, 6)
print()
print('END')