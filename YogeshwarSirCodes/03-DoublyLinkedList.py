'''
@author: Yogeshwar Shukla 
@date: 26th April 2025 
@goal: To implement doubly linked list of integers 
'''

def generic_exception_handler(trace=False): 
    from sys import exc_info 
    excName, excData, excTb = exc_info() 
    print(excName, excData, sep=':', flush=True)
    if trace is True: 
        from traceback import print_tb 
        print_tb(excTb) 

class DNode: 
    '''
    This class implements a node for doubly linked list and 
    doubly circular linked list 
    '''

    def __init__(self, initData: int): 
        # print('----Enterd DNode.__init__()----')
        if type(initData) != int and initData is not None: 
            raise TypeError(f'Data in node must of type int, given of type {type(initData)}')
        self.data = initData 
        self.prev = None 
        self.next = None 
        print(f'DNode.__init__():self.__dict__:{self.__dict__}')
        print("----Leaving DNode.__init__()----")


class DoublyLinkedList: 
    '''
    This class implements doubly linked list ADT. 
    '''
    def __init__(self): 
        '''
        An attribute named 'head_node' will be created in a newly allocated 
        object of class SinglyLinkedList. The attribute name will be assigned 
        to a newly allocated dummy node object of class SNode. (Note that 
        the dummy node is the one whose 'data' attribute is None)
        '''
        #print('----Entered SinglyLinkedList.__init__()----')
        self.headNode = DNode(None)
        #print(f'SinglyLinkedList.__init__():self.__dict__:{self.__dict__}')
        #print('----Leaving SinglyLinkedList.__init__()----')

    def insertStart(self, newData: int): 
        '''
        @input: 
            @newData: new data to be insert at the starting position of the linked list
        newData will be encapsulated in a new SNode object and the newly allocated SNode 
        object will be positioned at the beginning after the linked list (immediately 
        next to the head node)
        '''
        #print('----Entered DoublyLinkedList.insertStart()----')
        startNode = self.headNode 
        endNode = self.headNode.next      
        midNode = DNode(newData)
        midNode.next = endNode 
        midNode.prev = startNode
        startNode.next = midNode
        if endNode is not None and type(endNode) == DNode:
            endNode.prev = midNode 
        #print('----Leaving DoublyLinkedList.insertStart()----')

    def insertEnd(self, newData: int): 
        #print('----Entered DoublyLinkedList.insertEnd()----')
        run = self.headNode
        while run.next is not None: 
            run = run.next 
        run.next = DNode(newData)
        run.next.prev = run 
        #print('----Leaving DoublyLinkedList.insertEnd()----')

    def showList(self): 
        '''
        Display the data members of all nodes except the head node 
        '''
        print("[START]<->", end='')
        run = self.headNode.next 
        while run is not None: 
            print(f'[{run.data}]<->', end='')
            run = run.next
        print('[END]')

    
    def searchNode(self, searchData: int): 
        '''
        @input: 
            @searchData: data value to be searched. 
        returns the node containing first occurrence of search_data
        and the node previous to it. 
        returns None if the searchData is not present. 
        '''
        run = self.headNode.next 
        while run is not None: 
            if run.data == searchData: 
                return run 
            run = run.next 
        return None 
        

    def insertAfter(self, existingData: int, newData: int): 
        '''
        @input: 
            @existingData: Datavalue which is supposed to be present in the list. 
            @newData: Data value that must be inserted after the first occurrence 
                of the @existingData. 
        a) Inserts a newly allocated node containing @newData after the node 
        containing the first occurrence of existingData. 
        b) raise ValueError if existingData is not found. 
        '''
        existingNode = self.searchNode(existingData)
        if existingNode is None: 
            raise ValueError(f'Invalid existing data:{existingData}')
        newNode = DNode(newData)
        newNode.next = existingNode.next 
        newNode.prev = existingNode 
        if existingNode.next is not None: 
            existingNode.next.prev = newNode 
        existingNode.next = newNode 


    def insertBefore(self, existingData: int, newData: int): 
        '''
        @input: 
            @existingData: Datavalue which is supposed to be present in the list. 
            @newData: Data value that must be inserted before the first occurrence 
                of the @existingData. 
        a) Inserts a newly allocated node containing @newData before the node 
        containing the first occurrence of existingData. 
        b) raise ValueError if existingData is not found. 
        '''
        existingNode = self.searchNode(existingData)
        if existingNode is None: 
            raise ValueError(f'Invalid existing data:{existingData}')
        newNode = DNode(newData)
        newNode.next = existingNode
        newNode.prev = existingNode.prev 
        existingNode.prev.next = newNode 
        existingNode.prev = newNode 

    
    def getStart(self) -> int: 
        '''
        a) Returns data value in the first node with data without removing the first node. 
        b) raise ValueError if the list is empty 
        '''
        if self.isEmpty(): 
            raise ValueError(f'Cannot get start of the empty list')
        return self.headNode.next.data 

    def getEnd(self) -> int: 
        '''
        a) Returns data value in the last node with data without removing the last node. 
        b) raise ValueError if the list is empty 
        '''
        if self.isEmpty(): 
            raise ValueError(f'Cannot get end of the empty list')
        run = self.headNode
        while run.next is not None: 
            run = run.next 
        return run.data 


    def popStart(self) -> int: 
        '''
        a) Remove the first node with data and return the data value int it
        b) raise ValueError if the list is empty 
        '''
        if self.isEmpty(): 
            raise ValueError(f'Cannot pop start of the empty list')
        firstNodeWithData = self.headNode.next 
        data = firstNodeWithData.data 
        firstNodeWithData.prev.next = firstNodeWithData.next
        if firstNodeWithData.next is not None: 
            firstNodeWithData.next.prev = firstNodeWithData.prev 
        del firstNodeWithData 
        return data 


    def popEnd(self) -> int: 
        '''
        a) Remove the last node with data and return the data value int it
        b) raise ValueError if the list is empty 
        '''
        if self.isEmpty(): 
            raise ValueError(f'Cannot pop end of the empty list')
        run = self.headNode 
        while run.next is not None: 
            run = run.next 
        data = run.data 
        run.prev.next = None 
        del run 
        return data 


    def removeStart(self): 
        '''
        a) Removes the first node with data in the list. 
        b) raise ValueError if the list is empty 
        '''
        if self.isEmpty(): 
            raise ValueError(f'Cannot remove start of the empty list')
        firstNodeWithData = self.headNode.next 
        firstNodeWithData.prev.next = firstNodeWithData.next
        if firstNodeWithData.next is not None: 
            firstNodeWithData.next.prev = firstNodeWithData.prev 
        del firstNodeWithData 
       

    def removeEnd(self): 
        '''
        a) Removes the last node with data in the list 
        b) raise ValueError if the list empty 
        '''
        if self.isEmpty(): 
            raise ValueError(f'Cannot remove end of the empty list')
        run = self.headNode 
        while run.next is not None: 
            run = run.next 
        run.prev.next = None 
        del run 
       

    def removeData(self, rData: int): 
        '''
        @input: 
            @rData: Data value whose first occurrence within linked list must be removed
        Remove the first node containing value @rData 
        raise ValueError if the @rData does not exist
        ''' 
        rNode = self.searchNode(rData)
        if rNode is None: 
            raise ValueError(f"Invalid value for remove data {rData}")
        rNode.prev.next = rNode.next 
        if rNode.next is not None: 
            rNode.next.prev = rNode.prev 
        del rNode 


    def find(self, fData: int) -> bool: 
        '''
        @input: 
            @fData: data value to be searched in list
        '''
        run = self.searchNode(fData)
        return run is not None 
    
  
    def length(self) -> int: 
        '''
        Returns number of data nodes in the calling linked list 
        '''
        n = 0 
        run = self.headNode.next 
        while run is not None: 
            n += 1 
            run = run.next 
        return n 

    
    def isEmpty(self) -> bool: 
        '''
        Returns whether or not the calling list object is empty
        ''' 
        return self.headNode.next is None
    
    def concat(self, other): 
        newList = DoublyLinkedList() 
        lastNode = newList.headNode 
        run = self.headNode.next 
        while run is not None: 
            newNode = DNode(run.data)
            lastNode.next = newNode 
            newNode.prev = lastNode 
            lastNode = newNode 
            run = run.next 
        run = other.headNode.next 
        while run is not None: 
            newNode = DNode(run.data)
            lastNode.next = newNode 
            newNode.prev = lastNode 
            lastNode = newNode 
            run = run.next 
        return newList 

    
    def append(self, other): 
        if other.isEmpty(): 
            del other.headNode 
            return None 
        
        lastNode = self.headNode 
        while lastNode.next is not None: 
            lastNode = lastNode.next 

        lastNode.next = other.headNode.next 
        other.headNode.next.prev = lastNode 
        
        other.headNode.next = None 
        del other.headNode 
    

    def merge(self, other): 
        mergedList = DoublyLinkedList() 
        lastNode = mergedList.headNode
        run1 = self.headNode.next 
        run2 = other.headNode.next 
        while True: 
            if run1 is None: 
                while run2 is not None: 
                    newNode = DNode(run2.data)
                    lastNode.next = newNode 
                    newNode.prev = lastNode 
                    lastNode = lastNode.next 
                    run2 = run2.next 
                break 
            
            if run2 is None: 
                while run1 is not None: 
                    newNode = DNode(run1.data)
                    lastNode.next = newNode 
                    newNode.prev = lastNode 
                    lastNode = lastNode.next 
                    run1 = run1.next 
                break 

            tmpData = None 
            if run1.data <= run2.data: 
                tmpData = run1.data 
                run1 = run1.next 
            else: 
                tmpData = run2.data 
                run2 = run2.next 
            newNode = DNode(tmpData)
            lastNode.next = newNode 
            newNode.prev = lastNode 
            lastNode = lastNode.next 
        
        return mergedList


    def getReversedList(self): 
        newList = DoublyLinkedList() 
        run = self.headNode.next 
        while run is not None: 
            newList.insertStart(run.data)
            run = run.next 
        return newList 

    
    def reverse(self): 
        if self.isEmpty(): 
            return None 
        originalFirstNode = self.headNode.next 
        run = originalFirstNode.next 
        while run is not None: 
            run_next = run.next 
            run.next = self.headNode.next 
            run.prev = self.headNode 
            self.headNode.next.prev = run 
            self.headNode.next = run 
            run = run_next 
        originalFirstNode.next = None 


