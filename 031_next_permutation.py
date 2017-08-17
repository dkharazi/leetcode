# -*- coding: utf-8 -*-
"""
31. Next Permutation

Implement next permutation, which rearranges numbers into
the lexicographically next greater permutation of numbers.

If such arrangement is not possible,
it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples.
Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 --> 1,3,2
3,2,1 --> 1,2,3
1,1,5 --> 1,5,1

解题思路：输出字典序中的下一个排列。
比如123生成的全排列是：123，132，213，231，312，321。
那么321的next permutation是123。

下面这种算法据说是STL中的经典算法。
在当前序列中，从尾端往前寻找两个相邻升序元素，升序元素对中的前一个标记为partition。
然后再从尾端寻找另一个大于partition的元素，并与partition指向的元素交换，
然后将partition后的元素（不包括partition指向的元素）逆序排列。
比如14532，那么升序对为45，partition指向4，
由于partition之后除了5没有比4大的数，
所以45交换为54，即15432，
然后将partition之后的元素逆序排列，即432排列为234，
则最后输出的next permutation为15234。
确实很巧妙。
"""

import itertools


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # itertools Permutations are emitted in lexicographic sort order
        # for perm in itertools.permutations(sorted(nums)):
        #    if tuple(nums) == perm:
        #        return perm

        # if the input iterable is sorted, the permutation tuples will be produced in sorted order.
        it = itertools.permutations(sorted(nums))
        while True:
            try:
                if tuple(nums) == next(it):
                    return list(next(it))
            except StopIteration:
                it = itertools.permutations(sorted(nums))
                return list(next(it))
                # break

    # http://www.cnblogs.com/zuoyuan/p/3780167.html
    def nextPermutation(self, nums):
        if len(nums) <= 1: return nums

        partition = -1
        # i: len-2, len-3, .. 1, 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                partition = i
                break

        if partition == -1:
            nums.reverse()
            return nums
        else:
            # start from end of list, find one that is bigger than partition
            # exchange them
            for i in range(len(nums)-1, partition, -1):
                if nums[i] > nums[partition]:
                    nums[i], nums[partition] = nums[partition], nums[i]
                    break

        # reverse order everything after partition
        left = partition + 1; right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1; right -= 1

        return nums


if __name__ == '__main__':
    print Solution().nextPermutation([1, 3, 2])
    print Solution().nextPermutation([1, 2])
    print Solution().nextPermutation([1])
    print Solution().nextPermutation([1, 1, 5])