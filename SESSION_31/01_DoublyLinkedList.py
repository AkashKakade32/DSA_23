'''
@Author: Akash Kakade
@Date: 19th April 2025
@Goal: To implement singly linked list of integers
'''

def generic_exception_handler(trace = False):
    from sys import exc_info
    excName, excData, excTb = exc_info()
    print(excName, excData, sep=":", flush=True)
    if trace == True:
        from traceback import print_tb
        print_tb(excTb)

class DNode:
    '''
    This class implements a node for singly linked list and 
    singly circular list
    '''

    def __init__(self, initData:int):
        '''
        @Input:
            @initData: Integer to be stored in newly allocated node
        Constructor creates two attributes ina newly allocated node
        viz. i) data : initialized by local variable 'initData'
        ii)next: initialized to None. This is a self reference to the 
        next in sequence node in a collection
        '''

        if type(initData) != int and initData != None:
            raise TypeError(f"{initData} is not of type int")
        self.data = initData
        self.prev = None
        self.next = None

class DoublyLinkedList:
    '''
    This class implements singly linked list ADT
    '''

    def __init__(self):
        '''
        An attribute named 'head node' will be created in a newly allocated object
        of class SinglyLinkedList. The attribute name will be assigned to a newly allocated dummy node
        object of class SNode.
        '''

        self.headNode = DNode(None)

    def insertStart(self, newData:int):
        '''
        @Input: 
            @newData: new data to be insert at the starting position of the 
            linked list newData will be encapsulated in a new SNode and newly allocated
            SNode object will be positioned at the beginning after the linked list
        '''

        #Logic
        startNode = self.headNode
        endNode = self.headNode.next
        midNode = DNode(newData)
        midNode.next = endNode
        midNode.prev = startNode
        startNode.next = midNode
        if endNode != None and type(endNode) == DNode:
            endNode.prev = midNode



    def insertEnd(self, newData:int):
        run = self.headNode
        while run.next != None:
            run = run.next
        run.next = DNode(newData)
        run.next.prev = run
        

    def showList(self):
        '''
        Display the data members of all nodes except the head node
        '''
        print("[START]<-->", end="")
        run = self.headNode.next
        while run != None:
            print(f"{run.data}<-->", end="")
            run = run.next
        print("[END]")
        

    def searchNode(self, searchData:int):
        '''
        @input:
            @searchData: data value to be searched.
        returns the node containing first occurance of searchData
        and the node previous to it. Returns none if searchData
        is not present
        '''
        run = self.headNode.next
        while run != None:
            if run.data == searchData:
                return run
            run = run.next
        return None

    
    def insertAfter(self, existingData:int, newData:int):
        '''
        @input:
            @existingData: data value which is supposed to be present
            in the list.
            @newData: data value must be inserted after the first occurance
            of @existingData
            a) Inserts a newly allocated node containig @newData after the
            node containig the first occurance of existingData
            b) Raise an value error if the existingData is not present in the list
        '''

        existingNode = self.searchNode(existingData)
        if existingNode == None:
            raise ValueError(f"Invalid Existing data: {existingData}")
        newNode = DNode(newData)
        newNode.next = existingNode.next
        newNode.prev = existingNode
        if existingNode.next != None:
            existingNode.next.prev = newNode
        existingNode.next = newNode

        

    def insertBefore(self, existingData:int, newData:int):
        '''
        @input:
            @existingData: data value which is supposed to be present
            in the list.
            @newData: data value must be inserted before the first occurance
            of @existingData
            a) Inserts a newly allocated node containig @newData before the
            node containig the first occurance of existingData
            b) Raise an value error if the existingData is not present in the list
        '''

        existingNode = self.searchNode(existingData)
        if existingNode == None:
            raise ValueError(f"Invalid Existing data: {existingData}")
        newNode = DNode(newData)
        newNode.next = existingNode
        newNode.prev = existingNode.prev
        existingNode.prev.next = newNode
        existingNode.prev = newNode

        

    def getStart(self)->int:
        '''
        a) Returns data value in the first node with data without removing the first node.
        b) Raise value error if the list is empty
        '''
        if self.isEmpty():
            raise ValueError("Cannot getStart() of the empty list")
        return self.headNode.next.data
       
    
    def getEnd(self)->int:
        '''
        a) Returns data value in the first node with data without removing the last node.
        b) Raise value error if the list is empty
        '''
        if self.isEmpty():
            raise ValueError("Cannot getEnd() of the empty list")
        run = self.headNode
        while run.next != None:
            run = run.next
        return run.data
       
    
    def popStart(self)->int:
        '''
        a) Remove the first node with data and returns the data value in int
        b) Raise value error if the list is empty
        '''
        if self.isEmpty():
            raise ValueError("Cannot popStart() of the empty list")
        firstNodeWithData = self.headNode.next
        data = firstNodeWithData.data
        firstNodeWithData.prev.next = firstNodeWithData.next
        if firstNodeWithData.next != None:
            firstNodeWithData.next.prev = firstNodeWithData.prev
        del firstNodeWithData
        return data
    
    def popEnd(self)->int:
        '''
        a) Remove the last node with data and returns the data value in int
        b) Raise value error if the list is empty
        '''
        if self.isEmpty():
            raise ValueError("Cannot popEnd() of the empty list")
        run = self.headNode
        while run.next != None:
            run = run.next
        data = run.data
        run.prev.next = None
        del run
        return data
    
    def removeStart(self):
        '''
        a) Remove the first node with data in the list
        b) Raise value error if the list is empty
        '''
        firstNodeWithData = self.headNode.next
        firstNodeWithData.prev.next = firstNodeWithData.next
        if firstNodeWithData.next != None:
            firstNodeWithData.next.prev = firstNodeWithData.prev
        del firstNodeWithData

    def removeEnd(self):
        '''
        a) Remove the last node with data in the list
        b) Raise value error if the list is empty
        '''
        if self.isEmpty():
            raise ValueError("Cannot popEnd() of the empty list")
        run = self.headNode
        while run.next != None:
            run = run.next
        run.prev.next = None
        del run

    def removeData(self, rData:int):
        '''
        @input: 
            @rData: Data value whose first occurance within linked list must be removed
            raise value error if the @rData does not exist
        '''
        rNode = self.searchNode(rData)
        if rNode == None:
            raise ValueError(f"Invalid search data {rData}")
        rNode.prev.next = rNode.next
        if rNode.next != None:
            rNode.next.prev = rNode.prev
        del(rNode)


    def find(self, fData:int)->bool:
        '''
        @input: 
            @Data: data value to be searched in list
        '''
        run = self.searchNode(fData)
        return run is not None
        
    
    def length(self)->int:
        '''
        Returns number of data nodes in the calling linked list
        '''
        n = 0
        run = self.headNode.next
        while run != None:
            n += 1
            run = run.next
        return n
       
    
    def isEmpty(self)->bool:
        return self.headNode.next == None
    
