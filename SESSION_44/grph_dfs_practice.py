class hnode:
    def __init__(self, v:int):
        self.v = v
        self.next = None
        self.prev = None

class hlist:
    @staticmethod
    def genericInsert(startNode:hnode, midNode:hnode, endNode:hnode):
        midNode.next = endNode
        midNode.prev = startNode

        startNode.next = midNode
        endNode.prev = midNode

    @staticmethod
    def searchNode(headNode:hnode, v:int)->hnode:
        run = headNode.next

        while run != headNode:
            if run.v == v:
                return run
            run = run.next

        return None

    def __init__(self):
        self.headNode = hnode(-1)
        self.headNode.next = self.headNode
        self.headNode.prev = self.headNode

    def insertEnd(self, v:int):
        hlist.genericInsert(self.headNode.prev, hnode(v), self.headNode)

class vnode:
    def __init__(self, v:int):
        self.v = vnode
        self.adjList = hlist()

        self.prev = None
        self.next = None


class vlist:
    @staticmethod
    def genericInsert(startNode:vnode, midNode:vnode, endNode:vnode):
        midNode.next = endNode
        midNode.prev = startNode

        startNode.next = midNode
        startNode.prev = midNode

    @staticmethod
    def searchNode(headNode:vnode, v:int)->vnode:
        run = headNode.next

        while run != headNode:
            if run.v == v:
                return run
            run = run.next
        return None

    def __init__(self):
        self.headNode = vnode(-1)
        self.headNode.next = self.headNode
        self.headNode.prev = self.headNode

    def insertEnd(self, v:int):
        vlist.genericInsert(self.headNode.prev, vnode(v), self.headNode)


class graph:
    def __init__(self):
        self.verticalList = vlist()
        self.verticalList.headNode.adjList = None

    def addVertex(self, v:int):
        self.verticalList.insertEnd(v)

    def addEdge(self, startData:int, endData:int):
        vNodeStart = vlist.searchNode(self.verticalList.headNode, startData)
        if vNodeStart == None:
            print('vNodeStart is not in the Graph')

        vNodeEnd = vlist.searchNode(self.verticalList.headNode, endData)
        if vNodeEnd == None:
            print('vNodeEnd is not in the Graph')


        vNodeStart.adjList.insertEnd(endData)
        vNodeEnd.adjList.insertEnd(startData)

    def printGraph(self):
        vRun = self.verticalList.headNode.next

        while vRun != self.verticalList.headNode:
            print(f'[{vRun.v}]\t-->\t', end='')

            hRun = vRun.adjList.headNode.next

            while hRun != vRun.adjList.headNode:
                print(f'[{hRun.v}]-->', end='')
                hRun = hRun.next

            print('[END]')

            vRun = vRun.next





L = [1,2,3,4,5,6]

E = [(1,2), (3,4), (5,6), (2,6), (3,5), (4,2)]

g = graph()

for i in L:
    g.addVertex(i)

#for i,j in E:
    #g.addEdge(i,j)

g.printGraph()
