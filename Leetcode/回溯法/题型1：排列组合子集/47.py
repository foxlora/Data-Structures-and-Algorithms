# -*- coding: utf-8 -*-
'''
给定一个可包含重复数字的序列，返回所有不重复的全排列。

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
__author__ = 'Foxlora'
__time__ = '2020/10/19 15:47'

class Solution:
    def permuteUnique(self, nums) :
        nums.sort()
        n = len(nums)
        res = []
        used = [0]*n
        def backtrack(k,perm):
            '''
            perm:当前排列
            '''

            if k == n:
                res.append(perm)
            else:
                for i in range(n):

                    #剪枝
                    #对于排序重复数组，如果本数字和前面的那个数字重复，而且前面数字没有被使用过
                    if used[i] == 1:
                        continue
                    if i > 0 and nums[i] == nums[i-1] and used[i-1] == 0:
                        continue
                    used[i] = 1

                    backtrack(k+1,perm+[nums[i]])
                    used[i] = 0


        backtrack(0,[])
        return res
if __name__ == '__main__':
    s = Solution()
    a = s.permuteUnique([1,1,2])
    print(a)