class Array_iterator: 
    def __init__(self, G): 
        self.G = G 
    def __next__(self): 
        return self.G.__next__()

class Array: 
    def __init__(self, N): 
        if type(N) is not int: 
            raise TypeError('Size of array must be an integer')
        if N < 0: 
            raise ValueError('Size of array must be positive int')
        self.L = [0 for i in range(N)]


    def set(self, i, val): 
        if i not in range(len(self.L)): 
            raise IndexError('Array index out of range')
        self.L[i] = val 


    def get(self, i): 
        if i not in range(len(self.L)): 
            raise IndexError('Array index out of range')
        return self.L[i]


    def __len__(self): 
        return len(self.L)


    def __iter__(self): 
        def get_generator(lst: list): 
            for x in lst: 
                yield x 
        return Array_iterator(get_generator(self.L))

    
A = Array(8)

for i in range(len(A)): 
    A.set(i, (i+1) * 100)

print('----Iterating using for loop and indexing----')
for i in range(len(A)): 
    val = A.get(i)
    print(f'Element at index {i} is {val}')

print('----Iterating using for loop----')
for x in A: 
    print(x)


