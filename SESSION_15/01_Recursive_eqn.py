'''
Practice of recurssion and mathematical equation
'''

def myRecurr(n:int):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return myRecurr(n - 1) + myRecurr(n - 2)

print(myRecurr(7))
