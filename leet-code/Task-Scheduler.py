"""

"""
from collections import Counter, defaultdict
class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        max_freq, interval, cnt = 0,0,0
        freq = defaultdict(int)
        for t in tasks:
            freq[t] += 1
            print("CURRENT MAX_FREQ %f" % (max_freq))
            print("FRequent[%s] = %f" % (t, freq[t]))
            if freq[t] > max_freq:
                print("if FREQUENT[%s] = %f > MAX_FREQ = %f" % (t,freq[t], max_freq))
                
                max_freq = freq[t]
                print("MAX REQUENT ", max_freq)
                cnt = 1
            elif freq[t] == max_freq:
                print("ELSE CNT value = %f" % (cnt))
                cnt += 1
            print("CNT ",cnt)
            print(freq) 
            print("================================")
            print()

        print("AFTER FOR LOOP")
        print("FREQ = ", freq)
        print("CNT = %f" % (cnt))
        interval = (max_freq - 1) * (n + 1) + cnt

        return len(tasks) if interval < len(tasks ) else interval

s = Solution().leastInterval(["A", "A", "A", "B","B","C","D","E","F"], 2)

print(s)
        