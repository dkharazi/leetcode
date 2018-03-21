# 160. Intersection of Two Linked Lists
#
#  Write a program to find the node at which the intersection
# of two singly linked lists begins.
#
#
# For example, the following two linked lists:
#
# A:          a1 - a2
#                    \
#                      c1 - c2 - c3
#                    /
# B:     b1 - b2 - b3
# begin to intersect at node c1.
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
#
# Credits:
# Special thanks to @stellari for adding this problem and creating all test cases.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution:
    def getIntersectionNode(self, headA, headB):
        a = self._len(headA)
        b = self._len(headB)

        # let the longer linked list step |a-b| times first
        if a > b:
            for i in range(a - b):
                headA = headA.next
        else:
            for i in range(b - a):
                headB = headB.next

        # step at the same time on both list
        # the first identical node is their first common node
        while headA and headB:
            # This is the address of the object in memory.
            # seems not working
            # if id(headA) == id(headB):
            # to submit to leetcode, remove .val below
            if headA.val == headB.val:
                return headA.val
            headA = headA.next
            headB = headB.next

        return None

    # step both lists to get their length
    def _len(self, head):
        len = 0

        while head:
            len += 1
            head = head.next

        return len

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p = headA
        q = headB

        # get length of both lists
        lengthA = 0
        lengthB = 0
        while p:
            p = p.next
            lengthA += 1
        while q:
            q = q.next
            lengthB += 1

        # move the longer one diff steps first
        p = headA
        q = headB
        if lengthA > lengthB:
            for _ in range(lengthA - lengthB):
                p = p.next
        else:
            for _ in range(lengthB - lengthA):
                q = q.next

        # move together until equals
        while p and q:
            if p == q:
                return p
            p = p.next
            q = q.next


if __name__ == "__main__":
    headA = ListNode(1)
    headA.next = ListNode(2)
    headA.next.next = ListNode(3)
    headA.next.next.next = ListNode(6)
    headA.next.next.next.next = ListNode(7)

    headB = ListNode(4)
    headB.next = ListNode(5)
    headB.next.next = ListNode(6)
    headB.next.next.next = ListNode(7)

    print headA
    print headB
    print Solution().getIntersectionNode(headA, headB)
