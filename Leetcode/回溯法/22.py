# -*- coding: utf-8 -*-
'''
括号生成数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
__author__ = 'Foxlora'
__time__ = '2020/10/22 13:54'

class Solution:
    def generateParenthesis(self, n: int):
        symbol = ["(",")"]
        res = []
        def backtrack(s,path:str):
            if s == 2*n:
                res.append(path)
            #两个条件
            #path中（个数 <= n
            #path中 （个数 >= ）个数
            for i in symbol:
                if i == "(" and path.count("(") < n:
                    backtrack(s+1,path+i)
                if i == ")" and path.count("(") > path.count(")"):
                    backtrack(s+1,path+i)

        backtrack(0,"")
        return res

if __name__ == '__main__':
    s = Solution()
    a = s.generateParenthesis(3)
    print(a)