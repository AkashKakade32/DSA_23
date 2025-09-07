class hnode:
    def __init__(self, v:int, w:int):
        self.v = v
        self.w = w

        self.next = None
        self.prev = None

class hlist:
    @staticmethod
    def genericInsert(startNode, midNode, endNode):
        midNode.next = endNode
        midNode.prev = startNode

        startNode.next = midNode
        endNode.prev = midNode

    @staticmethod
    def searchNode(headNode, v:int):
        run = headNode.next

        while run != headNode:
            if run.v == v:
                return run
            run = run.next
        return None

    def __init__(self):
        self.headNode = hnode(-1,-1)
        self.headNode.next = self.headNode
        self.headNode.prev = self.headNode

    def insertEnd(self, v:int, w:int):
        hlist.genericInsert(self.headNode.prev, hnode(v,w), self.headNode)


class vnode:
    def __init__(self, v:int):
        self.v = v
        self.adjList = hlist()

        self.next = None
        self.prev = None

class vlist:
    @staticmethod
    def genericInsert(startNode, midNode, endNode):
        midNode.next = endNode
        midNode.prev = startNode

        startNode.next = midNode
        endNode.prev = midNode

    @staticmethod
    def searchNode(headNode, v:int):
        run = headNode.next

        while run != headNode:
            if run.v == v:
                return run
            run = run.next

        return None
    
    def __init__()
