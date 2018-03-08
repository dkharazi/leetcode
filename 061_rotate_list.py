# -*- coding: utf-8 -*-
"""
61. Rotate List

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

http://www.cnblogs.com/zuoyuan/p/3785465.html

由于k值有可能比链表长度大很多，
所以先要用一个count变量求出链表的长度。
而k%count就是循环右移的步数。
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if k == 0 or head is None:
            return head

        dummy = p = ListNode(0)
        dummy.next = head
        count = 0
        while p.next:
            p = p.next
            count += 1
        # after while loop, p points to last node (before None).
        # redirect last node to head. now it's a circle
        # p.next = head
        p.next = dummy.next

        # mod in case k is larger than length of list
        step = count - (k % count)
        # move p to the node to break
        for _ in range(0, step):
            p = p.next
        # new head point to the next node
        head = p.next
        # current node point to None
        p.next = None
        return head
