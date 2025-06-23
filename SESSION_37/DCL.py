class DNode:
    def __init__(self, newData:int):
        self.data = newData
        self.next = None
        self.prev = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.headNode = DNode(None)
        self.headNode.next = self.headNode
        self.headNode.prev = self.headNode

    def insertStart(self, newData:int):
        newNode = DNode(newData)

        newNode.next = self.headNode.next
        newNode.prev = self.headNode

        self.headNode.next.prev = newNode
        self.headNode.next = newNode

    def insertEnd(self, newData:int):
        newNode = DNode(newData)

        newNode.next = self.headNode
        newNode.prev = self.headNode.prev

        self.headNode.prev.next = newNode
        self.headNode.prev = newNode

    def popStart(self)->int:
        rNode = self.headNode.next

        rNode.prev.next = rNode.next
        rNode.next.prev = rNode.prev

        data = rNode.data

        del rNode

        return data

    def popEnd(self)->int:
        rNode = self.headNode.prev

        self.headNode.prev = rNode.prev
        rNode.prev.next = rNode.next

        data = rNode.data

        del rNode

        return data

    def getStart(self)->int:
        return self.headNode.next.data

    def getEnd(self)->int:
        return self.headNode.prev.data

    def isEmpty(self)->bool:
        return self.headNode.next == self.headNode

    
    def showList(self):
        run = self.headNode.next

        print('[START]', end='<->')
        while run != self.headNode:
            print(f'[{run.data}]', end='<->')
            run = run.next
        print('[END]')
    
 
