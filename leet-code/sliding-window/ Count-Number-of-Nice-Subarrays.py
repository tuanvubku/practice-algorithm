from collections import Counter

class Window():
    def __init__(self):
        self.count_odd = 0

    def add(self, val):
        if (val % 2 ) != 0:
            self.count_odd += 1
    def remove(self, val):
        if (val % 2 ) != 0:
            self.count_odd -= 1

class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        window1 = Window()
        window2 = Window()
        left1 = left2 = ans = 0
        for right in nums:
            window1.add(right)
            window2.add(right)

            # window1 only hold K value
            while window1.count_odd > k:
                window1.remove(nums[left1])
                left1 += 1
            
            while window2.count_odd >= k:
                window2.remove(nums[left2])
                left2 += 1
            
            ans += left2 - left1
    
        return ans

s = Solution().numberOfSubarrays([1,2,4,2,3], 2)
print(s)
