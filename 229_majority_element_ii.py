# 229. Majority Element II
#
# Given an integer array of size n,
# find all elements that appear more than n/3  times.
# The algorithm should run in linear time and in O(1) space.
#

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        http://bookshadow.com/weblog/2015/06/29/leetcode-majority-element-ii/

        https://leetcode.com/problems/majority-element-ii/discuss/63520/Boyer-Moore-Majority-Vote-algorithm-and-my-elaboration

        可以从Moore投票算法中得到一些启发

        观察可知，数组中至多可能会有2个出现次数超过 ⌊ n/3 ⌋ 的众数

        记变量n1, n2为候选众数； c1, c2为它们对应的出现次数

        遍历数组，记当前数字为num

        若num与n1或n2相同，则将其对应的出现次数加1

        否则，若c1或c2为0，则将其置为1，对应的候选众数置为num

        否则，将c1与c2分别减1

        最后，再统计一次候选众数在数组中出现的次数，若满足要求，则返回之。
        """
        n1 = n2 = None
        c1 = c2 = 0
        for num in nums:
            if num == n1:
                c1 += 1
            elif num == n2:
                c2 += 1
            elif c1 == 0:
                n1 = num
                c1 = 1
            elif c2 == 0:
                n2 = num
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        size = len(nums)
        return [n for n in (n1, n2) if n is not None and nums.count(n) > size/3]

    # O(n) space
    def majorityElement(self, nums):
        res = []
        if not nums:
            return []
        for num in set(nums):
            if nums.count(num) > len(nums)/3:
                res.append(num)
        return res

    # 1 liner. O(n) space.
    def majorityElement(self, nums):
        return [n for n in set(nums) if nums.count(n) > len(nums)/3]

