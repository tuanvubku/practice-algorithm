class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        left = 0
        right = 0
        sum_ = 0   
        length = -1
        min_length = float("inf")
        while right < len(nums) and right :
            sum_ += nums[right]
            if sum_ >= s:
                length = right - left + 1
                min_length = min(length, min_length)
                sum -= nums[left]
                right += 1
                left += 1
                sum_ = 0
            else:
                right += 1
        return min_length if min_length != float("inf") else 0

s = Solution().minSubArrayLen(4, [4,5,6])
print(s)