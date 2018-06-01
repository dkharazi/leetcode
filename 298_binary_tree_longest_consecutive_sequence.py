# 298: Binary Tree Longest Consecutive Sequence

# Given a binary tree, find the length of the longest consecutive sequence path.

# The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
# The longest consecutive path need to be from parent to child (cannot be the reverse).

# For example,
# 	
#    1
#     \
#      3
#     / \
#    2   4
#         \
#          5

# Longest consecutive sequence path is 3-4-5, so return 3.
	
#    2
#     \
#      3
#     / 
#    2    
#   / 
#  1

# Longest consecutive sequence path is 2-3,not 3-2-1, so return 2.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int


        There are three parameters of helper function, prev (the previous node), cur (the current node) 
        and length (the accumulated length before cur). 
        If cur.val == prev.val + 1, then we can continue exploring the current node’s children with length increased by 1. 
        Otherwise, refresh length. 
 
        The time complexity in the worst case will always be O(N) where N is the number of tree nodes.
        """
        if root is None:
            return 0

        self.res = 0    # global variable
        self.helper(root, root.left, 1)
        self.helper(root, root.right, 1)
        return self.res

    def helper(self, prev, cur, length):
        if cur is None:
            self.res = max(self.res, length)
            return

        if cur.val == prev.val + 1:
            self.helper(cur, cur.left, length+1)
            self.helper(cur, cur.right, length+1)
        else:
            self.res = max(self.res, length)
            self.helper(cur, cur.left, 1)
            self.helper(cur, cur.right, 1)


