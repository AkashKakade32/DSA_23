class bstNode:
    def __init__(self, newData:any):
        self.data = newData
        self.right = None
        self.left = None
        self.parent = None


class binaryTree:

    #Static Methods Declarations

    @staticmethod
    def _inorderTraversal(tNode:bstNode):
        if tNode != None:
            binaryTree._inorderTraversal(tNode.left)
            print(f'[{tNode.data}]', end='->')
            binaryTree._inorderTraversal(tNode.right)

    @staticmethod
    def _preorderTraversal(tNode:bstNode):
        if tNode != None:
            print(f'[{tNode.data}]', end='->')
            binaryTree._preorderTraversal(tNode.left)
            binaryTree._preorderTraversal(tNode.right)

    @staticmethod
    def _postorderTraversal(tNode:bstNode):
        if tNode != None:
            binaryTree._postorderTraversal(tNode.left)
            binaryTree._postorderTraversal(tNode.right)
            print(f'[{tNode.data}]', end='->')

    @staticmethod
    def _searchNode(tNode:bstNode, searchData:any) -> bstNode:
        run = tNode

        while run != None:
            if run.data == searchData:
                break
            elif searchData < run.data:
                run = run.left
            else:
                run = run.right
        return run


    def __init__(self):
        self.rootNode = None

    def insertNode(self, newData:int):
        newNode = bstNode(newData)

        if self.rootNode == None:
            self.rootNode = newNode
            return None
        
        run = self.rootNode

        while(True):
            if newData <= run.data:
                if run.left == None:
                    run.left = newNode
                    newNode.parent = run
                    break
                else:
                    run = run.left
            else:
                if run.right == None:
                    run.right = newNode
                    newNode.parent = run
                    break
                else:
                    run = run.right

    
    def inorderTraversal(self):
        print('[START]', end='->')
        binaryTree._inorderTraversal(self.rootNode)
        print('[END]')

    def preorderTraversal(self):
        print('[START]', end='->')
        binaryTree._preorderTraversal(self.rootNode)
        print('[END]')

    def postorderTraversal(self):
        print('[START]', end='->')
        binaryTree._postorderTraversal(self.rootNode)
        print('[END]')

    def searchNode(self, searchData):
        z = binaryTree._searchNode(self.rootNode, searchData)
        print(f'Node is : {z.data} | Node.right : {z.right} | Node.left : {z.left.data}')

    def inorderSuccessor(self, searchData:int)->bstNode:
        z = binaryTree._searchNode(self.rootNode, searchData)

        if z.right != None:
            run = z.right

            while run.left != None:
                run = run.left
            return run
        
        x = z
        y = z.parent

        while y != None and x == y.right:
            x = y
            y = y.parent
        return y
    

    def inorderPredecessor(self, searchData:int)->bstNode:
        z = binaryTree._searchNode(self.rootNode, searchData)

        if z.left != None:
            run = z.left

            while run.right != None:
                run = run.right
            return run
        
        x = z
        y = z.parent

        while y != None and x == y.left:
            x = y
            y = y.parent
        return y
    
    def removeNode(self, rData:int):
        z = binaryTree._searchNode(self.rootNode, rData)

        #Case 1 : If z.left is none(z.right may be none or may not be none)
        if z.left == None:

            #Case a : To check if z is root node
            if z.parent == None:
                self.rootNode = z.right
            
            #Case b : To check if z is left node of z.parent
            elif z == z.parent.left:
                z.parent.left = z.right

            #Case c : To check if z is right node of z.parent
            else:
                z.parent.right = z.right
            
            #Important to assign parent to the new node
            if z.right != None:
                z.right.parent = z.parent
        
        #Case 2 : If z.left is NOT NONE and z.right is none
        elif z.right == None:

            #Case a : To check if z is root node
            if z.parent == None:
                self.rootNode = z.left
            
            #Case b : To check if z is left node of z.parent
            elif z == z.parent.left:
                z.parent.left = z.left

            #Case c : To check if z is right node of z.parent
            else:
                z.parent.right = z.left

            #Important to assign the parent to the new node
            z.left.parent = z.parent

        #Case 3 : If zleft is NOT NONE and z.right is NOT NONE
        elif z.right != None and z.left != None:
            y = self.inorderSuccessor(rData)

            if y is not z.right:

                y.parent.left = y.right
                if y.right != None:
                    y.right.parent = y.parent

                y.right = z.right
                y.right.parent = y

            y.left = z.left
            y.left.parent = y

            if z.parent == None:
                self.rootNode = y
            elif z == z.parent.left:
                z.parent.left = y
            else:
                z.parent.right = y

            y.parent = z.parent

            del z


b1 = binaryTree()

L = [100, 50, 25, 75, 65, 60, 72, 150, 200, 175, 160, 250, 225, 220, 215, 218, 217, 300]

for i in L:
    b1.insertNode(i)

b1.inorderTraversal()

b1.preorderTraversal()

b1.postorderTraversal()

tNode = b1.inorderSuccessor(100)
tNode2 = b1.inorderPredecessor(100)

print(f'Inorder Successor : {tNode.data} | Inorder Predessor : {tNode2.data}')

for i in L:
    b1.removeNode(i)

b1.inorderTraversal()

