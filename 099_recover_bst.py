# -*- coding: utf-8 -*-
"""
99. Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        if self:
            serial = []
            queue = [self]

            while queue:
                cur = queue[0]

                if cur:
                    serial.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    serial.append("#")

                queue = queue[1:]

            while serial[-1] == "#":
                serial.pop()

            return repr(serial)

        else:
            return None


class Solution(object):
    def recoverTree(self, root):
        """
        算法一：思路很简单，一颗二叉查找树的中序遍历应该是升序的，
        而两个节点被交换了，那么对这个错误的二叉查找树中序遍历，肯定不是升序的。
        那我们只需把顺序恢复过来然后进行重新赋值就可以了。

        开辟两个列表，list用来存储被破坏的二叉查找树的节点值，
        listp用来存储二叉查找树的节点的指针。
        然后将list排序，再使用listp里面存储的节点指针赋值就可以了。

        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        list = []
        listp = []
        self.inorder(root, list, listp)
        list.sort()
        for i in range(len(list)):
            listp[i].val = list[i]
        return root

    def inorder(self, root, list, listp):
        if root:
            self.inorder(root.left, list, listp)
            list.append(root.val)
            listp.append(root)
            self.inorder(root.right, list, listp)


if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    print root
    print Solution().recoverTree(root)