# Client Side 
# Create a new object of class DoublyLinkedList for testing purpose 
print('----------------Creating a new DoublyLinkedList object-----------------')
L = DoublyLinkedList() 
print('----------------Testing for empty list----------------')
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
print(f'Length of empty list:{n}')

b = L.isEmpty() 
print(f'L is empty: {b}')

print('----------------Testing insertStart()----------------')
for data in range(1, 6): 
    L.insertStart(data * 10) 

print('Showing list after L.insertStart():')
L.showList() 

print('----------------Testing insertEnd()----------------')
for data in range(6, 11): 
    L.insertEnd(data * 10)

print('Showing list after L.insertEnd():')
L.showList() 

print('----------------Testing insertAfter() for non-existent data----------------')
try: 
    L.insertAfter(-50, 1000)
except: 
    generic_exception_handler()

print('----------------Testing insertAfter() for middle node----------------')
L.insertAfter(10, 500)
L.showList() 

print("----------------Testing insertAfter() for the last node(boundary condition testing)----------------")
L.insertAfter(100, 1000)
L.showList() 

print('----------------Testing insertBefore() for non-existent data----------------')
try: 
    L.insertBefore(-50, 1000)
except: 
    generic_exception_handler()

print('----------------Testing insertBefore() for middle node----------------')
L.insertBefore(10, 600)
L.showList() 

