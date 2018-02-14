# 283. Move Zeroes

# Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

# For example, given nums = [0, 1, 0, 3, 12],
# after calling your function, nums should be [1, 3, 12, 0, 0].


class Solution(object):
    # http://bookshadow.com/weblog/2015/09/19/leetcode-move-zeroes/
    # 使用两个"指针"x和y，初始令y = 0
    # 利用x遍历数组nums：
    # 若nums[x]非0，则交换nums[x]与nums[y]，并令y+1
    # y指针指向首个0元素可能存在的位置
    # 遍历过程中，算法确保[y, x)范围内的元素均为0
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        y = 0
        for x in range(len(nums)):
            if nums[x]:
                nums[x], nums[y] = nums[y], nums[x]
                y += 1

if __name__ == '__main__':
    nums1 = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums1)
    print(nums1)

    nums2 = [1, 0]
    Solution().moveZeroes(nums2)
    print(nums2)
