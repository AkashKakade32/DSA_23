import sys

def get_list_of_numbers_from_file(path_name:str):
    #Type Checking

    if type(path_name) != str:
        print("Invalid Path Name. Exiting the app")
        sys.exit()

    try:
        f_handle = open(path_name, "r")
    except:
        print("Error opening the file. Exiting the app")
        f_handle.close()
        sys.exit()

    #Take and empty list and add the data in the empty list
    L = []

    for line in f_handle:
        line = line.strip()
        try:
            n = int(line)
            L.append(n)
        except:
            print("Bad Integer Format on file data. Exiting the app")
            sys.exit()
            f_handle.close()
    
    f_handle.close()
    
    return L

##########################################################################################################

def insert_at_sorting_position(L, N):
    k = L[N-1]
    i = N-2
    while i>=0:
        if L[i]>k:
            L[i+1] = L[i]
        else:
            break
        i = i-1
    L[i+1] = k

def insertion_sort(L):
    N = 2
    while N<=len(L):
        insert_at_sorting_position(L, N)
        N = N+1

lst = get_list_of_numbers_from_file('Numbers.txt')
print("Before List : ",lst)
insertion_sort(lst)
print("After Sort : ", lst)