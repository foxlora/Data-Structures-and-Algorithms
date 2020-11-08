# -*- coding: utf-8 -*-
'''
题目描述
给定一棵二叉树以及这棵树上的两个节点 o1 和 o2，请找到 o1 和 o2 的最近公共祖先节点。
示例1
输入
复制
[3,5,1,6,2,0,8,#,#,7,4],5,1
返回值
复制
3
'''
__author__ = 'Foxlora'
__time__ = '2020/11/8 9:58'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
#
# @param root TreeNode类
# @param o1 int整型
# @param o2 int整型
# @return int整型
#
class Solution:
    #https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/mian-shi-ti-68-ii-er-cha-shu-de-zui-jin-gong-gon-7/
    def lowestCommonAncestor(self, root:TreeNode, p, q):
        if not root or root.val == p or root.val == q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if not left:
            return right
        if not right:
            return left
        return root



    def get_node_trace(self,root:TreeNode,node:TreeNode):
        '''
        获取树中某一节点的正向路径：从根节点->node
        '''
        res = []
        def backtrack(root,path,node):
            if root.val == node.val:
                return res.append(path)
            if root.left:
                backtrack(root.left,path +[root.left.val],node)
            if root.right:
                backtrack(root.right,path+[root.right.val],node)

        backtrack(root,[root.val],node)
        print(res)

if __name__ == '__main__':
    tree = TreeNode(10)
    tree.left = TreeNode(5)
    tree.right = TreeNode(15)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(7)
    tree.right.left = TreeNode(13)
    tree.right.right = TreeNode(17)
    tree.right.right.right = TreeNode(20)

    s = Solution()
    s.get_node_trace(tree,TreeNode(17))
    a = s.lowestCommonAncestor(tree,TreeNode(1),TreeNode(20))
    print(a)



