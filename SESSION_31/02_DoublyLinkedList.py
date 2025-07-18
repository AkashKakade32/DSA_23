class DNode:
    def __init__(self, newData:int):
        self.data = newData
        self.prev = None
        self.next = None

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

        self.headNode.next = rNode.next
        rNode.next.prev = self.headNode

        data = rNode.data

        del rNode

        return data

    def popEnd(self)->int:
        rNode = self.headNode.prev

        self.headNode.prev = rNode.prev
        rNode.prev.next = self.headNode

        data = rNode.data

        del rNode

        return data

    def showList(self):
        run = self.headNode.next
        print('[START]', end='<->')
        while run != self.headNode:
            print(f'[{run.data}]<->',end='')
            run = run.next

        print("[END]")



D1 = DoublyCircularLinkedList()

D1.insertStart(10);
D1.insertStart(20);
D1.insertStart(30);
D1.insertStart(40);

D1.insertEnd(50);
D1.insertEnd(60);

D1.showList()

print(f'Popped data is : {D1.popStart()}')

print(f'Popped data from last is : {D1.popEnd()}')

D1.showList()

