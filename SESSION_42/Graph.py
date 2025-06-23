class hnode:
    def __init__(self, v):
        self.v = v
        self.next = None
        self.prev = None

class hlist:
    def __init__(self):
        self.headNode = hnode(None)
        self.headNode.next = self.headNode
        self.headNode.prev = self.headNode

class vnode:
    def __init__(self, v = None):
        self.v = v
        self.adjlist = hlist()

        self.prev = None
        self.next = None


class vlist:
    def __init__(self):
        self.headNode = vnode()
        self.headNode.next = self.headNode
        self.headNode.prev = self.headNode


class graph:
    def __init__(self):
        self.verticalList = vlist()
        self.verticalList.adjlist = None


g1 = graph()
