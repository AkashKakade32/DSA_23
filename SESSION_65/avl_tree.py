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
        # Fixed: Proper height calculation
        # None node has height -1
        # Leaf node has height 0
        # Others have 1 + max(left_height, right_height)
        if z is None:
            return -1
        if z.left is None and z.right is None:
            return 0
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
                raise HeightValidationError(f"Node {z.data} is not balanced: balance factor = {z.balance()}")


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
        # STAGE 1 
        if type(data) != int: 
            raise TypeError(f"Data must be of type int")
   
        # STAGE 2 
        new_node = avl_node(data)
        run = self.root_node 
        if run is None: 
            self.root_node = new_node
            self.N += 1 
            return None  
        
        # Find insertion point
        while True: 
            if data < run.data: 
                if run.left is None: 
                    run.left = new_node 
                    run.left.parent = run 
                    break 
                else: 
                    run = run.left 
            else: 
                if run.right is None: 
                    run.right = new_node 
                    run.right.parent = run 
                    break 
                else: 
                    run = run.right 
        self.N += 1 
        
        # STAGE 3 & 4: Fix imbalances going up from inserted node
        z = new_node.parent
        while z is not None:
            # Check if z is imbalanced
            balance_factor = z.balance()
            
            if balance_factor > 1:  # Left-heavy
                # Determine if it's LL or LR
                if z.left.balance() >= 0:  # LL case
                    self.right_rotate(z)
                else:  # LR case
                    self.left_rotate(z.left)
                    self.right_rotate(z)
                break
                
            elif balance_factor < -1:  # Right-heavy
                # Determine if it's RR or RL
                if z.right.balance() <= 0:  # RR case
                    self.left_rotate(z)
                else:  # RL case
                    self.right_rotate(z.right)
                    self.left_rotate(z)
                break
            
            # Move up to check next ancestor
            z = z.parent


    def remove(self, r_data: int) -> None: 
        z = avl_tree._search_node(self.root_node, r_data)
        if z is None: 
            raise ValueError(f'{r_data} is not a part of tree')
        
        # Store the parent of the node being deleted for later rebalancing
        parent_of_deleted = z.parent
        
        # Standard BST deletion
        if z.left is None: 
            self.transplant(z, z.right)
        elif z.right is None: 
            self.transplant(z, z.left)
        else: 
            z_successor = avl_tree.min_node(z.right)
            parent_of_deleted = z_successor.parent if z_successor.parent != z else z_successor
            
            if z_successor is not z.right: 
                self.transplant(z_successor, z_successor.right)
                z_successor.right = z.right 
                z_successor.right.parent = z_successor 
            self.transplant(z, z_successor)
            z_successor.left = z.left 
            z_successor.left.parent = z_successor 
        
        self.N -= 1
        del z
        
        current = parent_of_deleted
        while current is not None:
            # Store parent before potential rotation
            next_parent = current.parent
            
            balance_factor = current.balance()
            
            if balance_factor > 1:  # Left-heavy
                # Choose the taller child of left subtree
                if current.left is not None:
                    if current.left.balance() >= 0:  # LL case
                        self.right_rotate(current)
                    else:  # LR case
                        self.left_rotate(current.left)
                        self.right_rotate(current)
                        
            elif balance_factor < -1:  # Right-heavy
                # Choose the taller child of right subtree
                if current.right is not None:
                    if current.right.balance() <= 0:  # RR case
                        self.left_rotate(current)
                    else:  # RL case
                        self.right_rotate(current.right)
                        self.left_rotate(current)
            
            # Move up to check next ancestor
            current = next_parent


if __name__ == '__main__': 
    from random import randint, seed
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

    # Enhanced test with 100 random numbers
    print("=" * 70)
    print("AVL TREE TEST WITH 100 RANDOM NUMBERS")
    print("=" * 70)
    
    # Set seed for reproducibility
    seed(42)
    N = 100
    data_list = list(set([randint(1, N*10) for i in range(N)]))  # Ensure unique values
    T = avl_tree()
    
    print(f"\nTesting with {len(data_list)} unique random numbers\n")
    print("INSERTION PHASE:")
    print("-" * 50)
    
    for i, data in enumerate(data_list, 1):
        T.insert(data)
        H = T.height()
        max_H = floor(1.44 * log2(len(T) + 2))  # Theoretical max for AVL
        consistent = T.is_consistent()
        print(f'Insert #{i:3d} (value={data:4d}): Height={H:2d}, Max={max_H:2d}, '
              f'Ratio={H/max_H if max_H > 0 else 0:.2f}, Consistent={consistent}')
        
        if not consistent:
            print(f"ERROR: Tree became inconsistent after inserting {data}")
            break
    
    print("\n" + "=" * 70)
    print(f"AFTER ALL INSERTIONS: {len(T)} nodes")
    print(f"Final Height: {T.height()}, Max Theoretical: {floor(1.44 * log2(len(T) + 2))}")
    print(f"Tree is consistent: {T.is_consistent()}")
    
    print("\nTree inorder traversal:")
    T.inorder()
    
    print("\n" + "=" * 70)
    print("DELETION PHASE:")
    print("-" * 50)
    
    # Shuffle for random deletion
    from random import shuffle
    delete_order = data_list.copy()
    shuffle(delete_order)
    
    for i, data in enumerate(delete_order, 1):
        T.remove(data)
        remainingN = len(T)
        
        if remainingN > 0:
            H = T.height()
            max_H = floor(1.44 * log2(remainingN + 2))
            consistent = T.is_consistent()
            print(f'Delete #{i:3d} (value={data:4d}): Remaining={remainingN:3d}, '
                  f'Height={H:2d}, Max={max_H:2d}, Ratio={H/max_H if max_H > 0 else 0:.2f}, '
                  f'Consistent={consistent}')
            
            if not consistent:
                print(f"ERROR: Tree became inconsistent after deleting {data}")
                break
        else:
            print(f'Delete #{i:3d} (value={data:4d}): Tree is now empty')
    
    print("\n" + "=" * 70)
    print(f"FINAL STATE: Tree has {len(T)} nodes")
    print(f"Tree is consistent: {T.is_consistent()}")
    print("=" * 70)