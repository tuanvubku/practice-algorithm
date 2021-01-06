from collections import  Counter
class Window():
    def __init__(self):
        self.counter = Counter()
        #count the number of k difference
        self.count = 0

    def add(self, val):
        self.counter[val] += 1
        if self.counter[val] == 1:
            self.count += 1
    def remove(self, val):
        self.counter[val] -= 1
        if self.counter[val] == 0:
            self.count -= 1


class Solution:
    def subarraysWithKDistinct(self, A, K: int):
        window = Window()
        left = right = count =  0
        
        for val in A:
            window.add(val)
            if window.count == K:
                print(window.counter)
                count += 1
            if window.count > K:
                while window.count > K:
                    window.remove(A[left])
                    left += 1
                count += 1
            

        return count

s = Solution().subarraysWithKDistinct([1,2,1,2,3], 2)
print(s)
            