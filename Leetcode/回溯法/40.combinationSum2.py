'''
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.helper(candidates,target,-1,0,[],res)
        return res

    def helper(self,candidates,target,p,cur_sum,path,res):
        if cur_sum == target:
            res.append(path[:])
            # if path[:] not in res:
            #     res.append(path[:])
        elif cur_sum < target:

            for j in range(p+1,len(candidates)):
                if cur_sum + candidates[j] > target:
                    break
                if j>0 and candidates[j] == candidates[j - 1]:
                    continue
                self.helper(candidates,target,j,cur_sum+candidates[j],path+[candidates[j]],res)


s = Solution()
a = s.combinationSum2([1,1,2,3,5,6,7],8)
print(a)