print("----------------Testing insertBefore() for the first node(boundary condition testing)----------------")
L.insertBefore(50, 5000)
L.showList() 

print('----------------Testing getStart(), getEnd() on non-empty list----------------')
firstData = L.getStart() 
lastData = L.getEnd() 
print(f'First Data:{firstData}, Last Data:{lastData}')
print("Showing list after L.getStart() and L.getEnd() to prove that start and end nodes are not removed")
L.showList()

print('----------------Testing popStart(), popEnd() on non-empty list----------------')
firstData = L.popStart() 
lastData = L.popEnd() 
print(f'First Data:{firstData}, Last Data:{lastData}')
print("Showing list after L.popStart() and L.popEnd() to prove that start and end nodes are removed")
L.showList()

print('----------------Testing removeStart() and removeEnd() on non-empty list----------------')
L.removeStart() 
L.showList() 
L.removeEnd() 
L.showList() 

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

print('----------------Testing length()/isEmpty() on non-empty list----------------')
n = L.length() 
print(f'Length of list:{n}')

b = L.isEmpty() 
print(f'L is empty: {b}')

print('---------------Testing inter-list routines---------------')
L1 = DoublyLinkedList() 
L2 = DoublyLinkedList() 
for data in [100, 200, 300, 400, 500]: 
    L1.insertStart(data)
