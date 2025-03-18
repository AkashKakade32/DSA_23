import sys

a = int(input("Enter the first integer in range : "))
b = int(input("Enter the second integer in range : "))

if a > b:
    print("Invalid range : the first integer of range must be less than the second")
    sys.exit()

print(f"Integers between {a} and {b} including {a} and {b} are (b-a+1) : ", (b-a)+1)
print(f"Integers between {a} and {b} including {a} and excluding {b} (b-a) : ", b-a)
print(f"Integers between {a} and {b} excluding {a} and including {b} (b-a) : ", b-a)
print(f"Integers between {a} and {b} excluding {a} and excluding {b} (b-a-1) : ", (b-a)-1)