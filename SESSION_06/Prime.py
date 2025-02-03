
"""
Step 1: Let "n" be the representation of the number
Step 2: To check if "n" is the prime number, we have to divide the "n" in range from 1 to n and check the remainder.
                if(n%i == 0):
                    rem = rem + 1
Step 3: let "i" be representation of the range 1 to n and let "rem" is the variable for remainder
Step 4: After the loop we have to check if "rem" is 2 then its prime number otherwise its not a prime number
                if(rem == 2):
                    print(f"{n} is the prime number")
Step 5: Combine above steps to write the code
                n = input()
                i = 1
                while(i<=n):
                    if(n%i == 0):
                        rem = rem + 1
                    i = i+1
                if(rem == 2):
                    print("{n} is the prime number")

"""

n = 9

i = 1

rem = 0

while(i<=n):
    if(n%i == 0):
        rem = rem + 1
    i = i+1
if(rem ==2):
    print("its prime numnber")
else:
    print("Its not prime")