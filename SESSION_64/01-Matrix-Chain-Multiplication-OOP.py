
class MatrixChainMultiplication: 
    from math import inf as INFINITY 
    def __init__(self, p: list[int]): 
        if type(p) != list: 
            raise TypeError('Bad input')
        for x in p: 
            if type(x) is not int: 
                raise TypeError('Bad type for dimension')
            if x <= 0: 
                raise ValueError('Bad value for dimension')
        if len(p) < 2: 
            raise ValueError('Bad value')
        
        self.p = p 
        self.N = len(p)
        self.n = self.N - 1 
        self.m = [[0 for j in range(self.N)] for i in range(self.N)]
        self.s = [[0 for j in range(self.N)] for i in range(self.N)]

    
    def solve(self): 
        for l in range(2, self.n+1): 
            for i in range(1, self.n-l+2): 
                j = i + l - 1
                self.m[i][j] = self.INFINITY 
                for k in range(i, j): 
                    q = self.m[i][k] + self.m[k+1][j] + self.p[i-1] * self.p[k] * self.p[j]
                    if q < self.m[i][j]: 
                        self.m[i][j] = q 
                        self.s[i][j] = k


    @staticmethod
    def print_optimal_parens(s, i, j): 
        if i == j: 
            print(f'A{i}', end='')
        else: 
            print('(', end='')
            k = s[i][j]
            MatrixChainMultiplication.print_optimal_parens(s, i, k)
            MatrixChainMultiplication.print_optimal_parens(s, k+1, j)
            print(')', end='')
        
    
    def parenthize(self): 
        MatrixChainMultiplication.print_optimal_parens(self.s, 1, self.n)
        print()


    def optimal_val(self): 
        return self.m[1][self.n]
    

if __name__ == '__main__': 
    print('OOP VERSION')
    p = [30, 35, 15, 5, 10, 20, 25]
    MCM = MatrixChainMultiplication(p)
    MCM.solve() 

    print(f'OPTIMAL NUMBER OF STEPS:{MCM.optimal_val()}')
    print('PARENTHIZED EXPRESSION:')
    MCM.parenthize() 