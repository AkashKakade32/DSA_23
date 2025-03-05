def myR(n:int):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return n*myR(n-1)+n+myR(n-2)

print(myR(7))
