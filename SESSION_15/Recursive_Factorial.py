'''
Factorial of Number using recurssion
'''

def factorial(n:int):
    if(type(n) != int):
        raise TypeError('Factorial of non integer number cancnot be calculated')
    if(n < 0):
        raise ValueError('Factorial of negative number cannot be calculated')

    if(n == 0):
        return 1;
    else:
        return n * factorial(n-1)



for i in range(0,1000):
    print(f'Factorial({i}) : {factorial(i)}')
