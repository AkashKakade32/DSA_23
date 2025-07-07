'''
@goal: Implement class Gensquare which can be used as follows: 

gs = Gensquare(8)

for x in gs: 
    print(x) # 1, 4, 9, 16, 25, 36, 49, 64

'''

class Gensquare_iterator: 
    def __init__(self, G): 
        self.G = G 
 
    def __next__(self): 
        return self.G.__next__()

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
        I = Gensquare_iterator(G)
        return I 

gs = Gensquare(8)
print('----Iterating using for loop----')
for x in gs: 
    print(x) 

print('----Iterating using while loop----')
I = gs.__iter__()
while True: 
    try: 
        x = I.__next__()
        print(x)
    except StopIteration: 
        break 