# 217. Contains Duplicate
#
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.


class Solution(object):
    # use hash map to mark if num already appeared
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        for num in nums:
            if num in dict:
                return True
            dict[num] = 1
        return False
    # same as above, using set().
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False

    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

    # sort, then compare each element with next
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False


if __name__ == '__main__':
    print Solution().containsDuplicate([2, 3, 2, 1, 2])
