'''
@author: Yogeshwar
@goal: to implement ADT of bst
''' 

class EmptyTreeError(Exception): 
    pass 

class TreeNoSuccessor(Exception): 
    pass 


class TreeNoPredecessor(Exception): 
    pass 


class bst_node: 
    def __init__(self, data: any): 
        self.data = data 
        self.left = None 
        self.right = None 
        self.parent = None 
    def __str__(self): 
        return f'data:{self.data}'

class bst: 

    @staticmethod
    def _preorder(r:bst_node) -> None: 
        if r is not None: 
            print(f"[{r.data}]->", end='')
            bst._preorder(r.left)
            bst._preorder(r.right)

    
    @staticmethod
    def _inorder(r:bst_node) -> None: 
        if r is not None: 
            bst._inorder(r.left)
            print(f"[{r.data}]->", end='')
            bst._inorder(r.right)


    @staticmethod
    def _postorder(r:bst_node) -> None: 
        if r is not None: 
            bst._postorder(r.left)
            bst._postorder(r.right)
            print(f"[{r.data}]->", end='')


    @staticmethod 
    def search_node(root_node: bst_node, s_data: any) -> bst_node: 
        run = root_node 
        while run is not None: 
            if s_data == run.data: 
                return run 
            elif s_data < run.data: 
                run = run.left 
            else:
                run = run.right 
        return None  
                

    @staticmethod 
    def inorder_successor_node(e_node: bst_node) -> bst_node: 
        if e_node.right is not None: 
            run = e_node.right 
            while run.left is not None: 
                run = run.left 
            return run 
        
        x = e_node 
        y = x.parent 
        while y is not None and x == y.right: 
            x = y 
            y = y.parent
        return y 


    @staticmethod 
    def inorder_predecessor_node(e_node: bst_node) -> bst_node: 
        if e_node.left is not None: 
            run = e_node.left 
            while run.right is not None: 
                run = run.right 
            return run 
        
        x = e_node 
        y = x.parent 
        while y is not None and x == y.left: 
            x = y 
            y = y.parent
        return y 


    @staticmethod
    def search_node(root_node: bst_node, search_data: any) -> bst_node:
        run = root_node
        while run is not None: 
            if run.data == search_data: 
                break 
            elif search_data < run.data: 
                run = run.left 
            else: 
                run = run.right 
        return run 


    def __init__(self): 
        self.root_node = None 
        self.nr_elements = 0 


    def insert(self, new_data: any) -> None: 
        ''' 
        @self: calling object of BST
        @new_data: object of any type that must be made 
        a part of tree.

        adds @new_data to a tree named by @self 
        '''
        new_node = bst_node(new_data)
        if self.root_node == None:
            self.root_node = new_node 
            self.nr_elements += 1 
            return None 
        run = self.root_node 
        while True: 
            if new_data <= run.data: 
                if run.left == None: 
                    run.left = new_node 
                    run.left.parent = run 
                    break 
                else: 
                    run = run.left 
            else: 
                if run.right == None: 
                    run.right = new_node 
                    run.right.parent = run 
                    break 
                else: 
                    run = run.right 
        self.nr_elements += 1 
        
    
    def inorder(self): 
        '''
        @self: calling BST object 
        Travel through a BST @self using inorder sequence
        '''
        print("[START]->", end='')
        bst._inorder(self.root_node)
        print("[END]")


    def preorder(self): 
        '''
        @self: calling BST object. 
        Traversl through a BST @self using preorder sequence 
        '''
        print("[START]->", end='')
        bst._preorder(self.root_node)
        print("[END]")     
        

    def postorder(self): 
        '''
        @self: calling BST object 
        Traverse through a BST @self using postorder sequence 
        '''
        print("[START]->", end='')
        bst._postorder(self.root_node)
        print("[END]") 


    def level_order(self): 
        '''
        @self: calling BST object 
        Travel through the BST in level order sequence
        '''
        Q = [self.root_node]
        print("[START]->", end='')
        while len(Q) != 0: 
            N = Q.pop(0)
            print(f'[{N.data}]->', end='')
            if N.left is not None: 
                Q.append(N.left)
            if N.right is not None: 
                Q.append(N.right)
        print('[END]')
        

    def search(self, s_data: any) -> bool: 
        '''
        @self: calling BST object 
        @s_data: data to be searched 
        Search for @s_data in BST @self. 
        Return True if found, False otherwise 
        '''
        run = self.root_node 
        while run is not None: 
            if s_data == run.data: 
                return True 
            elif s_data < run.data: 
                run = run.left
            elif s_data > run.data: 
                run = run.right 
        return False 


    def remove(self, r_data: any) -> None: 
        '''
        @self: calling BST object 
        @r_data: existing data to be dropped 

        Remove a node containing @r_data from BST @self. 
        Raise invalid_data exception if there is not node 
        containing @r_data 
        '''
        z = bst.search_node(self.root_node, r_data)
        if z is None: 
            raise ValueError(f"{r_data} : data to be removed is invalid")
        
        if z.left is None: 
            if z.parent is None: 
                self.root_node = z.right 
            elif z is z.parent.left: 
                z.parent.left = z.right 
            else: 
                z.parent.right = z.right 
            if z.right is not None: 
                z.right.parent = z.parent 
        elif z.right is None: 
            if z.parent is None: 
                self.root_node = z.left 
            elif z is z.parent.left: 
                z.parent.left = z.left 
            else: 
                z.parent.right = z.left 
            z.left.parent = z.parent
        elif z.left is not None and z.right is not None:
            y = z.right 
            while y.left is not None: 
                y = y.left 
            
            if y != z.right: 
                y.parent.left = y.right; # !!
                if y.right is not None: 
                    y.right.parent = y.parent
                y.right = z.right 
                y.right.parent = y 

            y.left = z.left 
            y.left.parent = y 
            
            if z.parent is None: 
                self.root_node = y 
            elif z is z.parent.left: 
                z.parent.left = y 
            else: 
                z.parent.right = y 

            y.parent = z.parent 

          
    def min(self) -> any: 
        '''
        @self: calling BST object 
        Returns a min data value held by any node in BST @self 
        Raises bst_empty exception if the tree is empty 
        '''
        if self.root_node == None: 
            raise EmptyTreeError("Cannot find min in empty Tree")
        run = self.root_node 
        while run.left is not None: 
            run = run.left 
        return run.data 

    
    def max(self) -> any:
        '''
        @self: calling BST object 
        Returns a max data value held by any node in BST @self 
        Raises bst_empty exception if the tree is empty 
        '''
        if self.root_node == None: 
            raise EmptyTreeError("Cannot find min in empty Tree")
        run = self.root_node 
        while run.right is not None: 
            run = run.left 
        return run.data 


    def inorder_predecessor(self, e_data: any) -> any: 
        '''
        @self: calling BST object 
        @e_data: existing data value in BST 
        @return: data value in a predecessor node of the node 
        containing @e_data while traversing BST @self using 
        inorder sequence 
        @exceptions: 
        invald_data: if e_data is not found 
        inorder_no_predecessor: if @e_data is the min data in BST @self 
        '''
        e_node = bst.search_node(self.root_node, e_data) 
        if e_node is None: 
            raise ValueError("bad value for existing data")
        pred_node = bst.inorder_predecessor_node(e_node)
        if pred_node is not None: 
            return pred_node.data 
        else: 
            raise TreeNoPredecessor("Max data has no predecessor")



    def inorder_successor(self, e_data: any) -> any: 
        '''
        @self: calling BST object 
        @e_data: existing data value in BST 
        @return: data value in a successor node of the node 
        containing @e_data while traversing BST @self using 
        inorder sequence 
        @exceptions: 
        invald_data: if e_data is not found 
        inorder_no_successor: if @e_data is the max data in BST @self 
        '''
        e_node = bst.search_node(self.root_node, e_data) 
        if e_node is None: 
            raise ValueError("bad value for existing data")
        succ_node = bst.inorder_successor_node(e_node)
        if succ_node is not None: 
            return succ_node.data 
        else: 
            raise TreeNoSuccessor("Max data has no successor")


