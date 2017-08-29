# -*- coding: utf-8 -*-
# 129. Sum Root to Leaf Numbers
#
# Given a binary tree containing digits from 0-9 only,
# each root-to-leaf path could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# For example,
#
#     1
#    / \
#   2   3
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
#
# Return the sum = 12 + 13 = 25.
#
#
# http://www.cnblogs.com/zuoyuan/p/3721420.html
#
# 解题思路：看到二叉树，我们首先想到递归。比如一棵树如下：
#
# 　　　　　　　　　　　　　　　　　　　　　　1
#
# 　　　　　　　　　　　　　　　　　　　　　/     \
#
# 　　　　　　　　　　　　　　　　　　　　 2　　  3
#
# 　　　　　　　　　　　　　　　　　　　 /    \    /   \
#
# 　　　　　　　　　　　　　　　　　　  4      5 6      7
#
# 　　　　　此题求和为sum=124+125+136+137，
# 我们可以使用一个preSum变量来记录从根节点到节点父亲的路径，
# 比如当我们递归的4时，preSum=12，
# 递归到6时，preSum=13，这样就可以了。
# 具体看代码。


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sum(root, 0)

    def sum(self, root, preSum):
        if root is None:
            return 0
        preSum = preSum * 10 + root.val
        if root.left is None and root.right is None:
            return preSum
        return self.sum(root.left, preSum) + self.sum(root.right, preSum)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print Solution().sumNumbers(root)