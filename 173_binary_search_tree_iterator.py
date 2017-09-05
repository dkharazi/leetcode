# -*- coding: utf-8 -*-
# 173. Binary Search Tree Iterator
#
# Implement an iterator over a binary search tree (BST).
# Your iterator will be initialized with the root node of a BST.
#
# Calling next() will return the next smallest number in the BST.
#
# Note: next() and hasNext() should run in average O(1) time
# and uses O(h) memory, where h is the height of the tree.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
#
# https://shenjie1993.gitbooks.io/leetcode-python/173%20Binary%20Search%20Tree%20Iterator.html
# 要找到二叉搜索树中的最小节点，应该从根节点递归遍历左节点，
# 直到遍历的节点没有左节点，那么该节点就是二叉树中的最小节点。
# 现在已经有二叉搜索树中没有访问过的最小节点了，
# 那么当访问了该节点后，剩余没有访问的树中最小的节点在哪里呢？
# 如果该节点有右子树，那么在它的右子树中
# （又回到了找一棵二叉搜索树的最小元素，不过这棵二叉搜索树变小了）；
# 如果没有右子树，那么就是它的父节点。
# 为了能够快速定位到父节点，我们可以用栈将遍历路径暂存起来，
# 当进行next()操作时，我们弹出栈顶元素并进行访问，
# 如果它有右子树的话就遍历它的右子树；
# 如果没有右子树，当下次出栈操作时就是访问当前节点的父节点了。
#
# hasNext()和next()要连用，
# 如i.hasNext(): v.append(i.next())，
# 否则会抛出出栈异常，测试用例提供了这项保证


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self._pushLeft(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        self._pushLeft(node.right)
        return node.val

    def _pushLeft(self, node):
        while node:
            self.stack.append(node)
            node = node.left


if __name__ == '__main__':
    pass

    # Your BSTIterator will be called like this:
    # i, v = BSTIterator(root), []
    # while i.hasNext(): v.append(i.next())
