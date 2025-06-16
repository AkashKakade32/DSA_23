'''
@Author : Akash Avinash Kakade

'''

#def generic_exception_handler(trace=false):
#from sys import exc_info


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

    def showList(self):
        run = self.headNode.next
        
        print('[START]<->',end='')
        while run != self.headNode:
            print(f'[{run.data}]<->',end='')
            run = run.next
        print('[END]')



D1 = DoublyCircularLinkedList()

for i in range(1,6):
    D1.insertStart(10*i)

for i in range(6,11):
    D1.insertEnd(10*i)

D1.showList()
