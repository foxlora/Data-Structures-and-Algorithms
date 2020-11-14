# -*- coding: utf-8 -*-
'''
剑指 Offer 31. 栈的压入、弹出序列
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。



示例 1：

输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
示例 2：

输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。


提示：

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed 是 popped 的排列。
注意：本题与主站 946 题相同：htt
'''
__author__ = 'Foxlora'
__time__ = '2020/11/13 17:20'

class Solution():

    def allSeq(self,num:list):
        '''
        显示所有的合理出栈顺序
        这题是递归、回溯的思想，对于当前元素，只有2种操作：
        (1) 进栈，处理下一个元素
        (2) 栈非空，栈顶元素出栈，继续处理当前元素
        '''
        stack = []
        poped = []#已经出栈的元素
        n = len(num)
        def dfs(k):
            if n == k:
                print(poped + list(reversed(stack)))

                return

            #当前元素入栈
            stack.append(num[k])
            dfs(k +1)

            stack.pop()#回溯

            #第二种情况
            if stack:
                tmp = stack.pop()
                poped.append(tmp)
                dfs(k)

                poped.pop()#回溯
                stack.append(tmp)

        dfs(0)


    def validateStackSequences(self, pushed: list, popped: list) -> bool:
        '''

        '''
        a = []
        i = 0
        for val in pushed:
            a.append(val)
            while a and a[-1] == popped[i]:
                a.pop()
                i += 1
        return not a

if __name__ == '__main__':
    s= Solution()
    s.allSeq([1,2,3,4,5])