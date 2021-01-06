class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        if not nums :
            return False
        
        cache = {0: -1}
        surplus = 0
        for i in range(len(nums)):
            if k != 0:
                surplus =  (surplus + nums[i]) % k
            else:
                surplus =  surplus + nums[i]
            print(cache)
            if surplus in cache:
                if i - cache[surplus] > 1:
                    return True
            else:
                cache[surplus] = i
                
        return False

s = Solution().checkSubarraySum([0,0],0)