'''
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
'''

class Solution:
    #递归版本1
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


    #递归版本2

    def Permutation2(self, ss):
        list = []
        if len(ss) <= 1:
            return ss
        for i in range(len(ss)):
            for j in map(lambda x: ss[i] + x,
                         self.Permutation(ss[:i] + ss[i + 1:])):
                # 生成每个排好序的字符串（lambda补全每个循环中返回字符串的头部）
                if j not in list:  # 这里的判断可以消除重复值的影响
                    list.append(j)
        return list



    def permutation_iter(self,ss):
        res = []
        if len(ss) <= 1:
            return ss
        pre = ""
        s = [(ss,pre)]
        while s:
            u,pre = s.pop()
            if not u:
                if pre not in res:
                    res.append(pre)
            for i in range(len(u)):
                s.append((u[:i] + u[i+1:],pre + u[i]))
        return res


s = Solution()
b = s.permutation_iter('xlf')
print(b)
