# 287. Find the Duplicate Number

# Given an array nums containing n + 1 integers 
# where each integer is between 1 and n (inclusive),
# prove that at least one duplicate number must exist. 
# Assume that there is only one duplicate number, find the duplicate one.

# Note:

#     You must not modify the array (assume the array is read only).
#     You must use only constant, O(1) extra space.
#     Your runtime complexity should be less than O(n2).
#     There is only one duplicate number in the array, but it could be repeated more than once.

class Solution(object):
    # modifies array (sort)
    def findDuplicate(self, nums):
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

    # https://www.hrwhisper.me/leetcode-find-the-duplicate-number/
    # 如果数组中元素不重复，那么,任意下标i和数组中该下标的值一一对应，
    # 如 对于数组 3,4,1,2，有如下对应关系：（注意，值从1~n）

    #     0 – > 2
    #     1  -> 4
    #     2  -> 1
    #     3  -> 3

    # 设这个对应关系的运算函数为f(n) ，那么，我们从下标0出发，
    # 每次根据f取出下标i对应的值x，并将这个x作为下一次的下标，直到下标越界。

    # 如3，4，1，2这个数组，那么有 0 – > 2-> 1-> 4

    # 但如果有重复的话，中间就会产生多个映射，如3,4,1,2,3

    #     0 – > 2
    #     1  -> 4
    #     2  -> 1
    #     3  -> 3
    #     4  ->3

    # 继续这么做的话，会发生 0 – > 2-> 1-> 4  -> 3 -> 3->3……

    # 也就是最后一定是那个重复的元素。

    # 这样类似于  leetcode 142 Linked List Cycle II一样，找链表环路的起点，
    # 我们先用快慢两个下标都从0开始，快下标每轮运算两次，
    # 慢下标每轮运算一次，直到两个下标再次相同。
    # 这时候保持快下标位置不变，将慢下标移动到0，
    # 接着两个每轮分别运算一次，当这两个下标相遇时，就是环的起点，也就是重复的数。

    def findDuplicate(self, nums):
        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
