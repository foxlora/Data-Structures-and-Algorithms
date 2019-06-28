'''
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
'''

class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        res = []
        self.helper(ss, res, '')
        return sorted(list(set(res)))

    def helper(self, ss, res, path):
        if not ss:
            res.append(path)
        else:
            for i in range(len(ss)):
                self.helper(ss[:i] + ss[i+1:], res, path + ss[i])

    def helper_iter(self,ss,res,path):
        if not ss:
            res.append(path)
        s = [ss]
        while s:
            u = s.pop()
            for i in range(len(u)):
                s.append(ss[:i] + ss[i+1:])


s = Solution()
b = s.Permutation('xlf')
print(b)
