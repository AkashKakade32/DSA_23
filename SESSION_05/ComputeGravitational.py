m1 = float(input("Enter mass of object 1 :"))
m2 = float(input("Enter mass of object 2 :"))
r = float(input("Enter the distance between the objects :"))
G = 6.67*10**-11



F = (G*m1*m2)/(r**2)
print(f"Gravitational Force of Attraction is {F} Newton")