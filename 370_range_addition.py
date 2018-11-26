# 370. Range Addition

# Assume you have an array of length n initialized with all 0's and are given k update operations.

# Each operation is represented as a triplet: [startIndex, endIndex, inc]
# which increments each element of subarray A[startIndex ... endIndex]
# (startIndex and endIndex inclusive) with inc.
#
# Return the modified array after all k operations were executed.
#
# Example:
#
# Given:
#
#     length = 5,
#     updates = [
#         [1,  3,  2],
#         [2,  4,  3],
#         [0,  2, -2]
#     ]
#
# Output:
#
#     [-2, 0, 3, 5, 3]
#
# Explanation:
#
# Initial state:
# [ 0, 0, 0, 0, 0 ]
#
# After applying operation [1, 3, 2]:
# [ 0, 2, 2, 2, 0 ]
#
# After applying operation [2, 4, 3]:
# [ 0, 2, 5, 5, 3 ]
#
# After applying operation [0, 2, -2]:
# [-2, 0, 3, 5, 3 ]
#
# ---------------------
#
# 原文：https://blog.csdn.net/qq508618087/article/details/51864853


class Solution:
    # https://all4win78.wordpress.com/2016/06/29/leetcode-370-range-addition/
    # 在这题中没必要每次把区间的每一个值都更新, 只需要更新起点和终点后的一点即可.
    # 也就是说把增加的值放在起点, 终点后的一点减去增加的值,
    # 这样再扫描的时候把之前累加的和作为最终值即可.
    def getModifiedArray(self, length, updates):
        result = [0] * length
        for operation in updates:
            result[operation[0]] += operation[2]
            if operation[1] < length - 1:
                result[operation[1] + 1] -= operation[2]

        sum = 0
        for i in range(0, length):
            sum += result[i]
            result[i] = sum
        return result

length = 5
updates = [
        [1,  3,  2],
        [2,  4,  3],
        [0,  2, -2]
]

print(Solution().getModifiedArray(length, updates))
