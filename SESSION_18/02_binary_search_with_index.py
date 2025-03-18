def binSearch(si, ei, L, SE):
    if si<=ei:
        mi = (si+ei)//2
        if SE == L[mi]:
            return True, mi
        elif SE < L[mi]:
            return binSearch(si, mi-1, L, SE)
        else:
            return binSearch(mi+1, ei, L, SE)
    else:
        return False, None

L = [10,20,30,40,50,60,70,80,90]

for x in L:
    status, index = binSearch(0, len(L)-1, L, x)
    if status == True:
        print(x, "is present in the list", L, "at index", index)
    else:
        print(x, "is not present in the list", L)

M = [15,25,35,45,55,65]

for x in M:
    status, index = binSearch(0, len(L)-1, L, x)
    if status == True:
        print(x, "is present in the list", L, "at index", index)
    else:
        print(x, "is not present in the list", L)


while True:
    ans = int(input("Do you want to search one more time? [1 : Yes, 0 : No] : "))
    if ans != 1:
        break
    SE = int(input("Enter integer value to be searched : "))
    status, index = binSearch(0, len(L)-1, L, SE)
    if status == True:
        print(SE, "is present in the list", L, "at index", index)
    else:
        print(SE, "is not present in the", L)

print("Exiting the binary search")