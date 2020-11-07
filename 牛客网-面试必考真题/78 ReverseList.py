# -*- coding: utf-8 -*-
'''
输入一个链表，反转链表后，输出新链表的表头。
输入
复制
{1,2,3}
返回值
复制
{3,2,1}
'''
__author__ = 'Foxlora'
__time__ = '2020/11/6 20:37'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead

        pre = None
        while pHead:
            cur = pHead
            pHead = pHead.next
            cur.next = pre
            pre = cur


        return cur