# -*- coding: utf-8 -*-
'''

'''
__author__ = 'Foxlora'
__time__ = '2020/11/8 18:09'
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        max_num = float('-inf')
        min_num = float('inf')
        def helper(node):
            if not node:
                return (True,max_num,min_num)

            left,left_max, = helper(node.left)
            right,right_max = helper(node.right)
            return (left and right and left_max <= node.val ,max(node.val,right_max))

        a = helper(root)
        print(a)



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
    s.isValidBST(tree)