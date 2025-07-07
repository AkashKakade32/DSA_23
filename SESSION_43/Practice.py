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
        rNode.prev.next = rNode.next
        rNode.next.prev = rNode.prev

        del rNode


    def __init__(self):
        self.headNode = hNode(None)
        self.headNode.next = self.headNode
        self.headNode.prev = self.headNode

    def insertEnd(self, v:int):
        self.genericInsert(self.headNode.prev, hNode(v), self.headNode)

    def searchNode(self, searchData:int):
        run = self.headNode.next

        while run != self.headNode:
            if run.data == searchData:
                return run
            run = run.next
        return None

class vNode:
    def __init__(self, v:int):
        self.data = v
        self.adjList = hList()

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

    def searchNode(self, searchData:int):
        run = self.headNode.next

        while run != self.headNode:
            if run.data == searchData:
                return run
            run = run.next
        return None

class graph:
    def __init__(self):
        self.verticalList = vList()
        self.verticalList.headNode.adjList = None
        self.numberOfVertex = 0
        self.numberOfEdges = 0

    def addVertex(self, v:int):
        vListNode = self.verticalList.searchNode(v)

        if vListNode != None:
            raise ValueError(f'Vertex {v} is alredy present in the Graph')
        
        self.verticalList.insertEnd(v)

        self.numberOfVertex += 1

    def addEdge(self, startData:int, endData:int):
        vListStartNode = self.verticalList.searchNode(startData)
        if vListStartNode == None:
            raise ValueError(f'Vertex {startData} is not present in the Graph')
        
        vListEndNode = self.verticalList.searchNode(endData)
        if vListEndNode == None:
            raise ValueError(f'Vertex {endData} is not present in the Graph')
        
        hListStartNode = vListStartNode.adjList.searchNode(endData)
        if hListStartNode != None:
            raise ValueError(f'Edge Between {startData} and {endData} is alredy present in the Graph')

        hListEndNode = vListEndNode.adjList.searchNode(startData)
        if hListEndNode != None:
            raise ValueError(f'Edge Between {startData} and {endData} is alredy present in the Graph')

        vListStartNode.adjList.insertEnd(endData)
        vListEndNode.adjList.insertEnd(startData)

        self.numberOfEdges += 1

    def printGraph(self):
        print(f'Total Number of Vertices : {self.numberOfVertex} || Total Number of Edges : {self.numberOfEdges}')
        print("\n")
        
        vListNode = self.verticalList.headNode.next

        while vListNode != self.verticalList.headNode:
            hListNode = vListNode.adjList.headNode.next
            print(f'[{vListNode.data}]\t-->\t', end='')
            while hListNode != vListNode.adjList.headNode:
                print(f'[{hListNode.data}]-->', end='')
                hListNode = hListNode.next
            print('[END]')
            vListNode = vListNode.next

    def removeVertex(self, v:int):
        rNode = self.verticalList.searchNode(v)

        if rNode == None:
            raise ValueError(f'Vertex {v} to be removed is not present in the Graph')
        
        hRun = rNode.adjList.headNode.next

        while hRun != rNode.adjList.headNode:
            hRunNext = hRun.next
            rInVList = self.verticalList.searchNode(hRun.data)
            rhInVListAdj = rInVList.adjList.searchNode(v)
            hList.genericDelete(rhInVListAdj)
            hList.genericDelete(hRun)
            self.numberOfEdges -= 1
            hRun = hRunNext

        vList.genericDelete(rNode)
        self.numberOfVertex -= 1


g = graph()

for i in range(8):
    g.addVertex(i)

E = [(0,1), (1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,0), (1,6), (6,3), (5,2), (7,2)]

for (i,j) in E:
    g.addEdge(i,j)

g.printGraph()

g.removeVertex(1)

print('Priniting a graph after remove vertex')

g.printGraph()




