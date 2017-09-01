# -*- coding: utf-8 -*-
# 147. Insertion Sort List
#
# Sort a linked list using insertion sort.
#


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        https://shenjie1993.gitbooks.io/leetcode-python/147%20Insertion%20Sort%20List.html
        数组的插入排序很简单，将元素依次放入已经排好序的数组中的正确位置。
        链表与数组的操作稍微有些不同，
        数组是将比要插入的元素大的数值往后移，直到遇到比该元素小的值，就把该元素放在比它小的值后面。
        但单链表只能从头开始判断新的节点该插入到哪里。
        链表也可以根据尾节点进行优化，如果要插入的节点比尾节点还大的话，就不用从头开始找插入的位置了。
        插入时要注意链表插入操作，Python写链表相关操作还是很方便的。

        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        cur = dummy
        while head:
            if cur and cur.val > head.val:
                cur = dummy
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            cur.next, cur.next.next, head = head, cur.next, head.next
        return dummy.next

    # http://www.cnblogs.com/zuoyuan/p/3700105.html
    def insertionSortList(self, head):
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        curr = head
        while curr.next:
            if curr.next.val < curr.val:
                pre = dummy
                while pre.next.val < curr.next.val:
                    pre = pre.next
                tmp = curr.next
                curr.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                curr = curr.next
        return dummy.next
