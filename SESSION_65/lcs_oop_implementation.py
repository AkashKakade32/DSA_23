class LongestCommonSubsequence:
    '''
    Implementation of Longest Common Subsequence using Dynamic Programming  
    '''
    
    # Direction constants for backtracking
    DIAGONAL = 1  
    UP = 2       
    LEFT = 3      
    
    def __init__(self, X: str, Y: str):
        '''
        Initialize LCS solver with two sequences
        X: First sequence (string or list)
        Y: Second sequence (string or list)
        '''
        # Input validation
        if type(X) not in [str, list]:
            raise TypeError('First sequence must be string or list')
        if type(Y) not in [str, list]:
            raise TypeError('Second sequence must be string or list')
        if len(X) == 0 or len(Y) == 0:
            raise ValueError('Sequences cannot be empty')
        
        self.X = X
        self.Y = Y
        self.m = len(X)
        self.n = len(Y)
        
        # c[i][j] stores length of LCS of X[1..i] and Y[1..j]
        # Following CLRS convention: indices 0 represent empty sequence
        self.c = [[0 for j in range(self.n + 1)] for i in range(self.m + 1)]
        
        # b[i][j] stores direction for solution reconstruction
        self.b = [[0 for j in range(self.n + 1)] for i in range(self.m + 1)]
        
        self.lcs_computed = False
        self.lcs_string = None
    
    
    def solve(self):
        '''
        Compute the length of LCS using dynamic programming
        '''
        # Initialize first row and column (empty sequence cases)
        for i in range(self.m + 1):
            self.c[i][0] = 0
        for j in range(self.n + 1):
            self.c[0][j] = 0
        
        # Fill the DP table
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                # Note: X[i-1] and Y[j-1] because our strings are 0-indexed
                # but our DP table uses 1-indexed convention from CLRS
                if self.X[i-1] == self.Y[j-1]:
                    self.c[i][j] = self.c[i-1][j-1] + 1
                    self.b[i][j] = self.DIAGONAL
                elif self.c[i-1][j] >= self.c[i][j-1]:
                    self.c[i][j] = self.c[i-1][j]
                    self.b[i][j] = self.UP
                else:
                    self.c[i][j] = self.c[i][j-1]
                    self.b[i][j] = self.LEFT
        
        self.lcs_computed = True
    
    
    def _construct_lcs(self, i: int, j: int, result: list):
        '''
        Private recursive method to construct LCS from b table
        '''
        if i == 0 or j == 0:
            return
        
        if self.b[i][j] == self.DIAGONAL:
            self._construct_lcs(i-1, j-1, result)
            result.append(self.X[i-1])
        elif self.b[i][j] == self.UP:
            self._construct_lcs(i-1, j, result)
        else:  # LEFT
            self._construct_lcs(i, j-1, result)
    
    
    def get_lcs(self) -> str:
        '''
        Return the actual longest common subsequence
        '''
        if not self.lcs_computed:
            self.solve()
        
        if self.lcs_string is None:
            result = []
            self._construct_lcs(self.m, self.n, result)
            if type(self.X) == str:
                self.lcs_string = ''.join(result)
            else:
                self.lcs_string = result
        
        return self.lcs_string
    
    
    def optimal_val(self) -> int:
        '''
        Return the length of the longest common subsequence
        '''
        if not self.lcs_computed:
            self.solve()
        return self.c[self.m][self.n]
    
    
    def print_lcs(self):
        '''
        Print the longest common subsequence
        '''
        lcs = self.get_lcs()
        print(f'LCS: {lcs}')
    


if __name__ == '__main__': 
    X = "AGGTAB"
    Y = "GXTXAYB"
    
    print(f'X = "{X}" (length: {len(X)})')
    print(f'Y = "{Y}" (length: {len(Y)})')
    
    lcs = LongestCommonSubsequence(X, Y)
    lcs.solve()
    
    length = lcs.optimal_val()
    subsequence = lcs.get_lcs()
    
    print(f'\nOPTIMAL VALUE (LCS Length): {length}')
    print(f'LONGEST COMMON SUBSEQUENCE: "{subsequence}"')
      
    