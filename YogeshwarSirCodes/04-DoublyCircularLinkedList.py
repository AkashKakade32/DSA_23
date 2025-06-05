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
    def __init__(self, newData: int): 
        self.data = newData 
        self.prev = None 
        self.next = None 

class DoublyCircularLinkedList: 
    def __init__(self): 
        self.headNode = DNode(None)
        self.headNode.prev = self.headNode 
        self.headNode.next = self.headNode 


    def insertStart(self, newData: int): 
        startNode = self.headNode 
        endNode = self.headNode.next 
        midNode = DNode(newData)
        midNode.next = endNode 
        midNode.prev = startNode 
        startNode.next = midNode 
        endNode.prev = midNode 


    def insertEnd(self, newData: int): 
        startNode = self.headNode.prev 
        endNode = self.headNode 
        midNode = DNode(newData)
        midNode.next = endNode 
        midNode.prev = startNode 
        startNode.next = midNode 
        endNode.prev = midNode 


    def searchNode(self, searchData: int): 
        run = self.headNode.next 
        while run is not self.headNode: 
            if run.data == searchData: 
                return run 
            run = run.next 
        return None 


    def insertAfter(self, existingData: int, newData: int): 
        existingNode = self.searchNode(existingData)
        startNode = existingNode 
        endNode = existingNode.next 
        midNode = DNode(newData)
        midNode.next = endNode 
        midNode.prev = startNode 
        startNode.next = midNode 
        endNode.prev = midNode 

    
    def insertBefore(self, existingData: int, newData: int): 
        existingNode = self.searchNode(existingData)
        startNode = existingNode.prev 
        endNode = existingNode 
        midNode = DNode(newData)
        midNode.next = endNode 
        midNode.prev = startNode 
        startNode.next = midNode 
        endNode.prev = midNode 
    

    def getStart(self): 
        if self.isEmpty(): 
            raise ValueError('Cannot getStart() from empty list')
        return self.headNode.next.data 


    def getEnd(self): 
        if self.isEmpty(): 
            raise ValueError('Cannot getEnd() from empty list')
        return self.headNode.prev.data 


    def popStart(self): 
        if self.isEmpty(): 
            raise ValueError('Cannot popStart() from empty list') 
        data = self.headNode.next.data 
        rNode = self.headNode.next 
        rNode.prev.next = rNode.next 
        rNode.next.prev = rNode.prev 
        del rNode 
        return data 
        

    def popEnd(self): 
        if self.isEmpty(): 
            raise ValueError('Cannot popEnd() from empty list')
        data = self.headNode.prev.data 
        rNode = self.headNode.prev 
        rNode.prev.next = rNode.next 
        rNode.next.prev = rNode.prev 
        del rNode 
        return data 


    def removeStart(self): 
        if self.isEmpty(): 
            raise ValueError('Cannot removeStart() from empty list')
        rNode = self.headNode.next 
        rNode.prev.next = rNode.next 
        rNode.next.prev = rNode.prev 
        del rNode 


    def removeEnd(self): 
        if self.isEmpty(): 
            raise ValueError('Cannot removeEnd() from empty list')
        rNode = self.headNode.prev 
        rNode.prev.next = rNode.next
        rNode.next.prev = rNode.prev 
        del rNode 


    def removeData(self, rData:int): 
        rNode = self.searchNode(rData)
        if rNode is None: 
            raise ValueError("Bad data from removal")
        rNode.prev.next = rNode.next 
        rNode.next.prev = rNode.prev 
        del rNode 

    
    def showList(self): 
        print('[START]<->', end='')
        run = self.headNode.next 
        while run is not self.headNode: 
            print(f'[{run.data}]<->', end='')
            run = run.next 
        print('[END]')


    def length(self) -> int: 
        n = 0 
        run = self.headNode.next 
        while run is not self.headNode: 
            n = n + 1 
            run = run.next 
        return n 


    def isEmpty(self) -> bool: 
        return ((self.headNode.next is self.headNode) and (self.headNode.prev is self.headNode))


    def concat(self, other): 
        newList = DoublyCircularLinkedList() 
        lastNode = newList.headNode 

        run = self.headNode.next 
        while run is not self.headNode: 
            newNode = DNode(run.data)
            newNode.prev = lastNode 
            lastNode.next = newNode 
            lastNode = lastNode.next
            run = run.next

        run = other.headNode.next 
        while run is not other.headNode: 
            newNode = DNode(run.data)
            newNode.prev = lastNode 
            lastNode.next = newNode 
            lastNode = lastNode.next 
            run = run.next 

        lastNode.next = newList.headNode 
        newList.headNode.prev = lastNode 

        return newList 

    def append(self, other): 
        if other.isEmpty(): 
            del other.headNode 
            return None 
        
        self.headNode.prev.next = other.headNode.next
        other.headNode.next.prev = self.headNode.prev 

        other.headNode.prev.next = self.headNode 
        self.headNode.prev = other.headNode.prev 

        del other.headNode 


    def merge(self, other): 
        mergedList = DoublyCircularLinkedList() 
        lastNode = mergedList.headNode 

        run1 = self.headNode.next 
        run2 = other.headNode.next 
        
        while True: 
            if run1 is self.headNode: 
                while run2 is not other.headNode: 
                    newNode = DNode(run2.data)
                    newNode.prev = lastNode 
                    lastNode.next = newNode 
                    lastNode = lastNode.next 
                    run2 = run2.next 
                break 
            
            if run2 is other.headNode: 
                while run1 is not self.headNode: 
                    newNode = DNode(run1.data)
                    newNode.prev = lastNode 
                    lastNode.next = newNode 
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
            tmpNode = DNode(tmpData)
            tmpNode.prev = lastNode 
            lastNode.next = tmpNode 
            lastNode = lastNode.next 
        
        lastNode.next = mergedList.headNode 
        mergedList.headNode.prev = lastNode 

        return mergedList 

    def getReversedList(self): 
        reversedList = DoublyCircularLinkedList() 
        run = self.headNode.next 
        while run is not self.headNode: 
            reversedList.insertStart(run.data)
            run = run.next 
        return reversedList 


    def reverse(self): 
        if self.isEmpty(): 
            return None 
        originalFirstNode = self.headNode.next 
        run = originalFirstNode.next 
        while run is not self.headNode: 
            run_next = run.next 

            run.next = self.headNode.next 
            run.prev = self.headNode 

            self.headNode.next.prev = run 
            self.headNode.next = run 

            run = run_next

        originalFirstNode.next = self.headNode 
        self.headNode.prev = originalFirstNode 


# Client Side 
# Create a new object of class DoublyLinkedList for testing purpose 
print('----------------Creating a new DoublyLinkedList object(New Version)-----------------')
L = DoublyCircularLinkedList() 
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
L1 = DoublyCircularLinkedList() 
L2 = DoublyCircularLinkedList() 
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
P = DoublyCircularLinkedList() 
Q = DoublyCircularLinkedList() 
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
newList = DoublyCircularLinkedList() 
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

