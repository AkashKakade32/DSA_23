class bstNode:
    def __init__(self, newData:int):
        self.data = newData
        self.left = None
        self.right = None
        self.parent = None

class bstTree:

    @staticmethod
    def _inorder(r:bstNode):
        if r != None:
            bstTree._inorder(r.left)
            print(f'[{r.data}]', end='->')
            bstTree._inorder(r.right)

    def __init__(self):
        self.root = None

    def insertNode(self, newData:int):
        newNode = bstNode(newData)

        if self.root == None:
            self.root = newNode
            return None
        
        run = self.root

        while True:
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

    def inorder(self):
        print('[START]', end='->')
        bstTree._inorder(self.root)
        print('[END]')

    def searchNode(self, searchData:int)->bstNode:
        run = self.root

        while run != None:
            if run.data == searchData:
                return run
            elif searchData < run.data:
                run = run.left
            elif searchData > run.data:
                run = run.right

        return None
    
    def inorderSuccessor(self, searchData:int)->bstNode:
        currentNode = self.searchNode(searchData)

        if currentNode.right != None:
            run = currentNode.right
            while run.left != None:
                run = run.left
            return run
        
        x = currentNode
        y = currentNode.parent

        while y != None and x == y.right:
            x = y
            y = y.parent
        return y
    
    def remove(self, searchData:int):
        rNode = self.searchNode(searchData)

        if rNode.left == None:
            if rNode.parent == None:
                self.root = rNode.right
            elif rNode == rNode.parent.left:
                rNode.parent.left = rNode.right
            else:
                rNode.parent.right = rNode.right
            
            if rNode.right != None:
                rNode.right.parent = rNode.parent

        elif rNode.right == None:
            if rNode.parent == None:
                self.root = rNode.left
            elif rNode == rNode.parent.left:
                rNode.parent.left = rNode.left
            else:
                rNode.parent.right = rNode.left
            rNode.left.parent = rNode.parent

        elif rNode.right != None and rNode.left != None:
            replaceNode = rNode.right

            while replaceNode.left != None:
                replaceNode = replaceNode.left

            if replaceNode != rNode.right:
                replaceNode.parent.left = replaceNode.right
                if replaceNode.right != None:
                    replaceNode.right.parent = replaceNode.parent
                replaceNode.right = rNode.right
                replaceNode.right.parent = replaceNode

            replaceNode.left = rNode.left
            replaceNode.left.parent = replaceNode

            if rNode.parent == None:
                self.root = replaceNode
            elif rNode == rNode.parent.left:
                rNode.parent.left = replaceNode
            else:
                rNode.parent.right = replaceNode

            replaceNode.parent = rNode.parent
            


b = bstTree()

L = [100, 50, 150, 25, 75, 125, 200, 
            15, 17, 130, 135]  
    
for x in L: 
    b.insertNode(x)

b.inorder()

print()

a = b.searchNode(50)
print(f'{a.data}')

succ = b.inorderSuccessor(50)

print(f'Inorder Successor : {succ.data}')

for x in L: 
    b.remove(x)

b.inorder()