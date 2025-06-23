class hnode:
    def __init__(self, v = None):
        self.v = v
        self.next = None
        self.prev = None
        print('We are in hnode')

class hlist:
    def __init__(self):
        self.headNode = hnode()
        self.headNode.next = self.headNode
        self.headNode.prev = self.headNode
        print('We are in hlist')

class vnode:
    def __init__(self, v = None):
        self.v = v
        self.adjList = hlist()

        self.next = None
        self.prev = None

        print('We are in vnode')

class vlist:
    def __init__(self):
        self.headNode = vnode()
        self.headNode.next = None
        self.headNode.prev = None
        print('We are in vlist')

class graph:
    def __init__(self):
        self.verticalList = vlist()
        self.verticalList.headNode.adjList = None
        print('We are in graph')


g = graph()