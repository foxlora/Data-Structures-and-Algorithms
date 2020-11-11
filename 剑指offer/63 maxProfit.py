# -*- coding: utf-8 -*-
'''
剑指 Offer 63. 股票的最大利润
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？



示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。


限制：

0 <= 数组长度 <= 10^5


'''
__author__ = 'Foxlora'
__time__ = '2020/11/11 17:03'


class Solution:
    def maxProfit(self, prices) -> int:
        dpi10 = 0  # 第0天
        dpi11 = float('-inf')
        dpi20 = 0
        dpi21 = float('-inf')

        for price in prices:
            dpi20 = max(dpi20, dpi21 + price) #昨天卖出，今天不变  | 昨天有股票，今天卖出
            dpi21 = max(dpi21, dpi10 - price)

            dpi10 = max(dpi10, dpi11 + price)
            dpi11 = max(dpi11, -price)

        return dpi20

if __name__ == '__main__':
    a = [3, 3, 5, 0, 0, 3, 1, 4]
    s = Solution().maxProfit(a)
    print(s)