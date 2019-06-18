#
# def bubble_sort(array):
#     for i in range(len(array)-1):
#         for j in range(len(array) - i -1):
#             if array[j] > array[j+1]:
#                 array[j],array[j+1] = array[j+1],array[j]
#
#
# if __name__ == '__main__':
#     list = input()
#     print(list)
#     a = bubble_sort(list)
#     print(a)
#
'''冒泡排序'''
def bubble_sort(array):
     for i in range(len(array)-1):
         for j in range(len(array) - i -1):
             if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
     print(array)



'''冒泡排序改善，如果没有改变位置，则退出'''
def bubble_sort_1(array):
    for j in range(len(array) - 1):
        current_status = True
        for k in range(len(array)- j - 1):
            if array[k] > array[k+1]:
                array[k],array[k+1] = array[k+1],array[k]
                current_status = False
        if current_status:
            break
    print(array)


"直接选择排序"
def select_sort(array):
    for i in range(len(array)-1):
        for j in range( i+1, len(array)):
            if array[j] < array[i]:
                array[i],array[j] = array[j],array[i]
    print(array)


'''直接插入排序'''
def insert_sort(array):
    for i in range(1,len(array)):
        k = array[i]
        j = i - 1
        while j>=0 and array[j] > k:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = k
    print(array)

'''快速排序'''
#def quck_sort(array):
quick_sort0 = lambda array: array if len(array) <= 1 else quick_sort(
        [item for item in array[1:] if item <= array[0]]) + [array[0]] + quick_sort(
        [item for item in array[1:] if item > array[0]])

def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]

    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[left] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)
    print(array)


'''堆排序'''
def sift(array, left, right):
    """调整"""
    i = left      # 当前调整的小堆的父节点
    j = 2*i + 1   # i的左孩子
    tmp = array[i]     # 当前调整的堆的根节点
    while j <= right:    # 如果孩子还在堆的边界内
        if j < right and array[j] < array[j+1]:   # 如果i有右孩子,且右孩子比左孩子大
            j = j + 1                              # 大孩子就是右孩子
        if tmp < array[j]:                         # 比较根节点和大孩子，如果根节点比大孩子小
            array[i] = array[j]                     # 大孩子上位
            i = j                                   # 新调整的小堆的父节点
            j = 2*i + 1                             # 新调整的小堆中I的左孩子
        else:                                       # 否则就是父节点比大孩子大，则终止循环
            break
    array[i] = tmp                                  # 最后i的位置由于是之前大孩子上位了，是空的，而这个位置是根节点的正确位置。


def heap(array):
    n = len(array)
    # 建堆，从最后一个有孩子的父亲开始，直到根节点
    for i in range(n//2 - 1, -1, -1):
        # 每次调整i到结尾
        sift(array, i, n-1)
    # 挨个出数
    for i in range(n-1, -1, -1):
        # 把根节点和调整的堆的最后一个元素交换
        array[0], array[i] = array[i], array[0]
        # 再调整，从0到i-1
        sift(array, 0, i-1)
    print(array)

heap([5,3,4,7,8])
