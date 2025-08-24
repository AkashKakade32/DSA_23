class color:
    WHITE = 1
    GRAY = 2
    BLACK = 3

class hNode:
    def __init__(self, v:int):
        self.data = v
        self.next = None
        self.prev = None

class hList:
    @staticmethod
    def genericInsert(startNode:hNode, midNode:hNode, endNode:hNode):
        midNode.next = endNode
        midNode.prev = startNode

        startNode.next = midNode
        endNode.prev = midNode

    @staticmethod
    def genericDelete(rNode:hNode):
        rNode.next.prev = rNode.prev
        rNode.prev.next = rNode.next

        del rNode

    def __init__(self):
        self.headNode = hNode(None)
        self.headNode.next = self.headNode
        self.headNode.prev = self.headNode

    def insertEnd(self, v:int):
        self.genericInsert(self.headNode.prev, hNode(v), self.headNode)

    def searchNode(self, v:int):
        run  = self.headNode.next

        while run != self.headNode:
            if run.data == v:
                return run
            
            run = run.next

        return None


class vNode:
    def __init__(self, v:int):
        self.data = v
        self.adjList = hList()
        self.color = color.WHITE

        self.next = None
        self.prev = None

class vList:
    @staticmethod
    def genericInsert(startNode:vNode, midNode:vNode, endNode:vNode):
        midNode.next = endNode
        midNode.prev = startNode

        startNode.next = midNode
        endNode.prev = midNode

    @staticmethod
    def genericDelete(rNode:vNode):
        rNode.prev.next = rNode.next
        rNode.next.prev = rNode.prev

        del rNode


    def __init__(self):
        self.headNode = vNode(None)
        self.headNode.next = self.headNode
        self.headNode.prev = self.headNode

    def insertEnd(self, v:int):
        self.genericInsert(self.headNode.prev, vNode(v), self.headNode)

    def searchNode(self, v:int):
        run  = self.headNode.next

        while run != self.headNode:
            if run.data == v:
                return run
            
            run = run.next

        return None

class graph:
    def __init__(self):
        self.verticalList = vList()
        self.verticalList.headNode.adjList = None
