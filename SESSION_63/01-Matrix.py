class Matrix: 
    def __init__(self, r: int, c: int): 
        if type(r) != int or type(c) != int: 
            raise TypeError('Bad type for row or column')
        if r <= 0 or c <= 0: 
            raise ValueError('Bad value for row or column')
        self.r = r 
        self.c = c 
        self.M = [[0.0 for i in range(c)] for j in range(r)]

    
    def __add__(self, other): 
        if self.r != other.r or self.c != other.c: 
            raise ValueError('Incompatible dimensions')
        addM = Matrix(self.r, self.c)
        for i in range(self.r): 
            for j in range(self.c): 
                addM.M[i][j] = self.M[i][j] + other.M[i][j]
        return addM


    def __sub__(self, other): 
        if self.r != other.r or self.c != other.c: 
            raise ValueError('Incompatible dimensions')
        subM = Matrix(self.r, self.c)
        for i in range(self.r): 
            for j in range(self.c): 
                subM.M[i][j] = self.M[i][j] - other.M[i][j]
        return subM 
    

    def __mul__(self, other): 
        if self.c != other.r: 
            raise ValueError('Incompatible dimensions for multiplicatoin')
        mulM = Matrix(self.r, other.c)

        for i in range(self.r): 
            for j in range(other.c): 
                element = 0.0
                for k in range(self.c): 
                    element += self.M[i][k] * other.M[k][j]
                mulM.M[i][j] = element 

        return mulM 
    

    def __getitem__(self, S: slice): 
        if type(S) != slice: 
            raise TypeError('Bad syntax')
        if S.step is not None: 
            raise ValueError('Step must not be given') 
        i = S.start 
        j = S.stop 
        if i not in range(self.r) or j not in range(self.c): 
            raise IndexError('Bad index')
        return self.M[i][j]
    

    def __setitem__(self, S: slice, rhs: float): 
        if type(S) != slice: 
            raise TypeError('Bad index')
        if S.step is not None: 
            raise ValueError('Step must not be given')
        if type(rhs) != int and type(rhs) != float: 
            raise TypeError('Value must be a numeric type')
        i = S.start 
        j = S.stop
        if i not in range(self.r) or j not in range(self.c): 
            raise IndexError('Bad index')
        self.M[i][j] = rhs 

    
    def __str__(self): 
        displayString = '' 
        for i in range(self.r): 
            for j in range(self.c): 
                displayString += f'M[{i}][{j}]:{self.M[i][j]}\n'
        return displayString
        


if __name__ == '__main__': 
    M1 = Matrix(3,3)
    M2 = Matrix(3,3)

    # Set M1 
    for i in range(3): 
        for j in range(3): 
            M1[i:j] = i + j 

    print("Showing M1:")
    print(M1)
    print('-------------------------------------------')
    # Set M2 
    for i in range(3): 
        for j in range(3): 
            M2[i:j] = ((i+1) * (j+1)) * 4

    print("Showing M2:")
    print(M2)
    print('-------------------------------------------')

    mAdd = M1 + M2 
    mSub = M1 - M2 
    mMul = M1 * M2 

    print('Showing Addition Matrix:')
    print(mAdd)

    print('Showing Subtraction Matrix:')
    print(mSub)

    print('Showing Multiplication Matrix:')
    print(mMul)