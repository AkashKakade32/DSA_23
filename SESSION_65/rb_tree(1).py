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
        return new_node  
    
    @staticmethod 
    def _height(x: rb_node) -> int: 
        '''
        Calculate height of subtree rooted at node x
        '''
        if x == rb_tree.NIL or x is None:
            return 0
        left_height = rb_tree._height(x.left)
        right_height = rb_tree._height(x.right)
        return 1 + max(left_height, right_height)


    def __init__(self): 
        self.root_node = rb_tree.NIL  # Initialize to NIL instead of None
        self.nr_elements = 0 


    def __len__(self): 
        return self.nr_elements 
    

    def left_rotate(self, x: rb_node) -> None: 
        '''
        Perform left rotation around node x
        '''
        y = x.right  # Set y
        x.right = y.left  # Turn y's left subtree into x's right subtree
        
        if y.left != rb_tree.NIL:
            y.left.parent = x
            
        y.parent = x.parent  # Link x's parent to y
        
        if x.parent == rb_tree.NIL:
            self.root_node = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
            
        y.left = x  # Put x on y's left
        x.parent = y


    def right_rotate(self, x: rb_node) -> None: 
        '''
        Perform right rotation around node x
        '''
        y = x.left  # Set y
        x.left = y.right  # Turn y's right subtree into x's left subtree
        
        if y.right != rb_tree.NIL:
            y.right.parent = x
            
        y.parent = x.parent  # Link x's parent to y
        
        if x.parent == rb_tree.NIL:
            self.root_node = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
            
        y.right = x  # Put x on y's right
        x.parent = y


    def rb_insert_fixup(self, z: rb_node) -> None: 
        '''
        Fix RB tree properties after insertion
        '''
        while z.parent.color == color.RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right  # Uncle
                if y.color == color.RED:
                    # Case 1: Uncle is red
                    z.parent.color = color.BLACK
                    y.color = color.BLACK
                    z.parent.parent.color = color.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        # Case 2: z is right child
                        z = z.parent
                        self.left_rotate(z)
                    # Case 3: z is left child
                    z.parent.color = color.BLACK
                    z.parent.parent.color = color.RED
                    self.right_rotate(z.parent.parent)
            else:
                # Mirror cases (parent is right child of grandparent)
                y = z.parent.parent.left  # Uncle
                if y.color == color.RED:
                    # Case 1: Uncle is red
                    z.parent.color = color.BLACK
                    y.color = color.BLACK
                    z.parent.parent.color = color.RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        # Case 2: z is left child
                        z = z.parent
                        self.right_rotate(z)
                    # Case 3: z is right child
                    z.parent.color = color.BLACK
                    z.parent.parent.color = color.RED
                    self.left_rotate(z.parent.parent)
        
        self.root_node.color = color.BLACK


    def _rb_transplant(self, u: rb_node, v: rb_node) -> None:
        '''
        Replace subtree rooted at u with subtree rooted at v
        '''
        if u.parent == rb_tree.NIL:
            self.root_node = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent


    def _tree_minimum(self, x: rb_node) -> rb_node:
        '''
        Find minimum node in subtree rooted at x
        '''
        while x.left != rb_tree.NIL:
            x = x.left
        return x


    def rb_delete_fixup(self, x: rb_node) -> None: 
        '''
        Fix RB tree properties after deletion
        '''
        while x != self.root_node and x.color == color.BLACK:
            if x == x.parent.left:
                w = x.parent.right  # Sibling
                if w.color == color.RED:
                    # Case 1: Sibling is red
                    w.color = color.BLACK
                    x.parent.color = color.RED
                    self.left_rotate(x.parent)
                    w = x.parent.right
                
                if w.left.color == color.BLACK and w.right.color == color.BLACK:
                    # Case 2: Both of sibling's children are black
                    w.color = color.RED
                    x = x.parent
                else:
                    if w.right.color == color.BLACK:
                        # Case 3: Sibling's right child is black
                        w.left.color = color.BLACK
                        w.color = color.RED
                        self.right_rotate(w)
                        w = x.parent.right
                    # Case 4: Sibling's right child is red
                    w.color = x.parent.color
                    x.parent.color = color.BLACK
                    w.right.color = color.BLACK
                    self.left_rotate(x.parent)
                    x = self.root_node
            else:
                # Mirror cases (x is right child)
                w = x.parent.left  # Sibling
                if w.color == color.RED:
                    # Case 1: Sibling is red
                    w.color = color.BLACK
                    x.parent.color = color.RED
                    self.right_rotate(x.parent)
                    w = x.parent.left
                
                if w.right.color == color.BLACK and w.left.color == color.BLACK:
                    # Case 2: Both of sibling's children are black
                    w.color = color.RED
                    x = x.parent
                else:
                    if w.left.color == color.BLACK:
                        # Case 3: Sibling's left child is black
                        w.right.color = color.BLACK
                        w.color = color.RED
                        self.left_rotate(w)
                        w = x.parent.left
                    # Case 4: Sibling's left child is red
                    w.color = x.parent.color
                    x.parent.color = color.BLACK
                    w.left.color = color.BLACK
                    self.right_rotate(x.parent)
                    x = self.root_node
        
        x.color = color.BLACK


    def insert(self, new_data: int) -> None: 
        '''
        Insert a new node with given data into the RB tree
        '''
        z = rb_tree.get_rb_node(new_data)
        y = rb_tree.NIL
        x = self.root_node
        
        # Find insertion position
        while x != rb_tree.NIL:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        
        # Set parent
        z.parent = y
        
        # Set as child
        if y == rb_tree.NIL:
            self.root_node = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z
        
        # New node is red
        z.left = rb_tree.NIL
        z.right = rb_tree.NIL
        z.color = color.RED
        
        # Fix RB properties
        self.rb_insert_fixup(z)
        self.nr_elements += 1


    def delete(self, r_data: int) -> None: 
        '''
        Delete node with given data from the RB tree
        '''
        # Find the node to delete
        z = self._find_node(r_data)
        if z == rb_tree.NIL:
            return  # Node not found
        
        y = z
        y_original_color = y.color
        
        if z.left == rb_tree.NIL:
            # No left child
            x = z.right
            self._rb_transplant(z, z.right)
        elif z.right == rb_tree.NIL:
            # No right child
            x = z.left
            self._rb_transplant(z, z.left)
        else:
            # Two children
            y = self._tree_minimum(z.right)
            y_original_color = y.color
            x = y.right
            
            if y.parent == z:
                x.parent = y
            else:
                self._rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            
            self._rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        
        if y_original_color == color.BLACK:
            self.rb_delete_fixup(x)
        
        self.nr_elements -= 1

    
    def _find_node(self, search_data: int) -> rb_node:
        '''
        Find and return node with given data
        '''
        x = self.root_node
        while x != rb_tree.NIL and search_data != x.data:
            if search_data < x.data:
                x = x.left
            else:
                x = x.right
        return x


    def find(self, search_data: int) -> bool: 
        '''
        Search for a node with given data in the RB tree
        '''
        return self._find_node(search_data) != rb_tree.NIL


    def height(self) -> int: 
        '''
        Return the height of the RB tree
        '''
        return rb_tree._height(self.root_node)
