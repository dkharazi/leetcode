# 285 Inorder Successor in BST

# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
#
# The successor of a node p is the node with the smallest key greater than p.val.
#
#
#
# Example 1:
#
# Input: root = [2,1,3], p = 1
# Output: 2
# Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.
#
# Example 2:
#
# Input: root = [5,3,6,2,4,null,null,1], p = 6
# Output: null
# Explanation: There is no in-order successor of the current node, so the answer is null.
#
#
#
# Note:
#
#     If the given node has no in-order successor in the tree, return null.
#     It's guaranteed that the values of the tree are unique.
#

# http://www.cnblogs.com/grandyang/p/5306162.html
# 这种方法充分地利用到了BST的性质，我们首先看根节点值和p节点值的大小，如果根节点值大，说明p节点肯定在左子树中，
# 那么此时我们先将res赋为root，然后root移到其左子节点，
# 循环的条件是root存在，我们再比较此时root值和p节点值的大小，如果还是root值大，我们重复上面的操作，
# 如果p节点值，那么我们将root移到其右子节点，
# 这样当root为空时，res指向的就是p的后继节点，：

class Solution:
    def inorderSuccessor(root, p):
        res = None
        while root:
            if root.val > p.val:
                res = root
                root = root.left
            else:
                root = root.right
        return res

