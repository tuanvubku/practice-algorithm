class Solution:
    def subarraySum(self, nums, k: int) -> int:
        sum_ = 0
        left = 0
        cnt = 0
        if len(nums) == 1 and nums[0] != k:
            return cnt
        for val in nums:
            sum_ += val

            if sum_ == k:
                cnt += 1
            while sum_ > k:
                sum_ -= nums[left]
                left += 1
                if sum_ == k:
                    cnt += 1
        
        return cnt

s = Solution().subarraySum([1,2,3],3)
print(s)
                

        