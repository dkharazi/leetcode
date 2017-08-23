# -*- coding: utf-8 -*-
"""
82. Remove Duplicates from Sorted List II

Given a sorted linked list,
delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

http://blog.csdn.net/hyperbolechi/article/details/43526043

这题的做法是用两个指针pre cur
1.dummy.next= head
2.pre=dummy cur=dummy.next
3.当指针移到 pre.next 和cur.next 不等的位置 将这个位置加入到 pre.next中去
4.否者就跳过cur
一次遍历 时间是O(n)
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

    def __repr__(self):
        return "{} -> {}".format(self.val, self.next)


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = dummy.next

        while curr:
            # while curr.next.val == prev.next.val:
            while curr.next and curr.next.val == prev.next.val:
                curr = curr.next
            # if nothing happens, move prev together with curr
            if prev.next == curr:
                prev = prev.next
            # else link prev to node behind curr
            else:
                prev.next = curr.next
            curr = curr.next

        return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(1)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(3)

    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    head2.next.next.next = ListNode(3)
    head2.next.next.next.next = ListNode(4)

    print Solution().deleteDuplicates(head2)
