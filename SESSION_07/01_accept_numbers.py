L = [] 
while True:
    ans = int(input("Do you want to add more numbers?[1 for Yes, 0 for No]"))
    if ans != 1:
        break
    data = int(input("Enter Next Number : "))
    L.append(data)

print("Enterd Numbers Are : ", L)