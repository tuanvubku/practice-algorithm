

def rotate( nums, k):
    n = len(nums)
    k %= n

    start = count = 0
    while count < n:
        current, prev = start, nums[start]
        while True:
            next_idx = (current + k) % n
            nums[next_idx], prev = prev, nums[next_idx]
            #print(nums[next_idx], prev)
            current = next_idx
            count += 1
            print(current)
            if start == current:
                print(start, current)
                break
        start += 1

n = [1, 2, 3, 4, 5,6]
rotate(n, 4)
print(n)
