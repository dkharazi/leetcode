# 314. Binary Tree Vertical Order Traversal

# Given a binary tree, return the vertical order traversal of its nodes' values.
# (ie, from top to bottom, column by column).

# If two nodes are in the same row and column, the order should be from left to right.

# Examples:
#
#     Given binary tree [3,9,20,null,null,15,7],
#
#        3
#       /\
#      /  \
#      9  20
#         /\
#        /  \
#       15   7
#
#     return its vertical order traversal as:
#
#     [
#       [9],
#       [3,15], #       [20],
#       [7]
#     ]
#
#     Given binary tree [3,9,8,4,0,1,7],
#
#          3
#         /\
#        /  \
#        9   8
#       /\  /\
#      /  \/  \
#      4  01   7
#
#     return its vertical order traversal as:
#
#     [
#       [4],
#       [9],
#       [3,0,1],
#       [8],
#       [7]
#     ]
#
#     Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5),
#
#          3
#         /\
#        /  \
#        9   8
#       /\  /\
#      /  \/  \
#      4  01   7
#         /\
#        /  \
#        5   2
#
#     return its vertical order traversal as:
#
#     [
#       [4],
#       [9,5],
#       [3,0,1],
#       [8,2],
#       [7]
#     ]
#

# https://www.geeksforgeeks.org/print-binary-tree-vertical-order/

# The idea is to traverse the tree once and get the minimum and maximum horizontal distance with respect to root.
# For the tree shown above, minimum distance is -2 (for node with value 4) and maximum distance is 3 (For node with value 9).

# Once we have maximum and minimum distances from root, we iterate for each vertical line at distance minimum to maximum from root,
# and for each vertical line traverse the tree and print the nodes which lie on that vertical line.

import collections

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Solution:

    # A utility function to find min and max distances with
    # respect to root
    def findMinMax(self, node, minimum, maximum, hd):
        if node is None:
            return
        if hd < minimum[0]:
            minimum[0] = hd
        elif hd > maximum[0]:
            maximum[0] = hd
        # recur for left and right subtrees
        self.findMinMax(node.left, minimum, maximum, hd-1)
        self.findMinMax(node.right, minimum, maximum, hd+1)


    # A utility function to print all nodes on a given line_no
    # hd is horizontal distance of current node with respect to root
    def printVerticalLine(self, node, line_no, hd):
        if node is None:
            return
        if hd == line_no:
            print node.data,
        self.printVerticalLine(node.left, line_no, hd-1)
        self.printVerticalLine(node.right, line_no, hd+1)

    def verticalOrder(self, root):
        minimum = [0]
        maximum = [0]
        self.findMinMax(root, minimum, maximum, 0)
        #print minimum[0], maximum[0]

        for line_no in range(minimum[0], maximum[0]+1):
            self.printVerticalLine(root, line_no, 0)
            print

    # https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/discuss/231256/python-queue-%2B-hash-map
    def verticalTraversal(self, root):
        g = collections.defaultdict(list)
        queue = [(root, 0)]
        while queue:
            new = []
            d = collections.defaultdict(list)
            for node, s in queue:
                d[s].append(node.val)
                if node.left:
                    new.append((node.left, s-1))
                if node.right:
                    new.append((node.right, s+1))
            for i in d:
                g[i].extend(sorted(d[i]))   # list1.extend(list2) --> list1 = list1 + list2
            queue = new
        return [g[i] for i in sorted(g)]    # sorted(g) = sorted(g.keys())

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)

#            1
#         /    \
#        2      3
#       / \    / \
#      4   5  6   7
#              \   \
#               8   9

    print "Vertical order traversal is"
    Solution().verticalOrder(root)


