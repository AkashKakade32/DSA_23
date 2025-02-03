#Nested loop pattern 1
print("Start")
N = 5
i = 0
while i<N:
    print("Outer Loop Starts With i : ",i)
    j = 0
    while j<N:
        print(f"i:{i}, j:{j}")
        j = j+1
    i = i+1
print("end")
