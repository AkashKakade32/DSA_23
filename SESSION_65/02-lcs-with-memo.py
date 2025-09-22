class LCS: 
    def __init__(self, X: str, Y: str): 
        self.X = X 
        self.Y = Y 
        self.c = [[None for j in range(len(Y))] for i in range(len(X))]


    def _solve(self, i, j): 
        if i == 0 or j == 0: 
            return 0 
        
        if i > 0 and j > 0: 
            if self.X[i] == self.Y[j]:
                n = self.c[i][j] 
                if n is None: 
                    self.c[i][j] = self._solve(self.X, self.Y, i-1, j-1)
                    n = self.c[i][j]
                else: 
                    return n + 1 
            else:
                m = self.c[i-1][j]
                if m is None: 
                    self.c[i-1][j] = self._solve(self.X, self.Y, i-1, j)
                    m = self.c[i-1][j]
                    
                n = self.c[i][j-1]
                if n is None: 
                    self.c[i][j-1] = self._solve(self.X, self.Y, i, j-1)
                    n = self.c[i][j-1]
                return max(m, n)


    def solve(self): 
        return self._solve(self.X, self.Y, len(self.X)-1, len(self.Y)-1)
