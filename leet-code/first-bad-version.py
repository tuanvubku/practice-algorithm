def isBadVersion(k):
    return True if k >= 0 else False

def firstBadVersion( n) -> int:
    left, right = 1, n
    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left


print(8//3)