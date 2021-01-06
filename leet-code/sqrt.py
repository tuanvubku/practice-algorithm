def mySqrt(x: int):
    previous = -1

    # case x = 0
    if x == 0 or x == 1:
        return x
    for i in range(1, x//2 + 1):
    
        current = i * i
        if current == x:
            return i
        elif current > x and previous < x:
            return previous
        previous = i
    return previous
    
print(mySqrt(2))



