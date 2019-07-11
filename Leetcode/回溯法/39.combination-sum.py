'''
Time:2019/07/10
题目描述：给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum

回溯算法
'''



class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        n = len(candidates)
        res = []

        def helper(i, tmp_sum, tmp):
            if tmp_sum > target or i == n:
                return
            if tmp_sum == target:
                res.append(tmp)
                return
            helper(i, tmp_sum + candidates[i], tmp + [candidates[i]])
            helper(i + 1, tmp_sum, tmp)

        helper(0, 0, [])
        return res

    def combinationSum2(self,candidates, target):
        res = []
        cur = []
        self.helper(candidates,0,target,0,res,cur)
        return res
    def helper(self,candidates,k,target,sum,res,cur):
        if sum == target:
            res.append(cur[:])


        elif sum > target:
            return
        else:
            for i in range(k,len(candidates)):
                if sum+candidates[i] > target:
                    break
                self.helper(candidates,i,target,sum+candidates[i],res,cur+[candidates[i]])



s = Solution()
a = s.combinationSum2([2,3,5],13)
print(a)