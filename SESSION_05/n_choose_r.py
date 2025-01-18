

def factorial(n:int)->int:
    if(n<0):
        exit()
    rs = 1
    i = 1

    while(i<=n):
        rs = rs*i
        i = i+1
    return rs

n = int(input("Enter the n: "))
r = int(input("Enter the r: "))

combos = factorial(n)/(factorial(r) * factorial(n-r))

print(combos)
