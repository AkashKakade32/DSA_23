print("Start")
N = 5
i = 0
while i<N:
    print("Outer Loop Start With i:",i)
    j = i+1
    while j<N:
        print(f"i:{i}, j:{j}")
        j = j+1
    i = i+1
print("end")
