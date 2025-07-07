'''
Syntax: 
    (1) The syntax of yield statement is similar to that of return statement. 
        yield RHS_expr 
    (2) Constraints: 
        (a) Like the return statement, the yield statement MUST BE written inside a 
            def statement. 
        (b) The function must have either return statement or yield statement but not 
            both. It is permissible for both statements to be absent. (In that case 
            Python inserts return None as the last statement)
        (c) If a function contains a yield statement then IT MUST NOT DO ANY STANDARD IO
            i.e. you are not allowed to call print() or input() function. They wont have 
            any effect if you use them. 
'''

def test_yield_stmnt(): 
    yield True 
    yield 10 
    yield "Hello"
    yield 500 
    # Uncomment following statements to verify that they 
    # have no effect when the function is called 
    # print("HELLO")
    # return "hi"

X = test_yield_stmnt() 
print('type(X):', type(X)) # class generator 

val = X.__next__()
print(val) 

val = X.__next__() 
print(val)

val = X.__next__() 
print(val)

val = X.__next__() 
print(val)

'''
val = X.__next__()  # this will trigger StopIteration Exception 
print(val)
'''

def test1(): 
    for i in range(1, 10): 
        if i % 2 == 0: 
            yield i**2 
        else: 
            yield i**3 

X = test1() 

while True: 
    try: 
        val = X.__next__() 
        print('X.__next__():', val)
    except StopIteration: 
        break 