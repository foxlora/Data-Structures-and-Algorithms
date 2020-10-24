# Data-Structures-and-Algorithms
算法总结，慢慢更新

## 一、链表

    ```
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    ```

步骤：

1. 建立假节点

   ```
   dummy = ListNode(0)
   ```

2. 建立游标

   ```
   pre = dummy
   ```

   

3. 逻辑处理

4. 返回dummy.next



可以用到的思想：

快慢指针




## 二、动态规划

1. 转移方程

   p[i,j] 与p[i -1,j+1]的关系

2. 边界条件