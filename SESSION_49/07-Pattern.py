'''
@goal:  We are implementing a container class T. 
        We should be able to iterate over object of class T 
        using for loop in order to visit all contained data elements 
'''

class T_iterator: 
    def __init__(self, G): 
        self.G = G 
    def __next__(self): 
        return self.G.__next__() 

    
class T: 
    def __init__(self, initialization_data): 
        # add appropriate attributes in object 
        pass # Your code here 

    def __iter__(self): 
        def get_generator(appropriate_input_data): 
            # add appropriate yield statements 
            pass # Your code here 
        return T_iterator(get_generator(appropriate_actual_parameter_list))
    

objT = T(appropriate_initialization_data)
for x in objT: 
    # do something with x 
    pass # Your code here 