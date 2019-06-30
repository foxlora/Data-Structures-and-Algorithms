'''
快速排序 四种方法
堆排序
冒泡排序
归并排序
'''

#不开辟新空间 第二种
def quicksort(arr,start,end):
    if start >= end:
        return
    low = start
    high = end

    key = arr[start]

    while low < high:
        while low < high and arr[high] >= key:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] <= key:
            low += 1
        arr[high] = arr[low]



    arr[low] = key

    quicksort(arr,start,low-1)
    quicksort(arr,low + 1,end)
    return arr

#第三种，算法导论，采用分区函数
#定义分区函数
def partition(arr,low,high):
    position = low - 1
    for i in range(low,high):
        if arr[i] <= arr[high]:
            position += 1
            arr[i],arr[position] = arr[position],arr[i]
    #分成两个列表[low,position]<=key [position+1:]>key
    arr[position + 1],arr[high]=arr[high],arr[position + 1]
    return position

def quicksort_partition(arr,low,high):
    if low < high:
        p = partition(arr,low,high)
        quicksort_partition(arr,low,p)
        quicksort_partition(arr,p+2,high)

#第四种 迭代法
def quicksort_iter(arr,low,high):
    s = []
    s.append((low,high))
    while s:
        u = s.pop()
        left,right = u[0],u[1]
        if left < right:
            p = partition(arr,left,right)
            s.append((left,p))
            s.append((p+2,right))


a = [5,3,4,7,8]
quicksort_iter(a,0,len(a)-1)
print(a)


#简单版本
def quicksort1(arr):
    if len(arr)<2:
        return arr
    arr1 = []
    arr2 = []
    for i in arr[1:]:
        if i < arr[0]:
            arr1.append(i)
        else:
            arr2.append(i)
    return quicksort1(arr1) + [arr[0]] + quicksort1(arr2)




'''
冒泡排序算法的运作如下： 
1、比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。

2、对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。

3、针对所有的元素重复以上的步骤，除了最后一个。

4、持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

'''

def bubblesort(arr):
    n = len(arr)

    for j in range(n - 1):
        count = 0
        # 从前往后进行比较相邻元素
        for i in range(n - j - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                count += 1



        if count == 0:
            break
    return arr












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
    return array




def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge_two_sorted_arr(left,right)

def merge_two_sorted_arr(left,right):
    res = []

    p1 = 0
    p2 = 0
    while p1 < len(left) and p2 < len(right):
        if left[p1] <= right[p2]:
            res.append(left[p1])
            p1 += 1
        else:
            res.append(right[p2])
            p2 += 1

    res += left[p1:]
    res += right[p2:]


    return res


