'''
@Author: Akash Avinash Kakade
@Date: 14th April 2025
@Goal: To implement singly linked list of integers
'''

class SNode:
    '''
    This class implements a node for singly linked list and 
    singly circular linked list
    '''

    def __init__(self, initData):
        '''
        @input:
            @initData: integer to be stored in a newly allocated node
        Constructor creates two attributes in a newly allocated node
        viz. i) 'data': initialized by local variable 'initData'
        ii) 'next': initialized to None. This is a self reference to the next
        in sequence node in a collection
        '''

        print('----Entered SNode.__init__()----')

        self.data = initData
        self.next = None

        print(f"SNode.__init__():self.__dict__:{self.__dict__}")

        print('----Leaving SNode.__init__()----')


class SinglyLinkedList:
    '''
    This class implemets singly linked list ADT.
    '''

    def __init__(self):
        '''
        An attribute named 'headNode' will be created in a newly allocated
        object of class SinglyLinkedList.
        The attribute name will be assigned to a newly allocated dummy node object
        of class SNode. (Note that the dummy node is the one whose 'data' attribute 
        is None)
        '''

        print("----Entered SinglyLinkedList.__init__()----")

        self.headNode = SNode(None)

        print(f"SinglyLinkedList.__init__():self.__dict__:{self.__dict__}")

        print("----Leaving SinglyLinkedList.__init__()----")

    
    def insertStart(self, newData:int):
        '''
        @input:
            @newData: new data to be insert at the starting position of the
            linked list. newData will be encapsulated in a new SNode object
            and the newwly allocated SNode object will be positioned at the 
            beginning of linked list(immediately next to the head node)
        '''

        print("----Entered SinglyLinkedList.insertStart()----")

        #Error Check
        if type(newData) != int:
            raise TypeError(f'{newData} is not type of int')

        #Logic
        newNode = SNode(newData)
        newNode.next = self.headNode.next
        self.headNode.next = newNode

        print("----Leaving SinglyLinkedList.insertStart()----")


    def insertEnd(self, newData:int):
        '''
        @input:
            @newData: new data to be insert at the end position of the linked list.
            newData will be encapsulated in a SNode object and the newly allocated
            SNode object will be positioned at the end of linked list.
        '''

        print("----Entered SinglyLinkedList.insertEnd()----")

        #Error Check
        if type(newData) != int:
            raise TypeError(f'{newData} is not type of int')

        #Logic
        run = self.headNode

        while run.next != None:
            run = run.next

        run.next = SNode(newData)
        
        print("----Leaving SinglyLinkedList.inserEnd()----")


    def showList(self):
        '''
        Display the data members of all nodes except the head node
        '''

        run = self.headNode.next

        print("[START]-->", end="")

        while run != None:
            print(f"[{run.data}]-->", end="")
            run = run.next

        print("[END]")



# Client Side

print("\n\n Creating a new SinglyLinkedList object\n")

L = SinglyLinkedList()

print("\n\n Testing insertStart()\n")
for data in range(1,6):
    L.insertStart(data * 10)

print("Showing list after L.insertStart() : ")
L.showList()

print("\n\n Testing insertEnd()\n")
for data in range(6,11):
    L.insertEnd(data*10)

print("Showing list after L.insertEnd():")
L.showList()

