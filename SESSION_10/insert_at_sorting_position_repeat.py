def insert_at_sorting_position(L):
    k = L[len(L) - 1]
    i = len(L) - 2
    while i>=0:
        if L[i]>k:
            L[i+1] = L[i]
        else:
            break
        i = i-1
    L[i+1] = k

#*******************************************************************
def insert_at_sorting_position(L):
    k = L[len(L)-1]
    i = len(L) - 2
    while i>=0:
        if L[i]>k:
            L[i+1] = L[i]
        else:
            break
        i = i+1
    L[i+1] = k

#**********************************************************************
def insert_at_sorting_position(L):
    k = L[len(L) - 1]
    i = len(L)-2
    while i>=0:
        if L[i]>k:
            L[i+1] = L[i]
        else:
            break
        i = i+1
    L[i+1] = k