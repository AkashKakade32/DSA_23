class Gensquare: 
    def __init__(self, N:int): 
        if type(N) != int: 
            raise TypeError(f'Bad type for N')
        if N <= 0: 
            raise ValueError(f'N must be positive but given {N}')
        self.N = N 

    def __iter__(self): 
        def get_generator(N:int): 
            for i in range(1, N+1): 
                yield i**2
        G = get_generator(self.N)
        self.G = G 
        return self

    def __next__(self): 
        return self.G.__next__()