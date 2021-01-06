"""

"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        for i in range(len(s) - k, -1, -1):

            #check from i to end
            if s[i] * k == s[i:i+k]:
                #remove k element same
                s = s[:i] + s[i+k:]
        return s

s = Solution().removeDuplicates("dtpdtaaaaaaaaappppppppppppppppppppaaaaaaaaaaxxxxxxxxxxxxxxsssssssssjjjjjjjjjjjjjjjjjjjjxxxxxxxxxxxxxxxxxxxxsssssssjjjjjjjjjjjjjjjjjjjjssssxxxxxxatdwvvpctpggggggggggggggggggggajagglaaaaaaaaaaaaaaaaaaaa", 20)
print(s)

