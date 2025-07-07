L = [10, 20, 30, 40]
print('LIST L:', L)
print('----Iterating through L using for loop----')
for x in L: 
    print(x)

print('----Iterating through L using while loop BUT WITHOUT INDEXING----')
print('We will achieve this by converting a for loop into while loop')

I = L.__iter__()  # type(I)==<class 'list_iterator'>
while True: 
    try: 
        x = I.__next__()
        print(x)
    except StopIteration: 
        break 


I = L.__iter__()  # type(I)==<class 'list_iterator'>
while True: 
    try: 
        x = I.__next__()
        # BODY OF FOR 
    except StopIteration: 
        break 