for data in [10, 15, 12, 32, 16, 76, 987]: 
    L2.insertEnd(data)

print('----Concat() test----')
L3 = L1.concat(L2)
print('Before concat:')
print("L1:")
L1.showList() 
print("L2:")
L2.showList() 
print("After concat:")
print("L3:")
L3.showList() 
print("L1:")
L1.showList() 
print("L2:")
L2.showList() 

print('----getReversedList()----')
LR1 = L1.getReversedList() 
LR2 = L2.getReversedList() 
print("Before L1.getReversedList() and L2.getReversedList()")
print("L1:")
L1.showList() 
print("L2:")
L2.showList() 
print("After L1.getReversedList() and L2.getReversedList():")
print("L1:")
L1.showList() 
print("L2:")
L2.showList() 
print("LR1:")
LR1.showList() 
print("LR2:")
LR2.showList() 

print("----L1.append(L2) testing----")
print("Before L1.append(L2):")
print("L1:")
L1.showList() 
print("L2:")
L2.showList() 

L1.append(L2)
del L2 

print("After L1.append(L2):L1:")
L1.showList() 

print('----P.merge(Q)----')
P = DoublyLinkedList() 
Q = DoublyLinkedList() 
for data in [10, 20, 30, 40, 50]: 
    P.insertEnd(data) 
for data in [5, 15, 17, 35, 49, 55, 80, 90]: 
    Q.insertEnd(data)

print("Before P.merge(Q):")
print("P:")
P.showList() 
print("Q:")
Q.showList() 
mergedList = P.merge(Q)
print("After P.merge(Q):")
print("P:")
P.showList() 
print("Q:")
Q.showList() 
print("mergedList:")
mergedList.showList() 

print("----L.reverse() testing----")
newList = DoublyLinkedList() 
print('Before newList.reverse():newList:')
newList.showList() 
newList.reverse() 
print('After newList.reverse():newList:')
newList.showList() 

newList.insertEnd(100)
print('Before newList.reverse():newList:')
newList.showList() 
newList.reverse() 
print('After newList.reverse():newList:')
newList.showList() 

for data in [100, 400, 200, 300, 600, 700, 100]: 
    newList.insertEnd(data)
print('Before newList.reverse():newList:')
newList.showList() 
newList.reverse() 
print('After newList.reverse():newList:')
newList.showList() 


print('----------------END----------------')
