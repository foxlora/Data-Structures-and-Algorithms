'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。
'''
import itertools
class Solution:
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            res += [[i] + num for num in res]
        return res

    #思路2 递归
    def subsets2(self, nums):
        if not nums:
            return [[]]
        u = nums[-1]
        return [[u] + i for i in self.subsets2(nums[:-1])] + self.subsets2(nums[:-1])

    #思路3 回溯
    def subsets3(self, nums):
        res = []
        n = len(nums)

        def helper(i,tmp):
            res.append(tmp)
            for j in range(i,n):
                helper(j+1,tmp+[nums[j]])

        helper(0,[])
        return res

    #回溯法2
    def subsets4(self, nums):
        res = []
        self.helper(nums,0,[],res)
        return res

    def helper(self,nums,start,path,res):
        res.append(path[:])
        for i in range(start,len(nums)):
            path.append(nums[i])
            self.helper(nums,i+1,path,res)
            path.pop()



s = Solution()
a = s.subsets4([1,2,3])
print(a)
