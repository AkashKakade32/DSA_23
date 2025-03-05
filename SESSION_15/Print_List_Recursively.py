'''
Program to print the list recursively
'''

L = [10,22,30,40,50,60,70,80,90,100,101,102,103,104,105,106,107,108,109,110]

def printList(i:int, L:list):
    if(len(L) == 0):
        raise ValueError('List has no items in it')

    if(i == len(L)):
        return None
    else:
        print(i, L[i])
        printList(i+1, L)

printList(0,L)

print("*****************************************************************************************************")


def printListReverse(i:int, L:list):
    if(len(L) == 0):
        raise ValueError("List has no items in it")

    if(i == len(L)):
        return None
    else:
        printListReverse(i+1, L)
        print(i, L[i])

printListReverse(0, L)
