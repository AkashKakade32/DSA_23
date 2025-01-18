'''
Goal to find the 1) Slope of 2) Angle of Inclination of given line
'''

import math
import sys

x1 = float(input("Enter the X1 : "))
y1 = float(input("ENter the Y1 : "))
x2 = float(input("Enter the X2 : "))
y2 = float(input("ENter the Y2 : "))


if x2-x1 != 0.0:
    slope = (y2-y1)/(x2-x1)
    angleOfInclination = math.atan(slope)
    print(f"Slope = {slope}, Angle Of Inclination = {angleOfInclination} radians")