import sys

a = float(input("Enter the CF of x^2 : "))
b = float(input("ENter the CF of X : "))
c = float(input("Enter the constants of equation : "))

if(a == 0):
    print("CF cannot be zero")
    sys.exit()

if(b**2 - 4*a*c < 0.0):
    print("This equation does not have real roots")
    sys.exit()

r1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
r2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

print(f"Root1: {r1}, Root2: {r2}")