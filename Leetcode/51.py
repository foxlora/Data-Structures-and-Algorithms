# -*- coding: utf-8 -*-
'''
经典八皇后问题，回溯算法
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
__author__ = 'Foxlora'
__time__ = '2020/10/19 11:09'

class Solution:
    def solveNQueens(self, n):
        res = []
        queens = [-1]*n #记录每一行放置皇后的列下标
        columns = set()
        diag1 = set()
        diag2 = set()
        row = ["."] * n

        def backtrack(row:int):
            if row == n:
                res.append(queens[:])
            else:
                #遍历所有的列
                for i in range(n):
                    #如果不符合放置条件，继续判断row行的下一列i + 1
                    if i in columns or row - i in diag1 or row + i in diag2:
                        continue
                    #如果符合放置条件，记录下当前放置的位置queens中,判断下一行放置的位置
                    queens[row] = i

                    columns.add(i)
                    diag1.add(row - i)
                    diag2.add(row +i)


                    backtrack(row + 1)

                    queens[row] = -1
                    columns.remove(i)
                    diag1.remove(row - i)
                    diag2.remove(row + i)



        backtrack(0)
        return res

if __name__ == '__main__':
    s = Solution()
    a = s.solveNQueens(4)

    print(a)
