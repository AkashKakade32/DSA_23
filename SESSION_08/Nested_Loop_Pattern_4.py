print("Start")
N = 5
i = 0
while i<N:
    print("Outer Loop Start With i:", i)
    j = 0
    while j<i:
        print(f"i:{i}, j:{j}")
        j = j+1
    i = i+1
print('End')
