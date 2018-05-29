#  219. Contains Duplicate II
#
#  Given an array of integers and an integer k,
# find out whether there are two distinct indices i and j in the array
# such that nums[i] = nums[j] and the absolute difference between i and j is at most k.


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = i
            else:
                if i - dict[nums[i]] <= k:
                    return True
                else:   # distance larger than k. replace with current position
                    dict[nums[i]] = i

        return False

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dict = {}
        for idx, num in enumerate(nums):
            if num not in dict:
                dict[num] = idx
            else: # num in dict
                # idx diff smaller than k
                if idx - dict[num] <= k:
                    return True
                else: # idx diff larger than k
                    # replace with current position, so that later diff may be smaller than k
                    dict[nums[i]] = i
        return False

    # shorter version. test in map first.
    def containsNearbyDuplicate(self, nums, k):
        num_map = {}
        for i in range(len(nums)):
            if nums[i] in num_map and i - num_map[nums[i]] <= k:
                return True
            num_map[nums[i]] = i
        return False
