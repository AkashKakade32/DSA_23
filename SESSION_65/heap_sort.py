"""
@author: Yogeshwar Shukla 
@goal: To implement and test the heap sort algorithm 
"""

import sys 

def get_list(N: int) -> list[int]: 
    """
    @input: 
        @N: positive integer -> expected size of list 
    @output: 
        Populates newly created list with @N random numbers 
        stipulated between 0 to 1000 
    """
    from random import randint
    
    if type(N) != int: 
        raise TypeError("N must be an int")
    if N <= 0: 
        raise ValueError("N must be positive")

    L = []  
    
    starting_number = 0
    ending_number = 1001
    
    for i in range(N): 
        L.append(randint(starting_number, ending_number))
    
    return L 

def show_list(L: list[int], msg: str) -> None: 
    """
    @input: 
        @L: list of integers 
        @msg: string message
    @output: 
        Displays @msg along with @L on the standard output device 
    """
    print(msg)
    for i in range(len(L)): 
        print(f'L[{i}]:{L[i]}')

def parent(i: int) -> int:
    return (i - 1) // 2

def left(i: int) -> int:
    return 2 * i + 1

def right(i: int) -> int:
    return 2 * i + 2

def max_heapify(A: list[int], i: int, heap_size: int) -> None:
    l = left(i)
    r = right(i)
    
    # Find the largest among A[i], A[l], A[r]
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i
    
    if r < heap_size and A[r] > A[largest]:
        largest = r
    
    # If largest is not the root, swap and continue heapifying
    if largest != i:
        # Exchange A[i] with A[largest]
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        
        # Recursively heapify the affected sub-tree
        max_heapify(A, largest, heap_size)

def build_max_heap(A: list[int]) -> None:
    heap_size = len(A)
    
    # Start from the last non-leaf node and heapify each node
    # Last non-leaf node is at index floor(n/2) - 1 (for 0-indexed)
    i = (heap_size // 2) - 1
    
    while i >= 0:
        max_heapify(A, i, heap_size)
        i = i - 1

def heap_sort(A: list[int]) -> None:
    # Build a max-heap from the input array
    build_max_heap(A)
    
    heap_size = len(A)
    i = len(A) - 1
    
    # Extract elements from heap one by one
    while i >= 1:
        # Move current root (maximum) to end
        temp = A[0]
        A[0] = A[i]
        A[i] = temp
        
        # Reduce heap size by one
        heap_size = heap_size - 1
        
        # Call max_heapify on the reduced heap
        max_heapify(A, 0, heap_size)
        
        i = i - 1


def main(): 
    """
    Main function to test heap sort implementation
    """
    print("-" * 60)
    
    # Interactive input
    N = int(input("Enter the size of the list (greater than 2): "))
    if N < 2: 
        print("Bad size")
        sys.exit(-1)

    # Generate random list
    L = get_list(N)
    show_list(L, "Before sort:")
    heap_sort(L)
    show_list(L, "\nAfter sort:")
   

main()