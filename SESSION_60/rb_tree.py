#----------------------------------------------------------------------------------------
class color: 
    '''
    This class implements RED and BLACK colors to be given to each RB node. 
    '''
    RED = 1 
    BLACK = 2 
#----------------------------------------------------------------------------------------
class rb_node: 
    '''
    This class implements an rb_node. Constructor creates 'data', 'color', 
    and 'left', 'right', 'parent' attributes inside a newly created RB object. 

    Value of 'data' attribute is defauled to None, should be overrideen by the client 
    with actual data except for the NIL node where we keep value to be None. 

    Value of the 'color' attribute is defaulted to color.RED, should be overridden to 
    color.BLACK while creating NIL node 
    '''
    def __init__(self, color = color.RED, data = None):
        self.data = data 
        self.color = color 
        self.left, self.right, self.parent = None, None, None 


class rb_tree: 
    '''
    This class implements NIL node and methods of creating and manipulating the RB tree 
    '''
    NIL = rb_node(color=color.BLACK) 
   
    @staticmethod 
    def get_rb_node(data): 
        new_node = rb_node(data=data) 
        new_node.left, new_node.right, new_node.parent = rb_tree.NIL, rb_tree.NIL, rb_tree.NIL

    
    @staticmethod 
    def _height(x: rb_node) -> int: 
        pass 


    def __init__(self): 
        self.root_node = None 
        self.nr_elements = 0 


    def __len__(self): 
        return self.nr_elements 
    

    def left_rotate(self, x: rb_node) -> None: 
        pass 


    def right_rotate(self, x: rb_node) -> None: 
        pass 


    def rb_insert_fixup(self, x: rb_node) -> None: 
        pass 


    def rb_delete_fixup(self, x: rb_node) -> None: 
        pass 


    def insert(self, new_data: int) -> None: 
        pass 


    def delete(self, r_data: int) -> None: 
        pass 

    
    def find(self, search_data: int) -> bool: 
        pass 


    def height(self) -> int: 
        pass 
#----------------------------------------------------------------------------------------
if __name__ == '__main__': 
    from math import log2, floor 
    def max_height(N): 
        return floor(2 * log2(N+1))

    L = [10, 20, 30, 40, 50, 60, 70, 80, 100]
    
    T = rb_tree() 
    for x in L: 
        T.insert(x)
    
    print(f'Current Height:{T.height()}, allowable height:{max_height(len(T))}')
    
    for x in L: 
        T.delete(x)
    
    del T 
#----------------------------------------------------------------------------------------