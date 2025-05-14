class DNode:
    def __init__(self, initData:int):
        self.data = initData
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.headNode = DNode(None)

    def insertStart(self, newData:int):
        newNode = DNode(newData)
        newNode.next = self.headNode.next
        newNode.prev = self.headNode
        if self.headNode.next != None and type(self.headNode.next) == DNode:
            self.headNode.next.prev = newNode
        self.headNode.next = newNode

    def insertEnd(self, newData:int):
        run = self.headNode
        while run.next != None:
            run = run.next
        run.next = DNode(newData)
        run.next.prev = run

    def showList(self):
        run = self.headNode.next
        print("[START]<->", end='')
        while run != None:
            print(f'[{run.data}]<->', end='')
            run = run.next
        print('[END]')

    def searchNode(self, existingData:int):
        run = self.headNode.next
        while run != None:
            if run.data == existingData:
                return run
            run = run.next
        return None

    def insertAfter(self, existingData:int, newData:int):
        existingNode = self.searchNode(existingData)
        if existingNode == None:
            raise ValueError(f'Existing Data not found {existingData}')
        newNode = DNode(newData)
        newNode.next = existingNode.next
        newNode.prev = existingNode
        if existingNode.next != None:
            existingNode.next.prev = newNode
        existingNode.next = newNode

    def insertBefore(self, existingData:int, newData:int):
        existingNode = self.searchNode(existingData)
        if existingNode == None:
            raise ValueError(f'Existing Data not found {existingData}')
        newNode = DNode(newData)
        newNode.next = existingNode
        newNode.prev = existingNode.prev
        existingNode.prev.next = newNode
        existingNode.prev = newNode

L = DoublyLinkedList()

for data in range(1,6):
    L.insertStart(10*data)

for data in range(6,11):
    L.insertEnd(10*data)

L.insertAfter(100,120)
L.insertBefore(50, 1000)

L.showList()
