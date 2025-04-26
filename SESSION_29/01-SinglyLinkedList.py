class SNode:
    def __init__(self, initData:int):
        self.data = initData
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.headNode = SNode(None)

    def insertStart(self, newData:int):
        newNode = SNode(newData)
        newNode.next = self.headNode.next
        self.headNode.next = newNode

    def insertEnd(self, newData:int):
        run = self.headNode

        while run.next != None:
            run = run.next

        run.next = SNode(newData)

    def searchNode(self, searchData:int):
        run = self.headNode.next
        prevNode = self.headNode

        while run != None:
            if searchData == run.data:
                return(run, prevNode)
            prevNode = run
            run = run.next
        return(None, None)

    def insertAfter(self, currentData:int, newData:int):
        currentNode, _ = self.searchNode(currentData)

        if currentNode == None:
            raise ValueError("Existing Data not found")

        newNode = SNode(newData)
        newNode.next = currentNode.next
        currentNode.next = newNode

    def insertBefore(self, currentData:int, newData:int):
        _, prevNode = self.searchNode(currentData)

        if prevNode == None:
            raise ValueError("Existing Data not found")

        newNode = SNode(newData)
        newNode.next = prevNode.next
        prevNode.next = newNode

    def removeNode(self, rData:int):
        rNode, prevNode = self.searchNode(rData)

        if rNode == None:
            raise ValueError("Existing data not found")

        prevNode.next = rNode.next
        del(rNode)

    def showList(self):
        run = self.headNode.next
        
        print(f"[START]",end="-->")
        while run != None:
            print(f"{run.data}", end="-->")
            run = run.next
        print("[END]")


L = SinglyLinkedList()

for i in range(1,6):
    L.insertStart(10*i)

for i in range(6, 11):
    L.insertEnd(10*i)

L.showList()

currentNode, prevNode = L.searchNode(50)

print(f"{currentNode.data}, {prevNode.data}")

L.insertAfter(10,600)

L.insertBefore(10, 500)

L.removeNode(10)

L.showList()

