import sys
from geh import geh

path_name =  'abc.txt'

try:
    f_handle = open('abc.txt', 'w')
    print("This is the first line", file=f_handle)
    L = [10,20,30,40]
    for x in L:
        print(x, file=f_handle)
    D = {'a':'Yogeshwar', 'b':'CPA'}
    print(D, file=f_handle)
    f_handle.close()
except:
    geh(should_exit=True)


try:
    f_handle = open('abc.txt', 'r')
    for x in f_handle:
        print(x)
    f_handle.close()
except:
    geh(should_exit=True)