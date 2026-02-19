import math

class color:
    WHITE = 1
    GRAY = 2
    BLACK = 3

class hnode:
    def __init__(self, v:int, w:int):
        self.v = v
        self.w = w

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
    def search(headNode:hnode, v:int):
        run = headNode.next

        while run != headNode:
            if run.v == v:
                return run
            run = run.next

        return None

    def __init__(self):
        self.headNode = hnode(None, None)
        self.headNode.next = self.headNode
        self.headNode.prev = self.headNode

    def insertEnd(self, v:int, w:int):
        hlist.genericInsert(self.headNode.prev, hnode(v,w), self.headNode)



class vnode:
    def __init__(self, v:int):
        self.v = v
        self.adjList = hlist()
        self.color = color.WHITE
        self.d = 0
        self.predVertex = None

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
    def search(headNode:vnode, v:int):
        run = headNode.next

        while run != headNode:
            if run.v == v:
                return run
            run = run.next

        return None
    
    def __init__(self):
        self.headNode = vnode(None)
        self.headNode.next = self.headNode
        self.headNode.prev = self.headNode

        self.headNode.adjList = None

    def insertEnd(self, v:int):
        vlist.genericInsert(self.headNode.prev, vnode(v), self.headNode)

class graph:
    def __init__(self):
        self.vList = vlist()

    def addVertex(self, v:int):
        self.vList.insertEnd(v)

    def addEdge(self, startData:int, endData:int, weight:int):
        startNode = vlist.search(self.vList.headNode, startData)
        endNode = vlist.search(self.vList.headNode, endData)

        if startNode == None or endNode == None:
            print(f'Graph between {startData} and {endData} does not exist')

        startNode.adjList.insertEnd(endData, weight)
        endNode.adjList.insertEnd(startData, weight)

    def printGraph(self):
        vRun = self.vList.headNode.next

        while vRun != self.vList.headNode:
            print(f'[{vRun.v}] \t-->\t', end='')

            hRun = vRun.adjList.headNode.next

            while hRun != vRun.adjList.headNode:
                print(f'[{hRun.v}]-->', end='')
                hRun = hRun.next

            print('[END]')

            vRun = vRun.next

    def dfs(self):
        def reset():
            run = self.vList.headNode.next

            while run != self.vList.headNode:
                run.color = color.WHITE
                run = run.next
            print(f'All Nodes are reset for DFS()')

        def dfsVisit(self, u:vnode):
            print(f'[{u.v}]-->', end='')

            u.color = color.GRAY

            hRun = u.adjList.headNode.next

            while hRun != u.adjList.headNode:
                vInH = vlist.search(self.vList.headNode, hRun.v)

                if vInH.color == color.WHITE:
                    dfsVisit(self, vInH)

                hRun = hRun.next

            u.color = color.BLACK

        reset()

        vRun = self.vList.headNode.next
        
        print('[DFS START]-->', end='')
        while vRun != self.vList.headNode:
            if vRun.color == color.WHITE:
                dfsVisit(self, vRun)
            vRun = vRun.next
        print('[END]')


    def bfs(self, v:int):
        def reset():
            run = self.vList.headNode.next

            while run != self.vList.headNode:
                run.color = color.WHITE
                run = run.next

            print('All Nodes are reset for bfs()')

        reset()

        vNode = vlist.search(self.vList.headNode, v)

        if vNode == None:
            print(f'Vertex {v} is not present in the Graph')
            return
        
        print('[START BFS]-->', end='')

        Q = []
        Q.append(vNode)

        while len(Q) != 0:
            u = Q.pop(0)
            u.color = color.BLACK
            print(f'[{u.v}]-->', end='')

            hRun = u.adjList.headNode.next

            while hRun != u.adjList.headNode:
                vInH = vlist.search(self.vList.headNode, hRun.v)

                if vInH.color == color.WHITE and vInH not in Q:
                    Q.append(vInH)
                hRun = hRun.next

        print('[END}')

    def djkstra(self, v:int):
        vNodeS = vlist.search(self.vList.headNode, v)

        if vNodeS == None:
            print(f'Vertex {v} is not present in the graph')
            return
        
        def initializeSingleSource(vNodeS:vnode):
            run = self.vList.headNode.next

            while run != self.vList.headNode:
                run.d = math.inf
                run.predVertex = None
                run = run.next

            vNodeS.d = 0

        def relax(u:vnode, v:vnode, w:int):
            if v.d > u.d + w:
                v.d = u.d + w
                v.predVertex = u

        def extractMin(Q:list) -> vnode:
            minD = Q[0].d
            minIndex = 0

            for i in range(1, len(Q)):
                if Q[i].d < minD:
                    minD = Q[i].d
                    minIndex = i

            u = Q.pop(minIndex)

            return u

        def printShortestPath(v:int, destNode:vnode):
            L = []

            run = destNode

            while run != None:
                L.append(run.v)
                run = run.predVertex

            L.reverse()

            print(f'Shortest Path between {v} and {destNode.v} : ')
            print('[START]-->', end='')
            for s in L:
                print(f'[{s}]-->', end='')
            print('[END]')

        initializeSingleSource(vNodeS)

        Q = []

        vRun = self.vList.headNode.next

        while vRun != self.vList.headNode:
            Q.append(vRun)
            vRun = vRun.next

        while len(Q) != 0:
            u = extractMin(Q)

            hRun = u.adjList.headNode.next

            while hRun != u.adjList.headNode:
                w = hRun.w

                vInH = vlist.search(self.vList.headNode, hRun.v)

                relax(u, vInH, w)

                hRun = hRun.next

        vRun = self.vList.headNode.next

        while vRun != self.vList.headNode:
            printShortestPath(v, vRun)
            vRun = vRun.next






g = graph()

for i in range(1,7):
    g.addVertex(i)

L = [(1,2,10), (1,4,2), (1,6,3), (2,3,6), (3,4,1), (4,5,7), (5,6,4)]

for i,j,k in L:
    g.addEdge(i,j,k)

g.printGraph()

g.dfs()

g.bfs(1)

for i in range(1,7):
    print(f'---------- Printing All Shortest Path for {i} ----------')
    g.djkstra(i)
    print('---------- [END] ----------')

