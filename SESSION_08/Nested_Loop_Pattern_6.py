print('start') 
N = 5
i = 0
while i < N:
    print('Out loop start with i:', i)
    j = 0
    while j != i:
        print(f'i:{i}, j:{j}')
        j = j + 1
    i = i + 1 
print('end')
