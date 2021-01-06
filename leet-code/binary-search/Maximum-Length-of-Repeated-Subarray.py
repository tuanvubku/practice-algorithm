"""
leetcode 718:  Maximum Length of Repeated Subarray
"""

# Approach 1: sliding window
import logging
# class Solution:
#     def findLength(self, A, B) -> int:
#         out = 0
#         a = len(A)
#         b = len(B)
#         print("Length A: %f;  Leng B: %f, Leng A + B: %f" % (a,b , a+ b))
#         for i in range(a + b - 1):
#             print("==============new for=================")
#             logging.warning("Start FOR loop: ")
#             print("Gia tri i = %f" % (i))
#             sA = max(0, a - 1 - i)
#             print(" a- 1 - i = %f; sA = %f"% ( a -1 - i, sA) )
#             sB = max(0, i - a + 1)
#             print(" i - a + 1 = %f; sB = %f"% ( i - a + 1, sB) )
#             cnt = 0

#             #sliding
#             while sA < a and sB < b:
#                 print("==============new while=================")
#                 logging.warning("Start WHILE loop: ")
#                 print("Gia tri sA, sB trong while: sA = %f, sB = %f" % (sA,sB))
#                 print("Compare value A[sA] = %f and B[sB] = %f" % (A[sA], B[sB]))
#                 if A[sA] == B[sB]:
#                     print("Co EQUALLLLL")
#                     cnt += 1 
#                     out = max(cnt, out)
#                 else:
#                     cnt = 0
#                 sA += 1
#                 sB += 1
#         return out

# s = Solution()

# slide 2

s = Solution()
print(s.findLength([1,2,3,2,4,10], [0,3,2]))