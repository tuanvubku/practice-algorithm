### Some built-in function using in python for solving problem

### dictionary
# dict = {} 
# defaultdict
# counter
from collections import defaultdict

## Create a defaultdic, pass the argument which is type of value in defauldict also default value
#  if int --> default = 0, if list -> []
a = defaultdict(int)
a['2']= 10
# if don't have key, defaultdict set key = default value
# add new keys to the dict when you query for missing keys
#print(a['3'])
# {'2': 10, '3': 0}

## dict in Python
d = {}
# two method same to defaultdict
name = d.setdefault("name", "Tuan vu")
#print(d.get("age",18))

# defaultdict want to get most common like Counter have to use sort method

## Counter
from collections import Counter
c = Counter()
c = Counter('aabbbbbbbcc')
# print(c)
# print(c.most_common(2))
# print(list(c.elements()))


### Binary search
# bisec
from bisect import bisect_left, bisect_right, bisect
lst = [[1,3],[5,10],[15,20]]
# find index to insert into list
bs_left = bisect_right(lst,[15, float('-inf')])

# bisec same bisec_right
# bs_right = bisect_right(lst, 3)
# bs = bisect(lst, 3)

print(bs_left)
### Heap queue
# heapq

a= [1,2,2,3,4]
print(set(tuple(a[1:1+2])))


# implement Counter

arr = ["A","A","B","B","B","C"]

# dic = defaultdict(int)

# max_cnt = 0
# res = None
# for c in arr:
#     dic[c] += 1
    
#     if dic[c] > max_cnt:
#         max_cnt = dic[c]
#         res = c

# return res