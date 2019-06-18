# -*- coding:utf-8 -*-

"""
利用并查集计算一个图的连通分量数目
"""

class UnionFindSet(object):
    """
    实现一个并查集
    """
    def __init__(self, m_nN):
        self.m_nN = m_nN
        self.m_pParent = [i for i in range(m_nN)]


    def find(self, i):
        """
        找到节点i最终的父节点。
        该查找改变了原数组。
        :param i:
        :return:
        """
        if i < 0 or i >= self.m_nN:
            return -1

        root = i
        while root != self.m_pParent[root]:   # 尚未找到根节点
            root = self.m_pParent[root]

        # 路径压缩（只要查找过一次，路径就被压缩为1）
        t = i
        while t != root:
            p = self.m_pParent[t]
            self.m_pParent[t] = root
            t = p

        return root


    def find2(self, i):
        """
        和find等价，递归实现。
        :param i:
        :return:
        """
        if i != self.m_pParent[i]:
            self.m_pParent[i] = self.find2(self.m_pParent[i])
        return self.m_pParent[i]


    def union(self, i, j):
        """
        合并一条边的节点i和j
        :param i:
        :param j:
        :return:
        """
        if i < 0 or i >= self.m_nN or j < 0 or j > self.m_nN:
            return
        ri = self.find(i)
        rj = self.find(j)
        if ri != rj:
            self.m_pParent[ri] = rj


def calcCompoment():
    """
    计算一个图的连通分量数目
    :return:
    """
    N = 10
    ufs = UnionFindSet(N)
    ufs.union(2, 6)
    ufs.union(5, 6)
    ufs.union(1, 8)
    ufs.union(2, 9)
    ufs.union(5, 3)
    ufs.union(4, 8)
    ufs.union(4, 0)


#查询有多少颗树
    component = [0] * N
    for i in range(N):
        component[ufs.find(i)] += 1
        print(component)

    nComponent = 0
    for i in range(N):
        if component[i] != 0:
            nComponent += 1
    return nComponent


if __name__ == '__main__':
    print(calcCompoment())