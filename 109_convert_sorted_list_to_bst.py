"""
109. Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.


"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        http://www.cnblogs.com/zuoyuan/p/3722114.html

        push node values into an array, then use solution of 108...

        :type head: ListNode
        :rtype: TreeNode
        """
        p = head
        array = []
        # push linked list values to array
        while p:
            array.append(p.val)
            p = p.next

        return self.sortedArrayToBST(array)

    def sortedArrayToBST(self, array):
        n = len(array)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(array[0])
        root = TreeNode(array[n / 2])
        root.left = self.sortedArrayToBST(array[:n/2])
        root.right = self.sortedArrayToBST(array[n/2 + 1:])
        return root

    # two pointers
    # https://gengwg.blogspot.com/2018/03/leetcode-109-convert-sorted-list-to.html
    def sortedListToBST(self, head):
        if head is None:
            return None
        return self.helper(head, None)

    def helper(self, head, tail):
        if head == tail:
            return None
        slow = head
        fast = head
        # slow fast pointers to find middle of list
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next

        root = TreeNode(slow.val)
        root.left = self.helper(head, slow)
        root.right = self.helper(slow.next, tail)
        return root
