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

    # https://all4win78.wordpress.com/2016/07/11/leetcode-285-inorder-successor-in-bst/
    def inorderSuccessor(root, p):
        # p.right != null，说明可以从p.right开始找successor
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p

        # p.right == null，说明需要从root开始寻找，
        # 因为这个是BST，而且p没有right，所以successor一定是某个包含p的子树的root。
        # 因此我们可以用一个临时变量，也就是successor，来存当前找到的大于p.val的node，
        # 在从root往leaves寻找的时候，每次有新的node符合这个条件就更新这个临时变量，
        # 最后返回这个临时变量就可以。
        successor = None
        node = root
        while node.val != p.val:
            if node.val < p.val:
                node = node.right
            else:
                successor = node
                node = node.left
        return successor

