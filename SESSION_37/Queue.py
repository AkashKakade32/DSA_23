import DCL

class queue:
    def __init__(self):
        self.qu = DCL.DoublyCircularLinkedList()

    def insert(self, newData):
        self.qu.insertEnd(newData)

    def remove(self):
        self.qu.popStart()

    def display(self):
        self.qu.showList()

q = queue()

q.insert(10)
q.insert(20)
q.insert(30)
q.insert(40)

q.display()

q.remove()

q.display()

q.remove()

q.display()

q.remove()

q.display()

q.remove()

q.display()

q.remove()

q.display()


