'''
Area of triangle using cartesian coordinate system
'''

X1 = float(input("Enter the X1 of point A : "))
Y1 = float(input("Enter the Y1 of point A : "))
X2 = float(input("Enter the X2 of point B : "))
Y2 = float(input("Enter the Y2 of point B : "))
X3 = float(input("Enter the X3 of point C : "))
Y3 = float(input("Enter the Y3 of point C : "))

slope_AB = abs((Y2-Y1)/(X2-X1))
slope_AC = abs((Y3-Y1)/(X3-X1))

if slope_AB == slope_AC:
    print("Points are coolinear hence cannot form the triangle")

a = ((X3-X2)**2 + (Y3-Y2)**2) **0.5
b = ((X3-X1)**2 + (Y3-Y1)**2) **0.5
c = ((X2-X1)**2 + (Y2-Y1)**2) **0.5

s = a+b+c/2

A = (s * (s-1) * (s-b) * (s-c))**0.5

print(f"Area = {A} units")