# 求最长回文串类
class LPS:
    # 初始化，需要提供一个字符串
    def __init__(self, string):
        self.string = string
        self.lens = len(self.string)

    # 暴力枚举：作为算法效率参照
    def brute_force(self):
        maxcount = 0
        for j in range(self.lens):
            for k in range(j, self.lens):
                count = 0
                l, m = j, k
                while m >= l:
                    if self.string[l] == self.string[m]:
                        l, m = l + 1, m - 1
                    else:
                        break
                if m < l:
                    count = k - j + 1
                if count > maxcount:
                    maxcount = count
                    lps = self.string[j:k+1]
        return maxcount,lps

    # 优化版：枚举子串中心
    def brute_force_opti(self):
        maxcount = 0
        if self.lens == 1:  # 只有一个字符直接返回1
            return 1
        for j in range(self.lens - 1):  # 枚举中心
            count, u = 1, j
            if self.string[j] == self.string[j + 1]:  # 处理偶数子串，将两个相邻相同元素作为整体
                u, count = j + 1, 2
            for k in range(1, j + 1):  # 两边扩展
                l, m = u + k, j - k
                if (m >= 0) & (l < self.lens):
                    if (self.string[l] == self.string[m]):
                        count += 2
                    else:
                        break
            if count > maxcount:  # 更新回文子串最长长度
                maxcount = count
        return maxcount

    # manacher算法
    def manacher(self):
        s = '#' + '#'.join(self.string) + '#'  # 字符串处理，用特殊字符隔离字符串，方便处理偶数子串
        lens = len(s)
        f = []  # 辅助列表：f[i]表示i作中心的最长回文子串的长度
        maxj = 0  # 记录对i右边影响最大的字符位置j
        maxl = 0  # 记录j影响范围的右边界
        maxd = 0  # 记录最长的回文子串长度
        for i in range(lens):  # 遍历字符串
            if maxl > i:
                count = min(maxl - i, int(f[2 * maxj - i] / 2) + 1)  # 这里为了方便后续计算使用count，其表示当前字符到其影响范围的右边界的距离
            else:
                count = 1
            while i - count >= 0 and i + count < lens and s[i - count] == s[i + count]:  # 两边扩展
                count += 1
            if (i - 1 + count) > maxl:  # 更新影响范围最大的字符j及其右边界
                maxl, maxj = i - 1 + count, i
            f.append(count * 2 - 1)
            maxd = max(maxd, f[i])  # 更新回文子串最长长度
        return int((maxd + 1) / 2) - 1  # 去除特殊字符



str1 = LPS('ZHOUUOHUI')

print(str1.manacher())