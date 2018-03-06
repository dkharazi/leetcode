# 234. Palindrome Linked List
#
# Given a singly linked list, determine if it is a palindrome.
#
# Follow up:
#    Could you do it in O(n) time and O(1) space?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# http://blog.csdn.net/coder_orz/article/details/51306985
class Solution(object):
    # put linked list val into an array
    # then test if array is palindrome
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        li = []
        while head:
            li.append(head.val)
            head = head.next

        # or: return li == li[::-1]
        length = len(li)
        for i in range(length/2):
            if li[i] != li[length - i - 1]:
                return False

        return True

    def isPalindrome2(self, head):
        if not head or not head.next:
            return True

        li = []
        slow = fast = head

        # use slow/fast to find middle of list
        # push first half into stack
        # must have fast.next
        while fast and fast.next:
            li.insert(0, slow.val)
            slow = slow.next
            fast = fast.next.next

        # skip testing middle element if odd number
        if fast:
            slow = slow.next

        # pop stack and compare with 2nd half
        for x in li:
            if x != slow.val:
                return False
            slow = slow.next

        return True

    # reverse 2nd half of linked list
    # Time O(1), space O(1)
    def isPalindrome3(self, head):
        if not head or not head.next:
            return True

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow = slow.next
        # slow point to 2nd half
        slow = self.reverseList(slow)

        while slow:
            if head.val != slow.val:
                return False
            slow = slow.next
            head = head.next

        return True

    def reverseList(self, head):
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
        return new_head

