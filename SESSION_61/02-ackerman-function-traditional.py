def ackerman(m:int, n:int): 
    assert m >= 0 and n >= 0, "m and n cannot be negative"
    if m == 0: 
        return n + 1 
    
    if n == 0: 
        return ackerman(m-1, 1)
    
    return ackerman(m-1, ackerman(m, n-1))


print(f'ackerman({3}, {0}) = {ackerman(3, 0)}')