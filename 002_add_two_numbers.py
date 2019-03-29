"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = ""
        if self != None:
            while self.next != None:
                s += str(self.val)
                s += "->"
                self = self.next
            s += str(self.val)
        return s

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        carryover = 0
        # advance p only; dummy to remember original head
        dummy = ListNode(0); p = dummy
        while l1 and l2:
            # p.next.val is the sum of 2 node value + carryover,
            # then mod 10 to get the remainder as digit val
            p.next = ListNode((l1.val+l2.val+carryover) % 10)
            # carryover is the quotient, 0 or 1
            carryover = (l1.val+l2.val+carryover) / 10
            # advance all 3 linked lists
            l1 = l1.next; l2 = l2.next; p = p.next

        # if l1 and l2 not equal length
        # loop over the rest of the nodes
        if l2:
            while l2:
                p.next = ListNode((l2.val+carryover) % 10)
                carryover = (l2.val+carryover) / 10
                l2 = l2.next; p = p.next
        if l1:
            while l1:
                p.next = ListNode((l1.val+carryover) % 10)
                carryover = (l1.val+carryover) / 10
                l1 = l1.next; p = p.next

        # carry over last possible 1
        if carryover == 1:
            p.next = ListNode(1)

        # ignore dummy.head which is always 0.
        return dummy.next

    # https://gengwg.blogspot.com/2018/02/leoleetcode-2-add-two-numbers.html
    def addTwoNumbers(self, l1, l2):
        # dummy.next to remember list head
        dummy = p = ListNode(0)
        carry = 0
        while l1 or l2 or carry:    # <-- this
            value = 0
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            value += carry
            # create next node
            p.next = ListNode(value % 10)
            carry = value / 10
            # p point to ListNode(value%10)
            p = p.next
        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(6)
    print l1

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    # l2.next.next.next = ListNode(2)
    print l2

    dummy = Solution().addTwoNumbers(l1, l2)
    print dummy
