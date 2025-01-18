'''
Goal to find the area of triangle
'''

a = float(input("Enter the length of sides a : "))
b = float(input("Enter the length of sides b : "))
c = float(input("Enter the length of sides c : "))



s = a+b+c/2

A = (s*(s-a)*(s-b)*(s-c))**0.5

print(f"Area of triangle {A} square units")