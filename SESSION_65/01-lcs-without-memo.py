def lcs(X: str, Y: str, i: int, j: int): 
    if i == 0 or j == 0: 
        return 0 
    
    if i > 0 and j > 0: 
        if  X[i] == Y[j]: 
            return lcs(X, Y, i-1, j-1) + 1 
        else:  
            return max(lcs(X, Y, i-1, j), lcs(X, Y, i, j-1)) 
        
X = 'AJKLBW'
Y = 'MAPKWZLB'

v = lcs(X, Y, len(X)-1, len(Y)-1)
print(v) 