import sys

def factorial(n:int)->int:
    if(n < 0):
        sys.exit()
    if(n == 0):
        rs = 1
        return rs
    
    rs = 1
    i = 1
    while(i < n):
        rs = rs*i
        i = i+1

    return rs


print(factorial(10))