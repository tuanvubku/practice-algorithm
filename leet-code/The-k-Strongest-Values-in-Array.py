"""

"""

class Solution:
    def getStrongest(self, arr, k: int):
        arr.sort()
        print(arr)
        res = []

        median = (len(arr) - 1) // 2 

        low = 0
        high = -1
    
        while k > 0:
            if abs(arr[high] - arr[median]) >= abs(arr[median] - arr[low]):
                res.append(arr[high])
                high -= 1
            else: 
                res.append(arr[low])
                low += 1
            k -= 1
        return res
           
s = Solution().getStrongest([-2,-4,-6,-8,-9,-7,-5,-3,-1], 3)
print(s)