#Client Side

print("----------------Creating a new SinglyLinkedList Object----------------")
L = DoublyLinkedList()

print("----------------Testing for the empty list----------------")
try:
    data = L.getStart()
except:
    generic_exception_handler()

try:
    data = L.getEnd()
except:
    generic_exception_handler()

try:
    data = L.popStart()
except:
    generic_exception_handler()

try:
    data = L.popEnd()
except:
    generic_exception_handler()

try:
    data = L.removeStart()
except:
    generic_exception_handler()

try:
    data = L.removeEnd()
except:
    generic_exception_handler()

n = L.length()
print(f"Length of the empty list : {n}")

b = L.isEmpty()
print(f"List is empty: {b}")

print("\n")

print("----------------Testing insertStart()----------------")
for data in range(1,6):
    L.insertStart(data * 10)
print("Showing the list after L.insertStart():")
L.showList()

print("\n")

print("----------------Testing insertEnd()----------------")
for data in range(6,11):
    L.insertEnd(data * 10)
print("Showing the list after L.insertEnd():")
L.showList()

print("\n")

print("----------------Testing insertAfter() for non-existent data----------------")
try:
    L.insertAfter(-50, 1000)
except:
    generic_exception_handler()

print("")

print("----------------Testing insertAfter() for middle----------------")
L.insertAfter(10, 500)
L.showList()

print("")

print("----------------Testing insertAfter() for last node----------------")
L.insertAfter(100, 1000)
L.showList()


print("\n")

print("----------------Testing insertBefore() for non-existent data----------------")
try:
    L.insertBefore(-50, 1000)
except:
    generic_exception_handler()

print("")

print("----------------Testing insertBefore() for middle node----------------")
L.insertBefore(10, 600)
L.showList()

print("")

print("----------------Testing insertBefore() for first node----------------")
L.insertBefore(50, 5000)
L.showList()

print("\n")

print("----------------Testing getStart(), getEnd() on non empty list----------------")
firstData = L.getStart()
lastData = L.getEnd()
print(f"First Data: {firstData}, Last Data: {lastData}")
print("Showing list after L.getStart() and L.getEnd() to prove that strart and end nodes are not removed")
L.showList()

print("\n")

print("----------------Testing popStart(), popEnd() on non empty list----------------")
firstData = L.popStart()
lastData = L.popEnd()
print(f"First Data: {firstData}, Last Data: {lastData}")
print("Showing list after L.popStart() and L.popEnd() to prove that strart and end nodes are removed")
L.showList()

print("\n")

print("----------------Testing removeStart(), removeEnd() on non-empty list----------------")
L.removeStart()
L.showList()
L.removeEnd()
L.showList()

print("\n")

print('----------------Testing removeData() for non-existing data value----------------')
try:
    L.removeData(-400)
except: 
    generic_exception_handler() 

print('----------------Testing removeData() for the middle data----------------')
L.removeData(60)
L.showList() 

print('----------------Testing removeData() for the first node (boundary condition testing)----------------')
L.removeData(L.getStart())
L.showList() 

print('----------------Testing removeData() for the last node(boundary condition testing)----------------')
L.removeData(L.getEnd())
L.showList()

print("\n")

print('----------------Testing length()/isEmpty() on non-empty list----------------')
n = L.length() 
print(f'Length of list:{n}')

b = L.isEmpty() 
print(f'L is empty: {b}')

print("\n")

print('----------------END----------------')