def main(): 
    T = bst() 
    print("T.root_node:", T.root_node)
    print("T.nr_elements:", T.nr_elements)

    L = [100, 50, 150, 25, 75, 125, 200, 
            15, 17, 130, 135]  
    
    for x in L: 
        T.insert(x)

    print("MANUAL TRAVERSAL:")
    v = T.root_node 
    print(v.data)       # 100 
    print(v.left.data)  # 50 
    print(v.right.data) # 150 
    print(v.left.left.data) # 25 
    print(v.left.right.data) # 75 
    print(v.right.left.data) # 125 
    print(v.right.right.data) # 200 
    print(v.left.left.left.data) # 15 
    print(v.left.left.left.right.data) # 17 
    print(v.right.left.right.data) # 130 
    print(v.right.left.right.right.data)# 135 

    print("INORDER:")
    T.inorder()

    print("PREORDER:")
    T.preorder()

    print("POSTORDER:")
    T.postorder()

    for x in L: 
        bRet = T.search(x)
        if bRet == True: 
            print(f'{x} is present in BST')
    
    nL = [-100, -200, 5000, 1000, 3565, 34635]
    for x in nL: 
        bRet = T.search(x)
        if bRet == False: 
            print(f'{x} is not preset in BST')

    T = bst() 
    L = [100, 50, 150, 40, 60, 200, 55, 70, 175, 250, 
        80, 160, 180, 225, 275, 158, 210, 155, 156]
    for x in L: 
        T.insert(x) 

    print("Printing new tree in inorder sequence:")
    T.inorder()

    succ_data = T.inorder_successor(150)
    print("SUCC of 150:", succ_data)

    succ_data = T.inorder_successor(80)
    print("SUCC of 80:", succ_data) 

    try: 
        for x in sorted(L): 
            succ_data = T.inorder_successor(x) 
            print(f'SUCC({x}) == {succ_data}')
    except TreeNoSuccessor: 
            print(f"Max data:{x} has no successor")

    try: 
        for x in sorted(L, reverse=True):
            pred_data = T.inorder_predecessor(x) 
            print(f'PRED({x}) == {pred_data}')
    except TreeNoPredecessor: 
            print(f"Max data:{x} has no predecessor")


    print("LEVEL ORDER:")
    T.level_order()

    from random import shuffle 
    LC = L.copy()
    shuffle(LC)
    for x in LC: 
        print(f"Removing {x} from T")
        T.remove(x)
        
   
main()