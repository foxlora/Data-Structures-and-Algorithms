'''
合并两个已排序的数组
Time：2019.06.12
Input :  arr1[] = { 1, 3, 4, 5}
         arr2[] = {2, 4, 6, 8}
Output : arr3[] = {1, 2, 3, 4, 5, 6, 8}

Input  : arr1[] = { 5, 8, 9}
         arr2[] = {4, 7, 8}
Output : arr3[] = {4, 5, 7, 8, 8, 9}
'''

#合并重复元素
def merge_two_sorted_arrays(arr1,arr2):
    p1,p2 = 0,0
    arr3 = []
    while p1 < len(arr1) and p2 < len(arr2) :
        if arr1[p1] > arr2[p2]:
            arr3.append(arr2[p2])
            p2 += 1
        elif arr1[p1] == arr2[p2]:
            arr3.append(arr1[p1])
            p2 += 1
            p1 += 1
        else:
            arr3.append(arr1[p1])
            p1 += 1


    if p1 == len(arr1) and p2 < len(arr2):
        arr3.extend(arr2[p2:])

    if p2 == len(arr2) and p1 < len(arr1):
        arr3.extend(arr1[p1:])
    return arr3




arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 6, 8]
arr3 = merge_two_sorted_arrays(arr1,arr2)


print(arr3)