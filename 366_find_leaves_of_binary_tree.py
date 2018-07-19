# 366. Find Leaves of Binary Tree

# Given a binary tree, collect a tree's nodes as if you were doing this:
# Collect and remove all leaves, repeat until the tree is empty.

# Example:
# Given binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Returns [4, 5, 3], [2], [1].

# Explanation:
# 1. Removing the leaves [4, 5, 3] would result in this tree:
#           1
#          /
#         2
# 2. Now removing the leaf [2] would result in this tree:
#           1
# 3. Now removing the leaf [1] would result in the empty tree:
#           []
# Returns [4, 5, 3], [2], [1].

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        https://www.jianshu.com/p/ae3315ba7582
        we don't actually remove the leaves.
        Instead, we add a node to its correct list by calculating its height.
        明白了Binary Tree的Height和Depth的区别，
        Height是从下往上数，Leaf的height为0， Root的height最大；
        而Depth是从上往下数，root的depth为0， Leaf的depth最高。
        所以这道题说是Find leaves, 其实是把所有node按Height分，
        比如第一层所有的Leaf nodes就是height = 0的node;
        第二层的Leaf nodes就是height = 1的node;
        第三层的leaf nodes就是height = 3的nodes。
        这样发现这个问题其实只和height有关，就很好解决了。
        """
        res = []
        self.helper(root, res)
        return res

    def helper(self, node, res):
        if node is None:
            return -1   # so that level corresponds to res[] index
        level = 1 + max(self.helper(node.left, res), self.helper(node.right, res))
        if len(res) < level + 1:
            res.append([])
        res[level].append(node.val)
        return level

s = Solution()
