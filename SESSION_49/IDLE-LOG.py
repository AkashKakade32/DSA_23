Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
T = (True, 10, 3.14, "Hello")
for x in T:
    print(x)

    
True
10
3.14
Hello
>>> #--------------------while loop
>>> I = T.__iter__()
>>> I.__next__()
True
>>> I.__next__()
10
>>> I.__next__()
3.14
>>> I.__next__()
'Hello'
>>> I.__next__()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    I.__next__()
StopIteration
>>> type(I)
<class 'tuple_iterator'>
>>> #-------------------
>>> I = T.__iter__()
>>> while True:
...     try:
...         x = I.__next__()
...         print(x)
...     except StopIteration:
...         break
... 
...     
True
10
3.14
Hello
