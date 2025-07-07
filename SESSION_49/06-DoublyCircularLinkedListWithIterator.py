class DoublyCircularLinkedList_iterator: 
    def __init__(self, G): 
        self.G = G 
    def __next__(self): 
        return self.G.__next__() 


class DNode: 
    def __init__(self, data): 
        self.data = data 
        self.prev = None 
        self.next = None 


class DoublyCircularLinkedList: 
    @staticmethod 
    def generic_insert(start_node, mid_node, end_node): 
        mid_node.next = end_node 
        mid_node.prev = start_node 
        start_node.next = mid_node 
        end_node.prev = mid_node


    @staticmethod 
    def generic_delete(d_node): 
        d_node.prev.next = d_node.next 
        d_node.next.prev = d_node.prev 
        del d_node 


    def __init__(self): 
        self.head_node = DNode(None)
        self.head_node.prev = self.head_node 
        self.head_node.next = self.head_node 


    def insert_end(self, new_data): 
        DoublyCircularLinkedList.generic_insert(self.head_node.prev, DNode(new_data), self.head_node)


    def show(self): 
        print('[START]<->', end='')
        run = self.head_node.next 
        while run is not self.head_node: 
            print(f'[{run.data}]<->', end='')
            run = run.next 
        print('[END]')


    def __iter__(self): 
        def get_generator(head_node:DNode): 
            run = head_node.next 
            while run is not head_node: 
                yield run.data 
                run = run.next 
        return DoublyCircularLinkedList_iterator(get_generator(self.head_node))

L = DoublyCircularLinkedList() 
from random import randint 

for i in range(6): 
    L.insert_end(randint(1, 100))


L.show() 

print('Iterating over doubly circular linked list using for loop')

for x in L: 
    print(x)