'''
@author: Yogeshwar 
@goal: to implement avl tree. 
'''


class HeightValidationError(Exception): 
    pass

class avl_node: 
    def __init__(self, data = None): 
        self.data, self.left, self.right, self.parent = data, None, None, None 


    def balance(self): 
        return avl_node.height(self.left) - avl_node.height(self.right)


    @staticmethod 
    def height(z): 
        if (z is None) or (z.left is None and z.right is None): 
            return 0 
        else: 
            return max(avl_node.height(z.left), avl_node.height(z.right)) + 1
        

class avl_tree:

    def __init__(self): 
        self.root_node = None 
        self.N = 0 


    @staticmethod 
    def _inorder(z: avl_node): 
        if z is not None: 
            avl_tree._inorder(z.left)
            print(f'[{z.data}]<->', end='')
            avl_tree._inorder(z.right)


    @staticmethod 
    def _height_validation(z: avl_node) -> None: 
        if z is not None: 
            avl_tree._height_validation(z.left)
            avl_tree._height_validation(z.right) 
            if z.balance() not in range(-1, 2): 
                raise HeightValidationError("The Tree is not balanced as per AVL definition")


    @staticmethod 
    def _search_node(root_node: avl_node, s_data: int) -> avl_node: 
        run = root_node 
        while run is not None: 
            if run.data == s_data: 
                break 
            elif s_data < run.data: 
                run = run.left 
            else: 
                run = run.right 
        return run 


    @staticmethod 
    def min_node(root_node) -> avl_node: 
        run = root_node 
        while run.left is not None: 
            run = run.left 
        return run 
    
    @staticmethod 
    def next_imbalanced_node(z: avl_node) -> avl_node: 
        while z is not None: 
            if z.balance() not in range(-1, 2): 
                break 
            z = z.parent 
        return z

    def transplant(self, u: avl_node, v: avl_node): 
        if u.parent is None: 
            self.root_node = v 
        elif u is u.parent.left: 
            u.parent.left = v 
        else: 
            u.parent.right = v 
        
        if v is not None: 
            v.parent = u.parent

    def __len__(self): 
        return self.N 
    

    def is_consistent(self) -> bool: 
        try: 
            avl_tree._height_validation(self.root_node)
        except: 
            return False 
        else: 
            return True 


    def height(self): 
        return avl_node.height(self.root_node) 


    def inorder(self): 
        print("[START]<->", end='')
        avl_tree._inorder(self.root_node)
        print("[END]")


    def left_rotate(self, x: avl_node) -> None: 
        # Part 1 
        y = x.right 
        x.right = y.left 
        if y.left is not None: 
            y.left.parent = x 
        # Part 2 
        y.parent = x.parent 
        if x.parent is None: 
            self.root_node = y 
        elif x is x.parent.left: 
            x.parent.left = y 
        elif x is x.parent.right: 
            x.parent.right = y 
        # Part 3 
        y.left = x 
        x.parent = y 


    def right_rotate(self, x: avl_node) -> None: 
        # Part 1 
        y = x.left 
        x.left = y.right 
        if y.right is not None: 
            y.right.parent = x 
        # Part 2 
        y.parent = x.parent 
        if x.parent is None: 
            self.root_node = y 
        elif x is x.parent.left: 
            x.parent.left = y 
        elif x is x.parent.right: 
            x.parent.right = y 
        # Part 3 
        y.right = x 
        x.parent = y 

    
    def insert(self, data: int) -> None: 
        '''
        STAGE 1: Input validation
        STAGE 2: BST insert 
        STAGE 3: Detect if there is an imbalance and if it is then where? 
        STAGE 4: Detect the type of violation and fix it. 
        '''
        if type(data) != int: 
            raise TypeError(f"Data must be of type int")
        # STAGE 1 
        z = avl_node(data)
        run = self.root_node 
        if run is None: 
            self.root_node = z
            self.N += 1 
            return None  
        
        # STAGE 2 
        while True: 
            if data < run.data: 
                if run.left is None: 
                    run.left = z 
                    run.left.parent = run 
                    break 
                else: 
                    run = run.left 
            else: 
                if run.right is None: 
                    run.right = z 
                    run.right.parent = run 
                    break 
                else: 
                    run = run.right 
        self.N += 1 
        
        # STAGE 3 
        x = z 
        y = z.parent 
        if y is not None: 
            z = y.parent 
        

        while z is not None: 
            if z.balance() not in range(-1, 2): 
                break 
            z = z.parent 
            y = y.parent 
            x = x.parent 

        
        if z is None: 
            return None 
        
        # STAGE 4 
        if y == z.left and x == y.left:     # LL violation 
            self.right_rotate(z)            # fix LL violation 
        elif y == z.left and x == y.right:  # LR vilation   
            self.left_rotate(y)             # fix LR violation 
            self.right_rotate(z)
        elif y == z.right and x == y.left:  # RL violation 
            self.right_rotate(y)            # Fix RL violation  
            self.left_rotate(z) 
        elif y == z.right and x == y.right: 
            self.left_rotate(z)


    def remove(self, r_data: int) -> None: 
        z = avl_tree._search_node(self.root_node, r_data)
        if z is None: 
            raise ValueError(f'{r_data} is not a part of tree')
        if z.left is None: 
            self.transplant(z, z.right)
            tmp = z 
            z = z.right 
        elif z.right is None: 
            self.transplant(z, z.left)
            tmp = z 
            z = z.left 
        else: 
            z_successor = avl_tree.min_node(z.right)
            if z_successor is not z.right: 
                self.transplant(z_successor, z_successor.right)
                z_successor.right = z.right 
                z_successor.right.parent = z_successor 
            self.transplant(z, z_successor)
            z_successor.left = z.left 
            z_successor.left.parent = z_successor 
            tmp = z 
            z = z_successor 
        
        del tmp 

        while True: 
            # find next imbalanced node 
            z = avl_tree.next_imbalanced_node(z)
            if z is None: 
                break 
            
            # set x, y 
            heightL = avl_node.height(z.left) 
            heightR = avl_node.height(z.right) 
            if heightL > heightR: 
                y = z.left 
            else: 
                y = z.right 

            if y is not None: 
                heightL = avl_node.height(y.left) 
                heightR = avl_node.height(y.right) 
                if heightL > heightR: 
                    x = y.left 
                else: 
                    x = y.right 

            # check violation type & fix it 
            if y is z.left and x is y.left:     # LL case 
                self.right_rotate(z)
            elif y is z.left and x is y.right:  # LR case 
                self.left_rotate(y)
                self.right_rotate(z)
            elif y is z.right and x is y.left:  # RL case 
                self.right_rotate(y) 
                self.left_rotate(z)
            elif y is z.right and x is y.right: # RR case 
                self.left_rotate(z)
        self.N -= 1 

