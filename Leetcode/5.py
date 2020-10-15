# -*- coding: utf-8 -*-
'''
5.最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
__author__ = 'Foxlora'
__time__ = '2020/10/14 20:27'


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 初始化
        n = len(s)
        dp = [[False] * n for i in range(n)]
        ans = ''

        #枚举子串的长度
        for length in range(n):
            for i in range(n):
                j = i + length
                if j >= len(s):
                    break
                if length == 0:
                    dp[i][j]=True
                elif length == 1:
                    dp[i][j]= (s[i]==s[j])
                else:
                    if dp[i + 1][j - 1] and s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1]
                if dp[i][j] and length + 1>len(ans):
                    ans = s[i:j+1]
        return ans