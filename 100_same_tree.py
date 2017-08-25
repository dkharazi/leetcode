"""
100. Same Tree

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical
and the nodes have the same value.

http://www.cnblogs.com/loadofleaf/p/5502249.html

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
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def dfs(p, q):
            if p is None and q is not None:
                return False
            if p is not None and q is None:
                return False
            if p is None and q is None:
                return True
            if p.val != q.val:
                return False
            return dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(p, q)


if __name__ == "__main__":
    p = TreeNode(0)
    # p.left = TreeNode(1)
    q = TreeNode(1)
    # q.left = TreeNode(1)

    print Solution().isSameTree(p, q)
