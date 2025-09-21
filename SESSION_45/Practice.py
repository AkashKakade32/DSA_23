class color:
    WHITE = 1
    GRAY = 2
    BLACK = 3


class hnode:
    def __init__(self, v, w):
        self.v = v
        self.w = w
        self.next = None
        self.prev = None


class hlist:
    @staticmethod
    def genericInsert(startNode, midNode, endNode):
        midNode.prev = startNode
        midNode.next = endNode

        startNode.next = midNode
        endNode.prev = midNode

    @staticmethod
    def searchNode(headNode, v):
        run = headNode.next

        while run != headNode:
            if run.v == v:
                return run
            run = run.next

        return None

    def __init__(self):
        self.headNode = hnode(-1, -1)
        self.headNode.next = self.headNode
        self.headNode.prev = self.headNode

    def insertEnd(self, v, w):
        hlist.genericInsert(self.headNode.prev, hnode(v, w), self.headNode)


class vnode:
    def __init__(self, v):
        self.v = v
        self.adjList = hlist()
        self.color = color.WHITE

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
    def searchNode(headNode, v):
        run = headNode.next

        while run != headNode:
            if run.v == v:
                return run
            run = run.next

        return None

    def __init__(self):
        self.headNode = vnode(-1)
        self.headNode.adjList = None

        self.headNode.next = self.headNode
        self.headNode.prev = self.headNode

    def insertEnd(self, v):
        vlist.genericInsert(self.headNode.prev, vnode(v), self.headNode)


class graph:
    def __init__(self):
        self.verticalList = vlist()

    def addVertex(self, v):
        self.verticalList.insertEnd(v)

    def addEdge(self, startData, endData, w):
        startNode = vlist.searchNode(self.verticalList.headNode, startData)
        endNode = vlist.searchNode(self.verticalList.headNode, endData)

        startNode.adjList.insertEnd(endData, w)
        endNode.adjList.insertEnd(startData, w)

    def printGraph(self):
        vRun = self.verticalList.headNode.next

        while vRun != self.verticalList.headNode:
            print(f"[{vRun.v}]\t-->\t", end="")

            hRun = vRun.adjList.headNode.next

            while hRun != vRun.adjList.headNode:
                print(f"[{hRun.v}](Marks = {hRun.w})-->", end="")

                hRun = hRun.next

            print("[END]")

            vRun = vRun.next

    def dfs(self):
        def reset(headNode):
            run = headNode.next

            while run != headNode:
                run.color = color.WHITE
                run = run.next

        def dfsVisit(self, u: vnode):
            print(f"[{u.v}]-->", end="")

            u.color = color.GRAY

            hRun = u.adjList.headNode.next

            while hRun != u.adjList.headNode:
                vHRun = vlist.searchNode(self.verticalList.headNode, hRun.v)

                if vHRun.color == color.WHITE:
                    dfsVisit(self, vHRun)

                hRun = hRun.next

            u.color = color.BLACK

        reset(self.verticalList.headNode)

        vRun = self.verticalList.headNode.next

        print("[START]-->", end="")
        while vRun != self.verticalList.headNode:
            if vRun.color == color.WHITE:
                dfsVisit(self, vRun)
            vRun = vRun.next

        print("[END]")


L = ['English', 'Maths', 'Comp', 'Hindi', 'Marathi', 'Micro']

g = graph()

for i in L:
    g.addVertex(i)

E = [
    ('English', 'Maths', 3),
    ('English', 'Marathi', 7),
    ('English', 'Hindi', 6),
    ('Maths', 'Micro', 5),
    ('Maths', 'Marathi', 11),
    ('Maths', 'Hindi', 8),
    ('Comp', 'Micro', 5),
    ('Comp', 'English', 8),
    ('Hindi', 'Micro', 7),
    ('Marathi', 'Micro', 2),
]

for i, j, k in E:
    g.addEdge(i, j, k)

g.printGraph()

print()

g.dfs()
