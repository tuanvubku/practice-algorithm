from collections import Counter
from collections import defaultdict
#from bisect import bisect_left
# a = "abc"
# counter = Counter(a)
# counter['a'] -= 1

# print(list(counter.elements()))
# print('a' in counter)
# print(counter)

# dic = [[3,10]]
# for x,y in dic:
#     print(x,y)

# dic = [1,3,4,10]
# d = {}
# for i,v in enumerate(dic):
#     d[v] = i
# print(d["3"])

# _str = "aabccfa"
# cnt = Counter(_str)
# print(cnt)
# # most_commom return list so we can access with index
# print(cnt.most_common())

# lst = [1,3,4,5,53,4,3]

# # c = Counter()
# # for v in lst:
# #     c[v] += 1
# # print(c)

# d = defaultdict(int)
# for v in lst:
#     d[v] += 1
# print(d[1])

# stack = [1]
# while stack:
#     print("1")
# def bisect_left(arr, target, lo, hi):
#     while lo < hi:
#         mid = (lo + hi) // 2
#         # left-most, so equal will be on the right side
#         if arr[mid] < target:
#             lo = mid + 1
#         else:
#             hi = mid
#         '''
#         # bisect right code
#         if arr[mid] > target:
#             hi = mid
#         else:
#             lo = mid + 1
#         '''
#     return lo

# arr = [1,3,5,10]
# print(bisect_left(arr,0,0, len(arr) ))

# dic1 = {
#     "a": 1,
#     "b": 2,
#     "c": 3 
# }
# dic2 = {
#     10: 10,
#     2: 5,
#     7: 3
# }

# # so sanh == with dictionary: so sanh each value of each dic
# print(dic1 == dic2)

# print(sorted([dic2[l] for l in dic2]))

# print(sorted(dic2))

# default 0 cho all keys

q = [2,3,4,5,1]
# a = q.pop(0)
b = q[::]
b[0] = 100
print(q)
print(b)
# print(q)