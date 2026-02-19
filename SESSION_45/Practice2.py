class hnode:
    def __init__(self, v: int, w: int):
        self.v = v
        self.w = w
        self.next = None
        self.prev = None


class hlist:
    def __init__(self):
        self.headNode = hnode(None, None)
        self.headNode.next = self.headNode
        self.headNode.prev = self.headNode

    @staticmethod
    def staticInsert(prevNode: hnode, midNode: hnode, endNode: hnode):
        midNode.next = endNode
        midNode.prev = prevNode

        prevNode.next = midNode
        endNode.prev = midNode

    @staticmethod
    def genericSearch(headNode: hnode, v: int):
        run = headNode.next

        while run != headNode:
            if run.v == v:
                return run
            run = run.next

    def insertEnd(self, v: int, w: int):
        hlist.staticInsert(self.headNode.prev, hnode(v, w), self.headNode)
