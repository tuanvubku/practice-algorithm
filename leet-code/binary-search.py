"""
Tại sao hay sử dụng mid = left + (right - left)/2 mà không sử dụng mid = (right + left) / 2


"""

arr = [7,10,15]

# bisec left: find index left : tìm vị trị thích hợp bên trái cho phần tử cần chèn 
# bisec right: find index right: tìm vị trí thích hợp bên phải cho phần tử cần chèn

# def bisec_left(arr, value):
#     left = 0
#     right = len(arr) - 1
#     print("Len: ", len(arr))
#     mid = -1
#     #print(right)
#     while left < right:
#         mid = (right + left) // 2
#         print("Mid  ", mid)
#         # if arr[mid] == value:
#         #     return mid
#         if arr[mid] < value:
#             # print("arr[mid] = ",arr[mid], "> ", "value = ", value)
#             # print("right = mid = ", mid - 1)
#             left = mid + 1
#         else:
#             # print("arr[mid] = ",arr[mid], "<= ", "value = ", value)
#             # print("Left = mid = ", mid)
#             right = mid 
#     print("LEft final: ", left)
#     return left if arr[left] == value else -1
# print(bisec_left(arr, 65))
#print(1 + (2 -1) //2)
# class BS:
#     def __init__(self, lst) -> None:
#         self.lst = lst

# left = 0
# right = 11

# mid = (left + right) // 3
# _mid = (left + right) / 3
# print(mid, _mid)

def bisect_right(arr, target, lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        # left-most, so equal will be on the right side
        # if arr[mid] < target:
        #     lo = mid + 1
        # else:
        #     hi = mid
        '''
        # bisect right code
        '''
        if arr[mid] > target:
            hi = mid
        else:
            lo = mid + 1
        
    return lo