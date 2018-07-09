# 270. Closest Binary Search Tree Value

# Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

# Note:
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.

class Solution:

    # Record root.val and recursively search for the closest value:
    #    If root.val < target, search in the right sub-tree.
    # If abs(result - target) < abs(root.val - target), return result.
    #    If root.val >= target, search in the left sub-tree.
    # If abs(result - target) < abs(root.val - target), return result.

    def closestValue(self, root, target):
        closest = root.val
        if root.val < target:
            if root.right:
                right = self.closestValue(root.right, target)
                if abs(right - target) < abs(closest - target):
                    closest = right
        else:
            if root.left:
                left = self.closestValue(root.left, target)
                if abs(left - target) < abs(closest - target):
                    closest = left
        return closest