#----------------------------------------------------------------------------------------
if __name__ == '__main__': 
    from math import log2, floor 
    import random
    
    def max_height(N): 
        return floor(2 * log2(N+1))

    print("-" * 70)
    print("RED-BLACK TREE TEST WITH 100 RANDOM NUMBERS")
    print("-" * 70)
    
    # Generate 100 unique random numbers between 1 and 1000
    random.seed(42)  # For reproducible results
    numbers = random.sample(range(1, 1001), 100)
    
    T = rb_tree()
    
    # INSERT TEST
    print("\nINSERTION TEST:")
    print("-" * 50)
    for i, num in enumerate(numbers, 1):
        T.insert(num)
        current_h = T.height()
        max_h = max_height(len(T))
        print(f"Insert #{i} (value={num}): Height={current_h}, Max Allowable={max_h}")
    
    print("\n" + "-" * 70)
    print(f"AFTER ALL INSERTIONS: {len(T)} nodes")
    print(f"Final Height: {T.height()}, Max Allowable: {max_height(len(T))}")

    
    # Test find function
    print("\nSEARCH TEST:")
    print("-" * 50)
    test_values = random.sample(numbers, 5)  # Test with 5 existing values
    for val in test_values:
        print(f"Finding {val}: {T.find(val)}")
    print(f"Finding 9999 (not in tree): {T.find(9999)}")
    
    # DELETE TEST
    print("\n" + "-" * 70)
    print("DELETION TEST:")
    print("-" * 50)
    
    # Shuffle for random deletion order
    delete_order = numbers.copy()
    random.shuffle(delete_order)
    
    for i, num in enumerate(delete_order, 1):
        T.delete(num)
        remaining = len(T)
        if remaining > 0:
            current_h = T.height()
            max_h = max_height(remaining)
            print(f"Delete #{i} (value={num}): Remaining={remaining}, Height={current_h}, Max={max_h}")
        else:
            print(f"Delete #{i} (value={num}): Tree is now empty")
    
    del T
#----------------------------------------------------------------------------------------