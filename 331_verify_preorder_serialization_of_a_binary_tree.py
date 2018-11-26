# 331. Verify Preorder Serialization of a Binary Tree

# One way to serialize a binary tree is to use pre-order traversal.
# When we encounter a non-null node, we record the node's value.
# If it is a null node, we record using a sentinel value such as #.
#
#      _9_
#     /   \
#    3     2
#   / \   / \
#  4   1  #  6
# / \ / \   / \
# # # # #   # #
#
# For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#",
# where # represents a null node.
#
# Given a string of comma separated values, verify whether it is a correct preorder traversal serialization
# of a binary tree. Find an algorithm without reconstructing the tree.
#
# Each comma separated value in the string must be either an integer or a character '#' representing null pointer.
#
# You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".
#
# Example 1:
#
# Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true
#
# Example 2:
#
# Input: "1,#"
# Output: false
#
# Example 3:
#
# Input: "9,#,#,1"
# Output: false
#

class Solution:
    # https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/78564/The-simplest-python-solution-with-explanation-(no-stack-no-recursion)
    # We just need to remember how many empty slots we have during the process.
    # Initially we have one ( for the root ).
    # for each node we check if we still have empty slots to put it in:
    #       a null node occupies one slot.
    #       a non-null node occupies one slot before he creates two more. the net gain is one.
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(',')
        slot = 1            # initially we have one empty slot to put the root in
        for node in nodes:
            if slot == 0:   # no empty slot to put current node in
                return False
            if node == '#': # a null node?
                slot -= 1   # occupy 1 slot
            else:           # a non-null node?
                slot += 1   # create new slot
        return slot == 0    # we don't allow empty slots at the end

sol = Solution()
print(sol.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
print(sol.isValidSerialization("1,#"))
