'''
Goal : Given (X,Y) find the distance between the two coordinates or length
'''

x1 = float(input("Enter the X1 : "))
y1 = float(input("Enter the Y1 : "))
x2 = float(input("Enter the X2 : "))
y2 = float(input("Enter the Y2 : "))

d = ((x2-x1)**2 + (y2-y1)**2)**0.5

print(f"Distance between the two points {d} units")