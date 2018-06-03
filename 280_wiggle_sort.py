# 280. Wiggle Sort

# Given an unsorted array nums, reorder it in-place such that 
# nums[0] <= nums[1] >= nums[2] <= nums[3]....

# For example, given nums = [3, 5, 2, 1, 6, 4], 
# one possible answer is [1, 6, 2, 5, 3, 4].

# the pattern is number in odd position is peak.

# First try to solve it without in-place:

#     sort the array in increasing order.
#     create a result array of the same size.
#     keep 2 pointers, one from the beginning, one from the middle(notice odd/even of array).
#     put beginning first, then the middle pointer, into the result array.

# Solve it in-place.

class Solution(object):
    # sort and swap(i,i+1) with step 2
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1, len(nums)-1, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]

    # 排序，然后两边分别取，复杂度O(nlogn)
    # 注意排完序之后应该倒着来。比如[4,5,5,6]这个 数据。
    def wiggleSort(self, nums):
        temp = sorted(nums)
        s = (len(nums) + 1) >> 1
        t = len(nums)
        for i in range(len(nums)):
            if i & 1 == 0:
                s -= 1
                nums[i] = temp[s]
            else:
                t -= 1
                nums[i] = temp[t]

    # The result needs to guarantee that when i is odd, nums[i] >= nums[i - 1]; 
    # when i is even, nums[i] <= nums[i - 1]. 
    # The idea is that, whenever we see a nums[i] that violates this rule, 
    # we swap it with nums[i - 1]. 
    # This will work because if i is odd and nums[i] < nums[i - 1], 
    # nums[i] is also always less than nums[i - 2]; 
    # if i is even and nums[i] > nums[i - 1], nums[i] is also always larger than nums[i - 2]. 
    # So swapping will not violate the relationship between nums[i - 1] and nums[i - 2].
    def wiggleSort(self, nums):
        for i in range(1, len(nums)):
            if ((i&1) and (nums[i] < nums[i-1])) or (not(i&1) and (nums[i] > nums[i-1])):
                nums[i], nums[i-1] = nums[i-1], nums[i]
        print(nums)                
            
nums = [3, 5, 2, 1, 6, 4]
Solution().wiggleSort(nums)