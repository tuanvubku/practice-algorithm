def longestOnes( A, K):
    l, r = 0, 0
    zeros = K
    res = 0
    while l < len(A) and r < len(A):
        print(r)
        print(A[r])
        if A[r] == 1:
            r += 1
        elif A[r] == 0 and zeros > 0:
            r += 1
            zeros -= 1
        elif A[r] == 0 and zeros <= 0:
            print("Vu", r)
            # move through all value 1
            while A[l] == 1:
                l += 1
            l += 1
            zeros += 1
            print("vulleft", l)
        print("right", r, "left", l)
        res = max(res, r - l)
    return res

res = longestOnes([0,0,0,1],0)
print(res)