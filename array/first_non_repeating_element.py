#查找第一个没有重复的数组元素

def first_non_repeating_element(arr):
    repeat = set()
    for index, i in enumerate(arr):

        if i not in arr[index+1:] and i not in repeat:
            return i

        repeat.add(i)

    return -1




from collections import defaultdict

def first_non_repeating_element_1(arr):
    d = defaultdict(int)
    for k in arr:
        d[k] += 1
    for key,value in d.items():
        if value == 1:
            return key


arr = [9,4,9,6,7,4]

print(first_non_repeating_element_1(arr))

