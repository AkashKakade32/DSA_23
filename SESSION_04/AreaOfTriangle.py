'''
@Author : Akash Avinash Kakade
@Date : 12/01/2025

@Goal:
    1) To calculate area of triangle
    2) Validate all points are non colinear
    3) To check the output 

'''

def areaOfTriangle(x1:float, y1:float, x2:float, y2:float, x3:float, y3:float) -> float:
    '''

    '''
    c = (((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)))**0.5
    a = (((x3-x2)*(x3-x2)) + ((y3-y2)*(y3-y2)))**0.5
    b = (((x1-x3)*(x1-x3)) + ((y1-y3)*(y1-y3)))**0.5
    s = (a+b+c)/2
    
    area = (s*(s-a)*(s-b)*(s-c))**0.5

    return area


def main()->None:
    '''

    '''
    x1 = float(input("Enter the X1 Coordinate : "))
    y1 = float(input("Enter the Y1 Coordinate : "))
    x2 = float(input("Enter the X2 Coordinate : "))
    y2 = float(input("Enter the Y2 Coordinate : "))
    x3 = float(input("Enter the X3 Coordinate : "))
    y3 = float(input("Enter the Y3 Coordinate : "))

    area = areaOfTriangle(x1,y1,x2,y2,x3,y3)

    print(f'Area Of Triangle = {area}')

main()