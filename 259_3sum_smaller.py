# 259. 3Sum Smaller

# Given an array of n integers nums and a target,
# find the number of index triplets i, j, k with 0 <= i < j < k < n
# that satisfy the condition nums[i] + nums[j] + nums[k] < target.

# For example, given nums = [-2, 0, 1, 3], and target = 2.
# Return 2. Because there are two triplets which sums are less than 2:

# [-2, 0, 1]
# [-2, 0, 3]

# Follow up:
# Could you solve it in O(n2) runtime?

class Solution(object):
    # 思路： 3Sum的变种，要求统计三个数的和小于给定target的次数。
    # 先排序，然后用外层循环来确定第一个数， 内层循环用左右指针从两头往中间寻找。
    # 得到三个数的和，如果和大于等于target，说明找大了, right指针往左移动；
    # 如果找到的和小于target，我们取right-left的差值即为有效结果。
    # 为什么呢？ 假设left不动，那那么right像左移，直到重合之前的前一点都属于有效结果。
    def threeSumSmaller(self, nums, target):
        res = 0
        nums.sort()

        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < target:
                    res += k-j
                    j += 1
                else:
                    k -= 1
        return res

if __name__ == '__main__':
    print(Solution().threeSumSmaller([-2, 0, 1, 3], 2))
    print(Solution().threeSumSmaller([], 2))

