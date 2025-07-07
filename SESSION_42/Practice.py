class vertexNotFoundError(Exception):
    pass

class vertexExistError(Exception):
    pass

class edgeNotFoundError(Exception):
    pass

class edgeExistError(Exception):
    pass




class hnode:
    def __init__(self, v):
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
    def genericDelete(dNode:hnode):
        dNode.prev.next = dNode.next
        dNode.next.prev = dNode.prev

        del dNode

    def __init__(self):
        self.headNode = hnode(None)
        self.headNode.next = self.headNode
        self.headNode.prev = self.headNode

    def insertEnd(self, v:int):
        self.genericInsert(self.headNode.prev, hnode(v), self.headNode)

    def searchNode(self, v:int):
        run = self.headNode.next

        while run != self.headNode:
            if run.v == v:
                return run
            run = run.next
        return None
    

class vnode:
    def __init__(self, v):
        self.v = v
        self.adjList = hlist()

        self.next = None
        self.prev = None

class vlist:

    @staticmethod
    def geneticInsert(startNode:vnode, midNode:vnode, endNode:vnode):
        midNode.next = endNode
        midNode.prev = startNode

        startNode.next = midNode
        endNode.prev = midNode

    @staticmethod
    def genericDelete(dNode:vnode):
        dNode.prev.next = dNode.next
        dNode.next.prev = dNode.prev

        del dNode\

    def __init__(self):
        self.headNode = vnode(None)
        self.headNode.next = self.headNode
        self.headNode.prev = self.headNode

    def insertEnd(self, v:int):
        self.geneticInsert(self.headNode.prev, vnode(v), self.headNode)

    def searchNode(self, v:int):
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
        self.num_vertices = 0
        self.num_edges = 0

    def addVertex(self, v:int):
        tmpNode = self.verticalList.searchNode(v)

        if tmpNode != None:
            raise vertexExistError(f'Vertex {v} is already present in the Graph')
        self.verticalList.insertEnd(v)

    def addEdge(self, vStart:int, vEnd:int):
        vStartNode = self.verticalList.searchNode(vStart)
        if vStartNode == None:
            raise vertexNotFoundError(f'Vertex {vStart} is not found in the graph')
        vEndNode = self.verticalList.searchNode(vEnd)
        if vEndNode == None:
            raise vertexNotFoundError(f'Vertex {vEnd} is not found in the graph')
        
        hInVStart = vStartNode.adjList.searchNode(vEnd)
        hInVEnd = vEndNode.adjList.searchNode(vStart)

        if hInVStart != None and hInVEnd != None:
            raise edgeExistError(f'Edge between {vStart} and {vEnd} already exists')
        
        vStartNode.adjList.insertEnd(vEnd)
        vEndNode.adjList.insertEnd(vStart)

    def removeEdge(self, vStart:int, vEnd:int):
        vStartNode = self.verticalList.searchNode(vStart)
        if vStartNode == None:
            raise vertexNotFoundError(f'{vStart} does not exist')
        
        vEndNode = self.verticalList.searchNode(vEnd)
        if vEndNode == None:
            raise vertexNotFoundError(f'{vEnd} does not exist')
        
        endInVStart = vStartNode.adjList.searchNode(vEnd)
        if endInVStart == None:
            raise edgeNotFoundError(f'There is no edge to remove between {vStart} and {vEnd}')
        
        endInVEnd = vEndNode.adjList.searchNode(vStart)
        if endInVEnd == None:
            raise edgeNotFoundError(f'There is no edge to remove between {vStart} and {vEnd}')
        
        hlist.genericDelete(endInVStart)
        hlist.genericDelete(endInVEnd)

    def removeVertex(self, v:int):
        rNode = self.verticalList.searchNode(v)

        if rNode == None:
            raise vertexNotFoundError(f'Veretx {v} to be remove not found in the Graph')
        
        hRun = rNode.adjList.headNode.next

        while hRun != rNode.adjList.headNode:
            hRunNext = hRun.next

            hInVList = self.verticalList.searchNode(hRun.v)

            rInHList = hInVList.adjList.searchNode(v)

            hlist.genericDelete(rInHList)
            hlist.genericDelete(hRun)

            hRun = hRun.next

        vlist.genericDelete(rNode)
        
    def printGraph(self):
        vRun = self.verticalList.headNode.next

        while vRun != self.verticalList.headNode:
            print(f'{vRun.v}\t<-->\t', end='')
            hRun = vRun.adjList.headNode.next

            while hRun != vRun.adjList.headNode:
                print(f'{hRun.v}<-->', end='')
                hRun = hRun.next
            print('[END]')
            vRun = vRun.next

g = graph()

for v in range(8):
    g.addVertex(v)

E = [(0,1), (1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,0), (1,6), (6,3), (5,2), (7,2)]

for (s,e) in E:
    g.addEdge(s,e)

g.printGraph()

print('\n')

g.removeEdge(0,1)
g.printGraph()

print('\n')

g.removeVertex(2)
g.printGraph()

g.removeVertex(12)