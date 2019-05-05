# 297. Serialize and Deserialize Binary Tree

# Serialization is the process of converting a data structure or object into a sequence of bits
# so that it can be stored in a file or memory buffer, or transmitted across a network connection link
# to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree.
# There is no restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string
# and this string can be deserialized to the original tree structure.

# For example, you may serialize the following tree

#     1
#    / \
#   2   3
#      / \
#     4   5

# as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree.
# You do not necessarily need to follow this format, so please be creative
# and come up with different approaches yourself.

# Note: Do not use class member/global/static variables to store states.
# Your serialize and deserialize algorithms should be stateless.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# https://gengwg.blogspot.com/2018/06/leetcode-297-serialize-and-deserialize.html
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/74259/Recursive-preorder-Python-and-C++-O(n)
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        vals = []
        def preorder(root):
            if root:
                vals.append(str(root.val))
                preorder(root.left)
                preorder(root.right)
            else:
                vals.append('#')
        preorder(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split())
        def doit():
            val = next(vals)
            if val == '#':
                return
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        root = doit()
        return root


if __name__ == '__main__':
    # Your Codec object will be instantiated and called as such:
    # codec = Codec()
    # codec.deserialize(codec.serialize(root))
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print((Codec().serialize(root)))
    print(Codec().deserialize((Codec().serialize(root))))
