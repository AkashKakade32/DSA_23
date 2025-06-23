import DCL

#import intro

class Stack:
    def __init__(self):
        self.st = DCL.DoublyCircularLinkedList()

    def push(self, newData):
        self.st.insertStart(newData)

    def pop(self):
        if self.isEmpty():
            raise TypeError('Cannot perform operation on empty stack \n')
        self.st.popStart()

    def showStack(self):
        self.st.showList()

    def peek(self):
        if self.isEmpty():
            raise TypeError('Cannot perform operation on empty stack \n')
        return self.st.getStart()

    def isEmpty(self):
        return self.st.isEmpty()


s1 = Stack()

s1.push(10)
s1.push(20)
s1.push(30)

s1.pop()
s1.pop()
s1.pop()

#print(s1.peek())

s1.showStack()


