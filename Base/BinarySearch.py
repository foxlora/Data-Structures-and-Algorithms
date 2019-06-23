'''
实现二分查找
Time：2019-6-24
关键点：判定条件，边界
循环的判定条件是：low <= high
'''

def binary_search(key,array):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right)//2
        if array[mid] > key:
            right = mid -1
        elif array [mid] < key:
            left = mid + 1
        else:
            return mid

    return False




'''

2. 查找目标值区域的左边界/查找与目标值相等的第一个位置/查找第一个不小于目标值数的位置
A = [1,3,3,5,7,7,7,7,8,14,14]
target = 7
return 4

'''
def binary_search_1(target,array):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right)//2
        if array[mid] >= target:
            right = mid -1
        else:
            left = mid + 1

    if array[left] == target:
        return left
    else:
        return -1




'''
3.查找旋转数组的最小元素（假设不存在重复数字）
LeetCode: Find Minimum in Rotated Sorted Array
Input: [3,4,5,1,2]
Output: 1
'''
def binary_search_2(array):
    left = 0
    right = len(array) - 1
    while left < right:
        mid = (left + right)//2
        if array[mid] > array[left]:
            left = mid + 1
        else:
            right = mid

    return array[right]

'''
4.查找旋转数组的最小元素（存在重复项）
LeetCode: Find Minimum in Rotated Sorted Array II
剑指offer：旋转数组的最小数字
Input: [2,2,2,0,1]
Output: 0
'''
def binary_search_3(array):
    if not array:
        return 0
    left = 0
    right = len(array) - 1
    while left < right:
        mid = (left + right)//2
        if array[mid] > array[right]:
            left = mid + 1
        elif array[mid] < array[right]:
            right = mid
        else:
            right -= 1
    return array[right]



a = [3,4,5,1,2]
print(binary_search_3(a))