if __name__ == '__main__': 
    from random import randint 
    from sys import argv, exit 
    from math import floor, log2

    def geh(tb=False, do_exit=True): 
        from sys import exc_info
        from traceback import print_tb 
        exc_name, exc_data, exc_tb = exc_info()
        print(exc_name.__name__, exc_data, sep=':')
        if tb is True: 
            print_tb(exc_tb)
        if do_exit: 
            exit(-1)

    argc = len(argv)
    if argc == 1: 
        print(f"UsageError:Correct Usage:{argv[0]} number_of_elements")
        exit(-1)
    
    try:
        N = int(argv[1])
        if N <= 0: 
            raise ValueError("Number of elements must be a positive number")
    except: 
        geh() 

    data_list = [randint(1, N*10) for i in range(N)] 
    T = avl_tree() 
    

    for data in data_list: 
        T.insert(data)
        print(f'Inserted:{data}, T.is_consistent():{T.is_consistent()}, #N:{len(T)}')
        H = T.height()
        max_H = floor(1.5 * log2(len(T)))
        print(f"Height:{H}, max_H:{max_H}")
    
    T.inorder()

    for data in data_list: 
        T.remove(data)
        remainingN = len(T)
        print(f'Removed data:{data}, #N:{remainingN}')
        if len(T) != 0: 
            H = T.height()
            max_H = floor(1.5 * log2(len(T)))
            print(f"Height:{H}, max_H:{max_H}")
     
    