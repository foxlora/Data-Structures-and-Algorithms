# -*- coding: utf-8 -*-
'''
. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
__author__ = 'Foxlora'
__time__ = '2020/10/14 19:44'

import pprint

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "{} -> {}".format(self.val, self.next)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and not l2:
            return l1
        if not l1:
            return l2

        dummy = ListNode(0)
        pre = dummy
        # 如果都没到底
        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next

            pre = pre.next

        pre.next = l1 if l1 else l2

        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next =ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next =ListNode(3)
    l2.next.next = ListNode(4)

    s = Solution()
    res = s.mergeTwoLists(l1,l2)
    print(res)