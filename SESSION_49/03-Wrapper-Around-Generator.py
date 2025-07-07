class Wrapper: 
    def __init__(self, G): 
        self.G = G 

    def __next__(self): 
        return self.G.__next__()