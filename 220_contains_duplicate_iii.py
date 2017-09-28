# -*- coding: utf-8 -*-
# 220. Contains Duplicate III
#
# Given an array of integers,
# find out whether there are two distinct indices i and j in the array
# such that the absolute difference between nums[i] and nums[j] is at most t
# and the absolute difference between i and j is at most k.


import collections


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool

        http://bookshadow.com/weblog/2015/06/03/leetcode-contains-duplicate-iii/

        解法I：“滑动窗口” + 字典（桶）

        如果： | nums[i] - nums[j] | <= t   式a

        等价： | nums[i] / t - nums[j] / t | <= 1   式b

        推出： | floor(nums[i] / t) - floor(nums[j] / t) | <= 1   式c

        ​等价： floor(nums[j] / t) ∈ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1} 式d

        其中式b是式c的充分非必要条件，因为逆否命题与原命题等价，所以：

        如果： floor(nums[j] / t) ∉ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1} 非d

        推出： | nums[i] - nums[j] | > t   非a

        因此只需要维护一个大小为k的窗口（字典）numDict，其中键为nums[i] / t，值为nums[i]。

        遍历数组nums时，检查nums[i]与键集{floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1}对应的值的差值即可。
        """

        if k < 1 or t < 0:
            return False

        numDict = collections.OrderedDict()
        for i in range(len(nums)):
            key = nums[i] / max(1, t)
            for m in (key, key - 1, key + 1):
                if m in numDict and abs(nums[i] - numDict[m]) <= t:
                    return True
            numDict[key] = nums[i]
            if i >= k:
                numDict.popitem(last=False)
        return False

    # https://www.hrwhisper.me/leetcode-contains-duplicate-i-ii-iii/
    # 桶的方法 O(n)
    #
    # 思想是分成t+1个桶，对于一个数，将其分到第num / (t + 1) 个桶中，我们只需要查找相同的和相邻的桶的元素就可以判断有无重复。
    #
    # 比如t = 4，那么0~4为桶0，5~9为桶1，10~14为桶2  然后你懂的- –
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0:
            return False
        div = t + 1
        vis = {}
        for i, num in enumerate(nums):
            index = num / div
            if index in vis \
                    or index - 1 in vis and abs(vis[index - 1] - num) <= t \
                    or index + 1 in vis and abs(vis[index + 1] - num) <= t:
                return True
            vis[index] = num
            if i >= k:
                del vis[nums[i - k] / div]
        return False


if __name__ == '__main__':
    print Solution().containsNearbyAlmostDuplicate([2, 5, 3, 9], 1, 1)
    print Solution().containsNearbyAlmostDuplicate([-1, -1], 1, 0)
