'''
排序数组，找到数字K第一次和最后一次出现的位置

'''
def find_first_index(arr,k):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right)//2

        if k <= arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    if arr[left] == k:
        return left
    else:
        print(k,'is not in arr')

def find_last_index(arr,k):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) //2
        if k < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return right



a = find_first_index([1,2,5,6,7],5)
print(a)


