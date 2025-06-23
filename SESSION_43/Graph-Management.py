class hnode:
    def __init__(self, v = None):
        self.v = v
        self.next = None
        self.prev = None

class hlist:
    @staticmethod
    def genericInsert(startNode:hnode, midNode:hnode, endNode:hnode)->None:
        midNode.next = endNode
        midNode.prev = startNode

        endNode.prev = midNode
        startNode.next = midNode

    @staticmethod
    def genericDelete(dNode:hnode):
        dNode.prev.next = dNode.next
        dNode.next.prev = dNode.prev
        del dNode

    def __init__(self):
        self.headNode = hnode(None)
        self.headNode.next = self.headNode
        self.headNode.prev = self.headNode

    def searchNode(self, v:int):
        run = self.headNode.next
        while run != self.headNode:
            if run.v == v:
                return run
            run = run.next
        return None
    
    def insertEnd(self, v:int):
        self.genericInsert(self.headNode.prev, hnode(v), self.headNode)

class vnode:
    def __init__(self, v = None):
        self.v = v
        self.adjList = hlist()

        self.next = None
        self.prev = None

class vlist:
    @staticmethod
    def genericInsert(startNode:vnode, midNode:vnode, endNode:vnode):
        midNode.next = endNode
        midNode.prev = startNode

        startNode.next = midNode
        endNode.prev = midNode

    @staticmethod
    def genericDelete(dNode:vnode):
        dNode.prev.next = dNode.next
        dNode.next.prev = dNode.prev
        del dNode


    def __init__(self):
        self.headNode = vnode(None)
        self.headNode.next = self.headNode
        self.headNode.prev = self.headNode

    def insertEnd(self, v:int):
        self.genericInsert(self.headNode.prev, vnode(v), self.headNode)

    def searchNode(self, v:int)->vnode:
        run = self.headNode.next

        while run != self.headNode:
            if run.v == v:
                return run
            run = run.next
        return None

class graph:
    def __init__(self):
        self.verticalList = vlist()
        self.verticalList.headNode.adjList = None

    def addVertex(self, v:int)->int:
        tmpNode = self.verticalList.searchNode(v)
        if tmpNode != None:
            raise ValueError(f'Vertex v : {v} is already present in the graph')
        
        self.verticalList.insertEnd(v)

    def addEdge(self, vStart:int, vEnd:int):
        vStartNode = self.verticalList.searchNode(vStart)
        if vStartNode == None:
            raise ValueError(f'vStart : {vStart} is not present in the Graph')
        
        vEndNode = self.verticalList.searchNode(vEnd)
        if vEndNode == None:
            raise ValueError(f'vEnd : {vEnd} is not presnet in the Graph')
        
        hInVStart = vStartNode.adjList.searchNode(vEnd)
        hInVEnd = vEndNode.adjList.searchNode(vStart)

        if hInVStart != None and hInVEnd != None:
            raise ValueError(f'Edge between {vStart} and {vEnd} is already exists')
        
        vStartNode.adjList.insertEnd(vEnd)
        vEndNode.adjList.insertEnd(vStart)

    def removeEdge(self, vStart:int, vEnd:int):
        vStartNode = self.verticalList.searchNode(vStart)
        if vStartNode == None:
            raise ValueError(f'vStart : {vStart} is not present in the Graph')
        
        vEndNode = self.verticalList.searchNode(vEnd)
        if vEndNode == None:
            raise ValueError(f'vEnd : {vEnd} is not present in the Graph')
        
        hEndInStart = vStartNode.adjList.searchNode(vEnd)
        if hEndInStart == None:
            raise ValueError(f'There is no edge between {vStart} and {vEnd}')
        
        hStartInEnd = vEndNode.adjList.searchNode(vStart)
        if hStartInEnd == None:
            raise ValueError(f'There is no edge between {vStart} and {vEnd}')
        
        hlist.genericDelete(hEndInStart)
        hlist.genericDelete(hStartInEnd)

    def removeVertex(self, v:int):
        rNode = self.verticalList.searchNode(v)
        if rNode == None:
            raise ValueError(f'Vertex to be removed does not exist : {v}')
        
        hRun = rNode.adjList.headNode.next

        while hRun != rNode.adjList.headNode:
            hRunNext = hRun.next
            hInVList = self.verticalList.searchNode(hRun.v)
            rInhListOfAdjNode = hInVList.adjList.searchNode(v)
            hlist.genericDelete(rInhListOfAdjNode)
            hlist.genericDelete(hRun)
            hRun = hRunNext
        vlist.genericDelete(rNode)


    def printGraph(self):
        vRun = self.verticalList.headNode.next

        while vRun != self.verticalList.headNode:
            print(f'[{vRun.v}] \t <-> \t', end='')

            hRun = vRun.adjList.headNode.next
            while hRun != vRun.adjList.headNode:
                print(f'[{hRun.v}]<->', end='')
                hRun = hRun.next
            print('[END]')
            vRun = vRun.next

g = graph()

for v in range(8):
    g.addVertex(v)

E = [(0,1), (1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,0), (1,6), (6,3), (5,2), (7,2)]

for (vStart, vEnd) in E:
    g.addEdge(vStart, vEnd)

g.printGraph()

g.removeEdge(2,3)
g.removeEdge(5,6)

print('After removing edges \n\n')
g.printGraph()

print('\n\n After removing vertex')
g.removeVertex(2)
g.removeVertex(5)
g.printGraph()